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
            self.cube.shift(
                move=each_key.move,
                angle=each_key.angle
            )
            self.key.append(each_key)

    def decrypt(self):
        """Decrypt the message to plain text."""
        while self.key:
            key = self.key.pop()
            self.cube.shift(
                move=key.move,
                angle=(360 - key.angle)
            )

#
# protocol = Encryption(
#     message="111111111222222222333333333444444444555555555666666666"
# )
# protocol.cube.print_cube()
# key = protocol.generate_random_key(length=25)
# protocol.encrypt(key=key)
# protocol.cube.print_cube()
# key = protocol.generate_random_key(length=25)
# protocol.encrypt(key=key)
# protocol.cube.print_cube()
# protocol.decrypt()
# protocol.cube.print_cube()
