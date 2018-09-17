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
