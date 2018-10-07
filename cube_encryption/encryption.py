"""Defines the encryption protocol."""
import numpy as np
from typing import List
from collections import deque
from cube_encryption.cube import Cube
from cube_encryption.constants import CUBE_MOVE, MOVE_ANGLE, Key


class Encryption:
    """Perform encryption and decryption of the input."""

    def __init__(self, message: str):
        """Put the message into a cube and create a queue to hold keys."""
        self._cube = Cube(cube_input=message)
        self._key = deque()

    @staticmethod
    def string_to_binary(input_string: str) -> str:
        string_to_byte = binascii.a2b_qp(input_string)
        byte_to_binary = bin(int.from_bytes(string_to_byte, byteorder="big"))
        return byte_to_binary.replace("b", "")

    @staticmethod
    def binary_to_string(input_binary: str) -> str:
        string_to_binary = int(input_binary, 2)
        binary_to_byte = string_to_binary.to_bytes(
            length=(string_to_binary.bit_length() + 7) // 8,
            byteorder="big"
        )
        return binary_to_byte.decode("utf-8")

    @staticmethod
    def generate_random_key(length: int) -> List[Key]:
        """Generate a randomized key based on the input length.

        :param length: The desired key length.
        :return: A list of key object, each key contains move and angle.
        """
        return [
            Key(
                move=np.random.choice(CUBE_MOVE, size=1),
                angle=np.random.choice(MOVE_ANGLE, size=1)
            )
            for __ in range(length)
        ]

    def encrypt(self, key: List[Key]):
        """Encrypt the message based on a given key."""
        for each_key in key:
            self._cube.shift(
                move=each_key.move,
                angle=each_key.angle
            )
            self._key.append(each_key)

    def decrypt(self):
        """Decrypt the message to plain text."""
        while self._key:
            key = self._key.pop()
            self._cube.shift(
                move=key.move,
                angle=(360 - key.angle)
            )

    def print_formatted_cube(self):
        """Print current cube state as formatted string."""
        print(self._cube.get_cube_formatted())

    def print_message(self):
        """Print current cube state as plain text string."""
        print(self._cube.get_cube_string())
