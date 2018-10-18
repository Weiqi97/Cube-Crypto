"""Defines the encryption protocol."""

import binascii
import numpy as np
from typing import List
from collections import deque
from cube_encryption.cube import Cube
from cube_encryption.constants import CUBE_MOVE, MOVE_ANGLE, CUBIE_LENGTH, Key


class Encryption:
    """Perform encryption and decryption of the input."""

    def __init__(self, message: str, cube_side_length: int):
        """Put the message into a cube and create a queue to hold keys.

        :param message: The message to encrypt.
        :param cube_side_length: The desired length of cube side.
        """
        # Store the cube max index.
        self._cube_max_index = int(np.floor(cube_side_length / 2))
        # Find the size of each block.
        block_size = cube_side_length ** 2 * 6 * CUBIE_LENGTH
        # Convert the string to binary numbers.
        binary_str = self.string_to_binary(message)
        # Pad the binary string for the encryption.
        binary_str_padded = self._pad_binary_str(
            input_string=binary_str, block_size=block_size
        )
        # Find number of blocks required.
        cube_required = len(binary_str_padded) / block_size

        # Create the cube object.
        self._cubes = [
            Cube(
                cube_input=message_chunk, cube_side_length=cube_side_length
            )
            for message_chunk in np.array_split(
                ary=list(binary_str_padded), indices_or_sections=cube_required
            )
        ]
        self._key = deque()

    @staticmethod
    def _pad_binary_str(input_string: str, block_size: int) -> str:
        """Pad the binary string so it can fill each cube chunk.

        :param input_string: The binary string need to be padded.
        :param block_size: Number of bits each cube can hold.
        :return: The padded binary string.
        """
        # Find the number of block required for the encryption.
        num_block_need = int(np.ceil(len(input_string) / block_size))
        # Find the number of extra zero needed.
        extra_zero_need = num_block_need * block_size - len(input_string) - 2
        # Deal with special case.
        extra_zero_need = \
            block_size - 2 if extra_zero_need == -2 else extra_zero_need

        # Return the padded string.
        return f"{input_string}01{'0' * extra_zero_need}"

    @staticmethod
    def string_to_binary(input_string: str) -> str:
        """Convert Ascii string to binary string.

        :param input_string: An input Ascii encoded string.
        :return: The binary encoded equivalence of the input Ascii string.
        """
        string_to_byte = binascii.a2b_qp(input_string)
        byte_to_binary = bin(int.from_bytes(string_to_byte, byteorder="big"))
        byte_to_binary = byte_to_binary.replace("b", "")
        # Make sure what ever being returned is multiple of 8.
        return f"{'0' * (8 - len(byte_to_binary) % 8)}{byte_to_binary}" \
            if len(byte_to_binary) % 8 != 0 \
            else byte_to_binary

    @staticmethod
    def binary_to_string(input_binary: str) -> str:
        """Convert binary string to Ascii string.

        :param input_binary: An input binary encoded string.
        :return: The Ascii encoded equivalence of the input binary string.
        """
        string_to_binary = int(input_binary, 2)
        binary_to_byte = string_to_binary.to_bytes(
            length=(string_to_binary.bit_length() + 7) // 8,
            byteorder="big"
        )
        return binary_to_byte.decode("utf-8")

    def get_pad_binary(self) -> str:
        """Get the padded binary string at the current state."""
        return "".join([cube.content for cube in self._cubes])

    def get_un_pad_binary(self) -> str:
        """Remove the padding from the current binary string."""
        # NOTE! This function should not be used while the cube is encrypted.
        un_pad_string = self.get_pad_binary().rstrip("0")
        return un_pad_string[:-2]

    def get_pad_string(self):
        """Return current padded Ascii string."""
        return self.binary_to_string(input_binary=self.get_pad_binary())

    def get_un_pad_string(self):
        """Return current un-padded Ascii string."""
        return self.binary_to_string(input_binary=self.get_un_pad_binary())

    def generate_random_key(self, length: int) -> List[Key]:
        """Generate a randomized key based on the input length.

        :param length: The desired key length.
        :return: A list of key object, each key contains move and angle.
        """
        # Helper function for generating one key.
        def generate_one_key() -> Key:
            """Generate key with random move, angle and index based on move."""
            return Key(
                move=np.random.choice(CUBE_MOVE, size=1)[0],
                angle=np.random.choice(MOVE_ANGLE, size=1)[0],
                index=np.random.randint(low=1, high=self._cube_max_index + 1)
            )

        return [generate_one_key() for __ in range(length)]

    def encrypt(self, key: List[Key]):
        """Encrypt the message based on a given key.

        :param key: A list of keys used for encryption.
        """
        # Loop through all the keys.
        for each_key in key:
            # Shift all the cubes.
            for cube in self._cubes:
                # Shift cube.
                cube.shift(key=each_key)
                # Shuffle bits.
                cube.shift_cubie_content()
            # Append the used key to key list.
            self._key.append(each_key)

    def decrypt(self):
        """Decrypt the message to plain text."""
        while self._key:
            # Pop the key from saved keys.
            each_key = self._key.pop()
            for cube in self._cubes:
                # Shift content backward by one space.
                cube.shift_cubie_content_back()
                # Reverse the cube shift move.
                cube.shift(
                    key=Key(
                        move=each_key.move,
                        angle=360 - each_key.angle,
                        index=each_key.index
                    )
                )
