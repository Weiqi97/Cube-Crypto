"""Constants for the project."""
from enum import Enum
from typing import NamedTuple

# ------------------------------- Constants ----------------------------------
# Set side length of the cube.
SIDE_LENGTH = 3
CUBIE_LENGTH = 4
MOVE_ANGLE = [90, 180, 270]
CUBE_MOVE = ["right", "left", "top", "down", "front", "back"]


class Key(NamedTuple):
    """Define the components of a legal key."""

    move: str
    angle: int


# Set enum object for moves.
class CubeMove(Enum):
    """Define the legal moves for a cube."""

    left = "left"
    right = "right"
    top = "top"
    down = "down"
    front = "front"
    back = "back"


# ---------------------------- Error Messages --------------------------------
# Error messages for the Cubie class.
WRONG_CUBIE_INPUT = "The input length does not match the length of a cubie."

# Error messages for the CubeFace class.
WRONG_SIDE_LENGTH = "The input length does not match the cube side length."
INDEX_OUT_CUBE_LENGTH = "The given index is larger than the cube side length."
WRONG_CUBE_FACE_INPUT = "The input length does not match the desired length " \
                        "of a cube face"

# Error messages for the Cube class.
WRONG_CUBE_MOVE = "The input cube move is undefined."
WRONG_CUBE_SIDE_LENGTH = "The input cube side length is too short."
WRONG_CUBE_INPUT = "The input length does not match size of the entire cube."

# Error messages for cross project usage.
WRONG_ROTATION_ANGLE = "Wrong rotation angle for the cube."
