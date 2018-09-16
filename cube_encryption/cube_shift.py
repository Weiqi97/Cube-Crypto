"""This file defines shifts of a cube."""
from cube_encryption.constants import SIDE_LENGTH, WRONG_LENGTH
from cube_encryption.cube_face import CubeFace


class CubeShift:
    def __init__(self, cube_input: str):
        """Initialize entire cube with a string of desired length."""
        # Check length of the input.
        assert len(cube_input) == SIDE_LENGTH ** 2 * 6, WRONG_LENGTH

        cube_input_list = [
            cube_input[index: index + SIDE_LENGTH ** 2]
            for index in range(0, len(cube_input), SIDE_LENGTH ** 2)
        ]

        # Assume that we fill the cube in the following order:
        #   - 1. Top face
        #   - 2. Front face
        #   - 3. Right face
        #   - 4. Back face
        #   - 5. Left face
        #   - 6. Bottom face
        self.top_face = CubeFace(cube_input_list[0])
        self.front_face = CubeFace(cube_input_list[1])
        self.right_face = CubeFace(cube_input_list[2])
        self.back_face = CubeFace(cube_input_list[3])
        self.left_face = CubeFace(cube_input_list[4])
        self.bottom_face = CubeFace(cube_input_list[5])

    def _shift_top(self):
        """Shift the top layer clockwise by 90 degrees."""
        temp_row = self.left_face.get_top_row()
        self.left_face.fill_top_row(self.front_face.get_top_row())
        self.front_face.fill_top_row(self.right_face.get_top_row())
        self.right_face.fill_top_row(self.back_face.get_top_row())
        self.back_face.fill_top_row(temp_row)

    def _shift_bottom(self):
        """Shift the bottom layer clockwise by 90 degrees."""
        temp_row = self.left_face.get_bottom_row()
        self.left_face.fill_bottom_row(self.back_face.get_bottom_row())
        self.back_face.fill_bottom_row(self.right_face.get_bottom_row())
        self.right_face.fill_bottom_row(self.front_face.get_bottom_row())
        self.front_face.fill_bottom_row(temp_row)

    def _shift_central_row(self):
        """Shift the central horizontal layer clockwise by 90 degrees."""
        # Assume this shift is in the same direction as top shift.
        temp_row = self.left_face.get_central_row()
        self.left_face.fill_central_row(self.front_face.get_central_row())
        self.front_face.fill_central_row(self.right_face.get_central_row())
        self.right_face.fill_central_row(self.back_face.get_central_row())
        self.back_face.fill_central_row(temp_row)

    def _shift_right(self):
        """Shift the right layer clockwise by 90 degrees."""
        temp_col = self.front_face.get_right_col()
        self.front_face.fill_right_col(self.bottom_face.get_right_col())
        self.bottom_face.fill_right_col(self.back_face.get_right_col())
        self.back_face.fill_right_col(self.top_face.get_right_col())
        self.top_face.fill_right_col(temp_col)

    def _shift_left(self):
        """Shift the left layer clockwise by 90 degrees."""
        temp_col = self.front_face.get_left_col()
        self.front_face.fill_left_col(self.top_face.get_left_col())
        self.top_face.fill_left_col(self.back_face.get_left_col())
        self.back_face.fill_left_col(self.bottom_face.get_left_col())
        self.bottom_face.fill_left_col(temp_col)

    def _shift_central_col(self):
        """Shift the central vertical layer clockwise by 90 degrees."""
        # Assume this shift is in the same direction as right shift.
        temp_col = self.front_face.get_central_col()
        self.front_face.fill_central_col(self.bottom_face.get_central_col())
        self.bottom_face.fill_central_col(self.back_face.get_central_col())
        self.back_face.fill_central_col(self.top_face.get_central_col())
        self.top_face.fill_central_col(temp_col)

