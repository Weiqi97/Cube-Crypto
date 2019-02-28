"""Defines the encryption protocol."""

import math
import random
import numpy as np
from typing import List
from collections import deque
from content.helper.constants import Key, CUBIE_LENGTH
from content.encryption.cube_for_cubie import CubeForCubie
from content.helper.helper import xor, binary_to_string, string_to_binary


class Encryption:
    """Perform encryption and decryption of the input."""

    def __init__(self, message: str, cube_side_length: int):
        """Put the message into a cube and create a queue to hold keys.

        :param message: The message to encrypt.
        :param cube_side_length: The desired length of cube side.
        """
        # Store the important information for other method to access.
        self._message = message
        self._max_index = math.floor(cube_side_length / 2)
        self._block_size = cube_side_length ** 2 * 3 * CUBIE_LENGTH

        # Initialize the random chunks saver.
        self._random_bits = []

        # Get the cubes.
        self._cubes = [
            CubeForCubie(
                cube_input=input_str, cube_side_length=cube_side_length
            )
            for input_str in self._get_binary_to_encrypt
        ]

        # Set up the holder for the key.
        self._key = deque()

    @property
    def _get_binary_to_encrypt(self) -> List[str]:
        """Convert the message to binary chunks and xor then with random bits.

        :return: A list of binary chunks where each chunk contains:
            - The first half is XOR result of original message
            - The second half if random bits generated
        """
        # Obtain the binary string.
        binary_str = string_to_binary(self._message)

        # Obtain the padded binary string.
        binary_str_padded = self._pad_binary_str(
            input_string=binary_str, block_size=self._block_size
        )

        # Find number of blocks required.
        cube_required = int(len(binary_str_padded) / self._block_size)

        # Split the binary into number of cubes required.
        binary_chunks = np.array_split(
            ary=list(binary_str_padded), indices_or_sections=cube_required
        )

        self._random_bits = [
            self._get_random_str for _ in range(cube_required)
        ]

        # Return input for each cube.
        return [
            xor(str_one="".join(binary),
                str_two=self._random_bits[index]) + self._random_bits[index]
            for index, binary in enumerate(binary_chunks)
        ]

    @property
    def _get_random_str(self) -> str:
        """Generate random binary string with the length of block size.

        :return: A random binary string with the length of half a cube.
        """
        # Random pick 0 or 1 in size of half of a cube.
        return "".join([
            str(random.randint(0, 1)) for _ in range(self._block_size)
        ])

    @staticmethod
    def _pad_binary_str(input_string: str, block_size: int) -> str:
        """Pad the binary string so it can fill each cube chunk.

        :param input_string: The binary string need to be padded.
        :param block_size: Number of bits each cube can hold.
        :return: The padded binary string.
        """
        # Find the number of block required for the encryption.
        num_block_need = math.ceil(len(input_string) / block_size)
        # Find the number of extra zero needed.
        extra_zero_need = num_block_need * block_size - len(input_string) - 2
        # Deal with special case.
        extra_zero_need = \
            block_size - 2 if extra_zero_need == -2 else extra_zero_need

        # Return the padded string.
        return f"{input_string}01{'0' * extra_zero_need}"

    def get_current_binary(self) -> str:
        """Get the padded binary string at the current state."""
        return "".join([cube.content for cube in self._cubes])

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

    def get_decrypted_str(self) -> str:
        """Decrypt the message and return the original input.

        :return: The original message that was encrypted as a string.
        """
        # First make sure that all cubes are decrypted.
        self.decrypt()
        # Retract the binary after XOR operation.
        decrypted_binary = [
            xor(
                str_one=cube.content[:self._block_size],
                str_two=cube.content[self._block_size:]
            ) for cube in self._cubes
        ]
        # Un-pad the binary result. (Remove all 0's at the end.)
        up_pad_binary = "".join(decrypted_binary).rstrip("0")[:-2]

        # Convert the un-pad binary to a string and return it.
        return binary_to_string(up_pad_binary)
