"""Constants for the project."""
from enum import Enum

# ------------------------------- Constants ----------------------------------
# Set side length of the cube.
SIDE_LENGTH = 3
MOVE_ANGLE = [90, 180, 270]
CUBE_MOVE = ["right", "left", "top", "bottom", "front", "back",
             "top_center_row", "top_center_col", "front_center_row"]


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
# Error message when input length is wrong.
WRONG_LENGTH = "The input object length does not match the desired length."
WRONG_CUBE_MOVE = "The input cube move is undefined."
