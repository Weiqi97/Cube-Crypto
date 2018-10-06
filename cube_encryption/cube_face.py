"""Define contents and operations of a cube face."""

import numpy as np
from typing import List
from cube_encryption.cubie import Cubie
from cube_encryption.constants import CUBIE_LENGTH, WRONG_SIDE_LENGTH, \
    WRONG_CUBE_FACE_INPUT


class CubeFace:
    """Create a cube face with desired size on inputs."""

    def __init__(self, cube_face_input: str, cube_side_length):
        """Initialize one cube face.
        :param cube_face_input: The input needed to fill in the cube face.
        :param cube_side_length: The desired side length of the cube.
        """
        # Error check. The input length should be cube face size times 4.
        assert len(cube_face_input) == cube_side_length ** 2 * CUBIE_LENGTH, \
            WRONG_CUBE_FACE_INPUT

        # Save the cube side length.
        self._side_length = cube_side_length

        # Split the cube face input to chunks with length of 4.
        face_input_list = np.array_split(
            ary=list(cube_face_input),
            indices_or_sections=len(cube_face_input) / CUBIE_LENGTH
        )

        # Create a list of cubies.
        face_input_cubie_list = [
            Cubie(cubie_input=cubie_input) for cubie_input in face_input_list
        ]

        # Fill in the cube face matrix with the cubies.
        self._face_cubie_matrix = np.array(
            np.array_split(
                ary=face_input_cubie_list,
                indices_or_sections=cube_side_length
            )
        )

    @property
    def face_string(self) -> str:
        """Get the entire cube face as a concatenated string."""
        # Convert each cubie to its string format.
        cubie_strings = [
            cubie.get_content_string()
            for cubie in self._face_cubie_matrix.flat
        ]

        # Concatenate the list to a string.
        return "".join(cubie_strings)

    def get_row(self, row_index: int) -> List[Cubie]:
        """Get one row in the cube face by index as a list of cubies."""
        # Return a deep copy of the desired row.
        return self._face_cubie_matrix[row_index].copy()

    def fill_row(self, row_index: int, input_list: List[Cubie]):
        """Fill one row in the cube face by index with a list of cubies."""
        # Error check. The input length is the same as side length of the cube.
        assert len(input_list) == self._side_length, WRONG_SIDE_LENGTH
        self._face_cubie_matrix[row_index] = input_list

    def get_col(self, col_index: int) -> List[Cubie]:
        """Get one column in the cube face by index as a list of cubies."""
        # Return a deep copy of the desired row.
        return self._face_cubie_matrix[..., col_index].copy()

    def fill_col(self, col_index: int, input_list: List[Cubie]):
        """Fill one column in the cube face by index with a list of cubies."""
        # Error check. The input length is the same as side length of the cube.
        assert len(input_list) == self._side_length, WRONG_SIDE_LENGTH
        self._face_cubie_matrix[..., col_index] = input_list

    def get_row_str(self, row_index: int) -> str:
        """Get one row in the cube face by index as a string."""
        # Get the desired cube row.
        cubie_row = self.get_row(row_index=row_index)
        # Convert each cubie to its string format.
        cubie_str_row = [cubie.get_content_string() for cubie in cubie_row]
        # Concatenate the list to a string.
        return "".join(["|", "|".join(cubie_str_row), "|"])
