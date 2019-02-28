"""Define contents and operations of one cube face that contains items."""

import numpy as np
import pandas as pd
from collections import deque
from content.helper.constants import WRONG_SIDE_LENGTH, \
    WRONG_CUBE_FACE_INPUT, WRONG_FRAME_INDEX_NAME, WRONG_FRAME_COLUMN_NAME


class CubeFaceForItem:
    """Create a cube face with desired side length on inputs."""

    def __init__(self, cube_face_input: list, cube_side_length):
        """Initialize one cube face.

        :param cube_face_input: The input needed to fill in the cube face.
        :param cube_side_length: The desired side length of the cube.
        """
        # Error check. The input length should be side length squared.
        assert len(cube_face_input) == cube_side_length ** 2, \
            WRONG_CUBE_FACE_INPUT

        # Save the cube side length.
        self._side_length = cube_side_length

        # Fill in the cube face matrix with the cubies.
        self._face_item_frame = pd.DataFrame(
            data=np.array_split(
                ary=cube_face_input,
                indices_or_sections=cube_side_length
            ),
            index=self.get_frame_index(cube_side_length=cube_side_length),
            columns=self.get_frame_column(cube_side_length=cube_side_length)
        )

    @property
    def get_item_list(self) -> list:
        """Get the entire cube face as a list."""
        # Concatenate the list to a string.
        return list(self._face_item_frame.values.flat)

    @staticmethod
    def get_frame_column(cube_side_length: int) -> deque:
        """Get column names for the cube face data frame.

        :param cube_side_length: The desired side length of the cube.
        :return: A deque object with the column names.
        """
        # If side length is even, start with empty queue.
        if cube_side_length % 2 == 0:
            column_queue = deque()
            # Pad R on the right side and L on the left side.
            for move_index in range(1, int(cube_side_length / 2) + 1):
                column_queue.appendleft(f"L{move_index}")
                column_queue.append(f"R{move_index}")

        # If side length is odd, start the queue with a "C" at the center.
        else:
            column_queue = deque("C")
            # Pad R on the right side and L on the left side.
            for move_index in range(1, int(np.ceil(cube_side_length / 2))):
                column_queue.appendleft(f"L{move_index}")
                column_queue.append(f"R{move_index}")

        return column_queue

    @staticmethod
    def get_frame_index(cube_side_length: int) -> deque:
        """Get index names for the cube face data frame.

        :param cube_side_length: The desired side length of the cube.
        :return: A deque object with the index names.
        """
        # If side length is even, start with empty queue.
        if cube_side_length % 2 == 0:
            index_queue = deque()
            # Pad D on the right side and T on the left side.
            for move_index in range(1, int(cube_side_length / 2) + 1):
                index_queue.appendleft(f"T{move_index}")
                index_queue.append(f"D{move_index}")

        # If side length is odd, start the queue with a "C" at the center.
        else:
            index_queue = deque("C")
            # Pad D on the right side and T on the left side.
            for move_index in range(1, int(np.ceil(cube_side_length / 2))):
                index_queue.appendleft(f"T{move_index}")
                index_queue.append(f"D{move_index}")

        return index_queue

    def get_row(self, row_name: str) -> pd.Series:
        """Get one row in the cube face by index as a list."""
        # Return a deep copy of the desired row.
        return self._face_item_frame.loc[row_name].copy()

    def fill_row(self, row_name: str, input_list: list):
        """Fill one row in the cube face by index with a list."""
        # Error check. The input length is the same as side length of the cube.
        assert len(input_list) == self._side_length, WRONG_SIDE_LENGTH
        # Error check. The index is not out of the list.
        assert row_name in self._face_item_frame.index, WRONG_FRAME_INDEX_NAME
        # Fill the desired row.
        self._face_item_frame.loc[row_name] = input_list

    def get_col(self, col_name: str) -> pd.Series:
        """Get one column in the cube face by index as a list."""
        # Return a deep copy of the desired row.
        return self._face_item_frame[col_name].copy()

    def fill_col(self, col_name: str, input_list: list):
        """Fill one column in the cube face by index with a list."""
        # Error check. The input length is the same as side length of the cube.
        assert len(input_list) == self._side_length, WRONG_SIDE_LENGTH
        # Error check. The index is not out of the list.
        assert col_name in self._face_item_frame.columns, \
            WRONG_FRAME_COLUMN_NAME
        # Fill the desired column.
        self._face_item_frame[col_name] = input_list

    def rotate_by_angle(self, angle: int):
        """Rotate the cube face by the desired angle."""
        # Rotate the face itself.
        self._face_item_frame.update(
            pd.DataFrame(
                data=np.rot90(
                    self._face_item_frame.values, int(4 - angle / 90)
                ),
                index=self._face_item_frame.index,
                columns=self._face_item_frame.columns
            )
        )
