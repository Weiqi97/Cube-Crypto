"""Defines the CubieItem location analyzer."""

import math
from typing import List
from content.encryption.constants import Key, CUBE_MOVE, MOVE_ANGLE
from content.encryption.cube_for_cubie import CubeForCubie


class CubieLocationAnalyzer:
    """Create the location analyzer based on the location to keep track of."""

    def __init__(self, cube_side_length: int, track_item_location: int):
        """Initialize the cubie location analyzer with desired parameters.

        :param cube_side_length: Length of the cube desired to be analyzed.
        :param track_item_location: Locations of item interested.
        """
        # Store the cube side length.
        self.side_length = cube_side_length
        # Store the total cube size.
        self.cube_size = cube_side_length ** 2 * 24
        # Store the location of the tracked item.
        self.track_item_location = track_item_location

    def get_all_basic_key(self) -> List[Key]:
        """Get all the possible keys with fixed 90 degrees.

        :return: A list of basic keys.
        """
        return [
            Key(move=move, angle=90, index=index)
            for move in CUBE_MOVE
            for index in range(1, math.floor(self.side_length / 2) + 1)
        ]

    def check_effective_key(self, key: Key) -> bool:
        """Check if the given key moves the tracked item.

        :param key: The possible key that moves the location.
        :return: If the key actually moves the item. (Not Equal = True)
        """
        # Make a new copy of the cube.
        temp_cube = CubeForCubie(
            cube_input="_" * self.cube_size,
            cube_side_length=self.side_length,
            track_location=self.track_item_location
        )
        # Perform the desired shift.
        temp_cube.shift(key=key)
        # Return True if the location is changed.
        return temp_cube.get_tracked_location() != self.track_item_location

    def get_effective_key(self) -> List[Key]:
        """Get all the keys that moves the tracked item with fixed 90 degrees.

        :return: A list of effective keys with fixed 90 degrees.
        """
        return [
            key for key in self.get_all_basic_key()
            if self.check_effective_key(key=key)
        ]

    def get_all_effective_key(self) -> List[Key]:
        """Get all the keys that moves the tracked item with any angles.

        :return: A list of effective keys with any degree.
        """
        return [
            key._replace(angle=angle)
            for key in self.get_effective_key()
            for angle in MOVE_ANGLE
        ]

    def get_location(self, key: Key) -> int:
        """Get location of the tracked item after performing a effective key.

        :param key: One known effective effective key.
        :return: New location of the tracked item.
        """
        # Make a new copy of the cube.
        temp_cube = CubeForCubie(
            cube_input="_" * self.cube_size,
            cube_side_length=self.side_length,
            track_location=self.track_item_location
        )
        # Perform the desired shift and shift the content.
        temp_cube.shift(key=key)
        temp_cube.shift_cubie_content()

        # Return the new location of the tracked item.
        return temp_cube.get_tracked_location()

    def get_all_location(self) -> List[int]:
        """Get all possible locations of the tracked item.

        :return: A list of possible locations of the tracked item.
        """
        return [(self.track_item_location + 1) % self.cube_size] + [
            self.get_location(key=key) for key in self.get_all_effective_key()
        ]
