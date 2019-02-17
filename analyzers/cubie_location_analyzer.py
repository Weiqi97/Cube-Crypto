"""Defines the CubieItem location analyzer."""

from typing import List
from cube_encryption.cube_for_cubie import CubeForCubie


class CubieLocationAnalyzer:
    """Create the location analyzer based on the locations to keep track of."""

    def __init__(self, cube_side_length: int, track_item_location: List[int]):
        """Initialize the cubie location analyzer with desired parameters.

        :param cube_side_length: Length of the cube desired to be analyzed.
        :param track_item_location: Locations of items interested.
        """
        cube_input = "_" * cube_side_length ** 2 * 24
        CubeForCubie(
            cube_input=cube_input,
            cube_side_length=cube_side_length,
            track_item_location=track_item_location
        )
