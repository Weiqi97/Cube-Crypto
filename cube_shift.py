"""Define what each cube face can do."""
import numpy as np
from constants import SIDE_LENGTH, WRONG_LENGTH


class CubeFace:
    """Class contains method to get and fill row/col in a cube face."""

    def __init__(self, face_input: str):
        """Initialize with a string of desired length."""
        # Check length of the input.
        assert len(face_input) == SIDE_LENGTH ^ 2, WRONG_LENGTH

        # Fill the cubies on a cube face.
        face_input_list = list(face_input)
        self.face_matrix = np.array(
            [face_input_list[index: index + SIDE_LENGTH]
             for index in range(0, len(face_input_list), SIDE_LENGTH)]
        )

    def get_face(self) -> np.ndarray:
        """Get the entire cube face as a 2D matrix.

        :return: A 2D matrix with all cubies.
        """
        return self.face_matrix

    def get_top_row(self) -> list:
        """Get top row of the cube face.

        :return: A list of cubies.
        """
        return self.face_matrix[0]

    def fill_top_row(self, input_list: list):
        """Fill top row with a input list."""
        assert len(input_list) == SIDE_LENGTH, WRONG_LENGTH
        self.face_matrix[0] = input_list

    def get_bottom_row(self) -> list:
        """Get bottom row of the cube face.

        :return: A list of cubies.
        """
        return self.face_matrix[2]

    def fill_bottom_row(self, input_list: list):
        """Fill bottom row with a input list."""
        assert len(input_list) == SIDE_LENGTH, WRONG_LENGTH
        self.face_matrix[2] = input_list

    def get_right_col(self) -> list:
        """Get right col of the cube face.

        :return: A list of cubies.
        """
        return self.face_matrix[..., 2]

    def fill_right_col(self, input_list: list):
        """Fill right col with a input list."""
        assert len(input_list) == SIDE_LENGTH, WRONG_LENGTH
        self.face_matrix[..., 2] = input_list

    def get_left_col(self) -> list:
        """Get left col of the cube face.

        :return: A list of cubies.
        """
        return self.face_matrix[..., 0]

    def fill_left_col(self, input_list: list):
        """Fill left col with a input list."""
        assert len(input_list) == SIDE_LENGTH, WRONG_LENGTH
        self.face_matrix[..., 0] = input_list

    def get_central_row(self) -> list:
        """Get central row of the cube face.

        :return: A list of cubies.
        """
        return self.face_matrix[1]

    def fill_central_row(self, input_list: list):
        """Fill central row with a input list."""
        assert len(input_list) == SIDE_LENGTH, WRONG_LENGTH
        self.face_matrix[1] = input_list

    def get_central_col(self) -> list:
        """Get central col of the cube face.

        :return: A list of cubies.
        """
        return self.face_matrix[..., 1]

    def fill_central_col(self, input_list: list):
        """Fill central col with a input list."""
        assert len(input_list) == SIDE_LENGTH, WRONG_LENGTH
        self.face_matrix[..., 1] = input_list
