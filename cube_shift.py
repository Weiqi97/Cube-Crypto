import numpy as np

# Global constants for length of the cube.
SIDE_LENGTH = 3


class CubeFace:
    def __init__(self, face_input: str):
        self.face_matrix = np.array(
            [face_input[index: index + SIDE_LENGTH]
             for index in range(0, len(face_input), SIDE_LENGTH)]
        )

    def get_face(self) -> np.ndarray:
        return self.face_matrix

    def get_top_row(self) -> list:
        return self.face_matrix[0]

    def fill_top_row(self, input_list: list):
        self.face_matrix[0] = input_list

    def get_bottom_row(self) -> list:
        return self.face_matrix[2]

    def fill_bottom_row(self, input_list: list):
        self.face_matrix[2] = input_list

    def get_right_col(self) -> list:
        return self.face_matrix[..., 2]

    def fill_right_col(self, input_list: list):
        self.face_matrix[..., 2] = input_list

    def get_left_col(self) -> list:
        return self.face_matrix[..., 0]

    def fill_left_col(self, input_list: list):
        self.face_matrix[..., 0] = input_list

    def get_central_row(self) -> list:
        return self.face_matrix[1]

    def fill_central_row(self, input_list: list):
        self.face_matrix[1] = input_list

    def get_central_col(self) -> list:
        return self.face_matrix[..., 1]

    def fill_central_col(self, input_list: list):
        self.face_matrix[..., 1] = input_list
