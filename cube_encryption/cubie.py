"""Define contents and operations of a cubie."""
from collections import deque
from cube_encryption.constants import MOVE_ANGLE


class Cubie:
    """Create a cubie with 4 bits on the given input."""
    def __init__(self, cubie_input: str):
        # Error check. Each cubie should only hold 4 bits.
        assert len(cubie_input) == 4, "Wrong input length for cubie."
        # Fill in the input bits as a queue.
        self._content = deque(cubie_input)

    def get_content(self) -> deque:
        """Return the content as a deque object."""
        return self._content

    def get_content_string(self) -> str:
        """Return the content as a string."""
        return "".join(map(str, self._content))

    def rotate_by_angle(self, angle: int):
        """Rotate the cubie content by desired angle.

        :param angle: The angle of desired rotation.
        """
        # Error check. Only possible angles are 90, 180 and 270 degrees.
        assert angle in MOVE_ANGLE, "Wrong rotating angle."
        # Find how many clockwise 90 degree is needed.
        rotate_step = int(angle / 90)
        # Do the desired amount of rotations.
        self._content.rotate(n=rotate_step)
