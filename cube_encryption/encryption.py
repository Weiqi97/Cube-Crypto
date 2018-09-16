"""Defines the encryption protocol."""
import numpy as np
from typing import List
from collections import deque
from cube_encryption.cube import Cube
from cube_encryption.constants import Key, CUBE_MOVE, MOVE_ANGLE


class Encryption:
    """Perform encryption and decryption of the input."""

    def __init__(self, message: str):
        """Put the message into a cube and create a queue to hold keys."""
        self.cube = Cube(cube_input=message)
        self.key = deque()

    @staticmethod
    def generate_random_key(length: int) -> List[Key]:
        return [
            Key(
                move=np.random.choice(CUBE_MOVE, size=1),
                angle=np.random.choice(MOVE_ANGLE, size=1)
            )
            for __ in range(length)
        ]

    def encrypt(self, key: List[Key]):
        for each_key in key:
            self.cube.shift(
                move=each_key.move,
                angle=each_key.angle
            )
            self.key.append(each_key)

    def decrypt(self):
        while self.key:
            key = self.key.pop()
            self.cube.shift(
                move=key.move,
                angle=(360 - key.angle)
            )

