"""This file defines shifts of a cube."""
from cube_encryption.constants import CubeMove, SIDE_LENGTH, WRONG_LENGTH, \
    WRONG_CUBE_MOVE
from cube_encryption.cube_face import CubeFace


class Cube:
    """Define all possible shift of a cube."""

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
        # back -> right -> front -> left -> back
        temp_row = self.left_face.get_top_row()
        self.left_face.fill_top_row(self.front_face.get_top_row())
        self.front_face.fill_top_row(self.right_face.get_top_row())
        self.right_face.fill_top_row(self.back_face.get_top_row())
        self.back_face.fill_top_row(temp_row)

    def _shift_bottom(self):
        """Shift the bottom layer clockwise by 90 degrees."""
        # front -> right -> back -> left -> front
        temp_row = self.left_face.get_bottom_row()
        self.left_face.fill_bottom_row(self.back_face.get_bottom_row())
        self.back_face.fill_bottom_row(self.right_face.get_bottom_row())
        self.right_face.fill_bottom_row(self.front_face.get_bottom_row())
        self.front_face.fill_bottom_row(temp_row)

    def _shift_front_center_row(self):
        """Shift the central horizontal layer clockwise by 90 degrees."""
        # Assume this shift is in the same direction as top shift.
        temp_row = self.left_face.get_central_row()
        self.left_face.fill_central_row(self.front_face.get_central_row())
        self.front_face.fill_central_row(self.right_face.get_central_row())
        self.right_face.fill_central_row(self.back_face.get_central_row())
        self.back_face.fill_central_row(temp_row)

    def _shift_right(self):
        """Shift the right layer clockwise by 90 degrees."""
        # top -> back -> bottom -> front -> top
        temp_col = self.front_face.get_right_col()
        self.front_face.fill_right_col(self.bottom_face.get_right_col())
        self.bottom_face.fill_right_col(self.back_face.get_right_col())
        self.back_face.fill_right_col(self.top_face.get_right_col())
        self.top_face.fill_right_col(temp_col)

    def _shift_left(self):
        """Shift the left layer clockwise by 90 degrees."""
        # bottom -> back -> top -> front -> bottom
        temp_col = self.front_face.get_left_col()
        self.front_face.fill_left_col(self.top_face.get_left_col())
        self.top_face.fill_left_col(self.back_face.get_left_col())
        self.back_face.fill_left_col(self.bottom_face.get_left_col())
        self.bottom_face.fill_left_col(temp_col)

    def _shift_top_center_col(self):
        """Shift the central vertical layer clockwise by 90 degrees."""
        # Assume this shift is in the same direction as right shift.
        temp_col = self.front_face.get_central_col()
        self.front_face.fill_central_col(self.bottom_face.get_central_col())
        self.bottom_face.fill_central_col(self.back_face.get_central_col())
        self.back_face.fill_central_col(self.top_face.get_central_col())
        self.top_face.fill_central_col(temp_col)

    def _shift_front(self):
        """Shift the front layer clockwise by 90 degrees."""
        temp_col = self.top_face.get_bottom_row()
        self.top_face.fill_bottom_row(self.left_face.get_right_col())
        self.left_face.fill_right_col(self.bottom_face.get_top_row())
        self.bottom_face.fill_top_row(self.right_face.get_left_col())
        self.right_face.fill_left_col(temp_col)

    def _shift_back(self):
        """Shift the back layer clockwise by 90 degrees."""
        temp_col = self.top_face.get_top_row()
        self.top_face.fill_top_row(self.right_face.get_right_col())
        self.right_face.fill_right_col(self.bottom_face.get_bottom_row())
        self.bottom_face.fill_bottom_row(self.left_face.get_left_col())
        self.left_face.fill_left_col(temp_col)

    def _shift_top_center_row(self):
        """Shift the central horizontal layer clockwise by 90 degrees."""
        # Assume this shift is in the same direction as front shift.
        temp_col = self.top_face.get_central_row()
        self.top_face.fill_central_row(self.left_face.get_central_col())
        self.left_face.fill_central_col(self.bottom_face.get_central_row())
        self.bottom_face.fill_central_row(self.right_face.get_central_col())
        self.right_face.fill_central_col(temp_col)

    def shift(self, move: str, angle: int):
        """Shift the cube with a move in certain amount of angle.

        :param move: The desired move the cube should shift.
        :param angle: The desired angle the cube should shift.
        """
        # Find number of movements.
        movements = int(angle / 90)

        # Perform moves based on the inputs.
        if move == CubeMove.right.value:
            for __ in range(movements):
                self._shift_right()

        elif move == CubeMove.left.value:
            for __ in range(movements):
                self._shift_left()

        elif move == CubeMove.top.value:
            for __ in range(movements):
                self._shift_top()

        elif move == CubeMove.bottom.value:
            for __ in range(movements):
                self._shift_bottom()

        elif move == CubeMove.front.value:
            for __ in range(movements):
                self._shift_front()

        elif move == CubeMove.back.value:
            for __ in range(movements):
                self._shift_back()

        elif move == CubeMove.front_center_row.value:
            for __ in range(movements):
                self._shift_front_center_row()

        elif move == CubeMove.top_center_row.value:
            for __ in range(movements):
                self._shift_top_center_row()

        elif move == CubeMove.top_center_col.value:
            for __ in range(movements):
                self._shift_top_center_col()

        # If the input movement was not defined.
        else:
            raise ValueError(WRONG_CUBE_MOVE)

    def print_cube(self):
        """Print formatted cube faces as string."""
        # Format cube to a string.
        formatted_cube_string = \
            f"       {self.top_face.get_top_row_str()}\n" \
            f"       {self.top_face.get_central_row_str()}\n" \
            f"       {self.top_face.get_bottom_row_str()}\n" \
            f" - - - - - - - - - - - - - - \n" \
            f"{self.left_face.get_top_row_str()}" \
            f"{self.front_face.get_top_row_str()}" \
            f"{self.right_face.get_top_row_str()}" \
            f"{self.back_face.get_top_row_str()}\n" \
            f"{self.left_face.get_central_row_str()}" \
            f"{self.front_face.get_central_row_str()}" \
            f"{self.right_face.get_central_row_str()}" \
            f"{self.back_face.get_central_row_str()}\n" \
            f"{self.left_face.get_bottom_row_str()}" \
            f"{self.front_face.get_bottom_row_str()}" \
            f"{self.right_face.get_bottom_row_str()}" \
            f"{self.back_face.get_bottom_row_str()}\n" \
            f" - - - - - - - - - - - - - - \n" \
            f"       {self.bottom_face.get_top_row_str()}\n" \
            f"       {self.bottom_face.get_central_row_str()}\n" \
            f"       {self.bottom_face.get_bottom_row_str()}\n"
        # Print the string.
        print(formatted_cube_string)

    def get_cube_string(self):
        """Get the cubies in the same order as they were filled in."""
        # Get all cube faces as string in the right order.
        cube_string = \
            f"{self.top_face.get_face_str}" \
            f"{self.front_face.get_face_str}" \
            f"{self.right_face.get_face_str}" \
            f"{self.back_face.get_face_str}" \
            f"{self.left_face.get_face_str}" \
            f"{self.bottom_face.get_face_str}"
        # Print the string.
        print(cube_string)
