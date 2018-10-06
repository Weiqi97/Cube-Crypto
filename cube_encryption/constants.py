"""Constants for the project."""
from enum import Enum
from typing import NamedTuple

# ------------------------------- Constants ----------------------------------
# Set side length of the cube.
SIDE_LENGTH = 3
CUBIE_LENGTH = 4
MOVE_ANGLE = [90, 180, 270]
CUBE_MOVE = ["right", "left", "top", "bottom", "front", "back",
             "top_center_row", "top_center_col", "front_center_row"]


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
    bottom = "bottom"
    front = "front"
    back = "back"
    top_center_row = "top_center_row"
    top_center_col = "top_center_col"
    front_center_row = "front_center_row"


# ---------------------------- Error Messages --------------------------------
# Error messages for the Cubie class.
WRONG_CUBIE_INPUT = "The input length does not match the length of a cubie."
# Error messages for the CubeFace class.
WRONG_CUBE_FACE_INPUT = "The input length does not match the desired length " \
                        "of a cube face"
WRONG_SIDE_LENGTH = "The input length does not match the cube side length."

# Error messages for cross project usage.
WRONG_ROTATION_ANGLE = "Wrong rotation angle for the cube."


WRONG_LENGTH = "The input object length does not match the desired length."
WRONG_CUBE_MOVE = "The input cube move is undefined."
