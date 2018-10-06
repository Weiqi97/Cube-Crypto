"""Define what each cube face can do."""
from typing import List

import numpy as np
from cube_encryption.constants import SIDE_LENGTH, WRONG_LENGTH, CUBIE_LENGTH
from cube_encryption.cubie import Cubie


class CubeFace:
    """Class contains method to get and fill row/col in a cube face."""

    def __init__(self, cube_face_input: str, cube_side_length):
        """Initialize one cube face with a string of desired length."""
        # Error check. The input length should be cube face size times 4.
        assert len(cube_face_input) == cube_side_length ** 2 * CUBIE_LENGTH, \
            WRONG_LENGTH

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

        # Get the length of all cubies.
        cubie_list_length = len(face_input_cubie_list)

        # Fill in the cube face matrix with the cubies.
        self._face_cubie_matrix = np.array(
            [face_input_cubie_list[index: index + cube_side_length]
             for index in range(0, cubie_list_length, cube_side_length)]
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
        """Get top row of the cube face.

        :return: A list of cubies.
        """
        return self._face_cubie_matrix[row_index].copy()

    def fill_row(self, row_index: int, input_list: List[Cubie]):
        """Fill top row with a input list."""
        assert len(input_list) == self._side_length, WRONG_LENGTH
        self._face_cubie_matrix[row_index] = input_list
    #
    # def get_bottom_row(self) -> list:
    #     """Get bottom row of the cube face.
    #
    #     :return: A list of cubies.
    #     """
    #     return self._face_matrix[2].copy()
    #
    # def fill_bottom_row(self, input_list: list):
    #     """Fill bottom row with a input list."""
    #     assert len(input_list) == SIDE_LENGTH, WRONG_LENGTH
    #     self._face_matrix[2] = input_list
    #
    # def get_right_col(self) -> list:
    #     """Get right col of the cube face.
    #
    #     :return: A list of cubies.
    #     """
    #     return self._face_matrix[..., 2].copy()
    #
    # def fill_right_col(self, input_list: list):
    #     """Fill right col with a input list."""
    #     assert len(input_list) == SIDE_LENGTH, WRONG_LENGTH
    #     self._face_matrix[..., 2] = input_list
    #
    # def get_left_col(self) -> list:
    #     """Get left col of the cube face.
    #
    #     :return: A list of cubies.
    #     """
    #     return self._face_matrix[..., 0].copy()
    #
    # def fill_left_col(self, input_list: list):
    #     """Fill left col with a input list."""
    #     assert len(input_list) == SIDE_LENGTH, WRONG_LENGTH
    #     self._face_matrix[..., 0] = input_list
    #
    # def get_central_row(self) -> list:
    #     """Get central row of the cube face.
    #
    #     :return: A list of cubies.
    #     """
    #     return self._face_matrix[1].copy()
    #
    # def fill_central_row(self, input_list: list):
    #     """Fill central row with a input list."""
    #     assert len(input_list) == SIDE_LENGTH, WRONG_LENGTH
    #     self._face_matrix[1] = input_list
    #
    # def get_central_col(self) -> list:
    #     """Get central col of the cube face.
    #
    #     :return: A list of cubies.
    #     """
    #     return self._face_matrix[..., 1].copy()
    #
    # def fill_central_col(self, input_list: list):
    #     """Fill central col with a input list."""
    #     assert len(input_list) == SIDE_LENGTH, WRONG_LENGTH
    #     self._face_matrix[..., 1] = input_list
    #
    # def get_top_row_str(self) -> str:
    #     """Get the top row as a formatted string."""
    #     return "".join(["|", "|".join(self.get_top_row()), "|"])
    #
    # def get_bottom_row_str(self) -> str:
    #     """Get the bottom row as a formatted string."""
    #     return "".join(["|", "|".join(self.get_bottom_row()), "|"])
    #
    # def get_central_row_str(self) -> str:
    #     """Get the central row as a formatted string."""
    #     return "".join(["|", "|".join(self.get_central_row()), "|"])
