"""Define contents and operations of the entire cube."""

import numpy as np
from cube_encryption.cube_face import CubeFace
from cube_encryption.constants import WRONG_CUBE_INPUT, CUBIE_LENGTH


class Cube:
    """Create a full cube with desired side length on inputs."""

    def __init__(self, cube_input: str, cube_side_length: int):
        """Initialize entire cube with a string of desired length.

        :param cube_input: The binary representation of the plain text.
        :param cube_side_length: The desired side length of the cube.
        """
        # Check length of the input.
        assert len(cube_input) == cube_side_length ** 2 * 6 * CUBIE_LENGTH, \
            WRONG_CUBE_INPUT

        # Save the cube side length and cube max index.
        self._side_length = cube_side_length
        self._cube_max_index = cube_side_length - 1

        # Split the cube input into six arrays.
        cube_input_list = np.array_split(
            ary=list(cube_input), indices_or_sections=6
        )

        # Assume that we fill the cube in the following order:
        #   - 1. Top face
        #   - 2. Front face
        #   - 3. Right face
        #   - 4. Back face
        #   - 5. Left face
        #   - 6. Down face
        self._top_face = CubeFace(
            cube_face_input=cube_input_list[0],
            cube_side_length=cube_side_length
        )
        self._front_face = CubeFace(
            cube_face_input=cube_input_list[1],
            cube_side_length=cube_side_length
        )
        self._right_face = CubeFace(
            cube_face_input=cube_input_list[2],
            cube_side_length=cube_side_length
        )
        self._back_face = CubeFace(
            cube_face_input=cube_input_list[3],
            cube_side_length=cube_side_length
        )
        self._left_face = CubeFace(
            cube_face_input=cube_input_list[4],
            cube_side_length=cube_side_length
        )
        self._down_face = CubeFace(
            cube_face_input=cube_input_list[5],
            cube_side_length=cube_side_length
        )

    @property
    def content(self) -> str:
        """Format all cubies into a continuous string.

        :return: A string contains all cubies.
        """
        # Get all cube faces as string in the right order.
        return \
            f"{self._top_face.face_string}" \
            f"{self._front_face.face_string}" \
            f"{self._right_face.face_string}" \
            f"{self._back_face.face_string}" \
            f"{self._left_face.face_string}" \
            f"{self._down_face.face_string}"

    def shift_cubie_content(self):
        """Shift the cube binary representation to right by one bit."""
        # Obtain the shifted content by padding the last bit to the first.
        shifted_binary_content = f"{self.content[-1]}" \
                                 f"{self.content[:-1]}"
        # Re-Init the class with new content.
        self.__init__(
            cube_input=shifted_binary_content,
            cube_side_length=self._side_length
        )

    def shift_cubie_content_back(self):
        """Shift the cube binary representation to left by one bit."""
        # Obtain the shifted content by padding the first bit to the last.
        shifted_content = f"{self.content[1:]}" \
                          f"{self.content[0]}"
        # Re-Init the class with new content.
        self.__init__(
            cube_input=shifted_content, cube_side_length=self._side_length
        )

    def _shift_in_x_y(self, row_index: int):
        """Shift the cube clockwise in x, y plane.

        :param row_index: The index of the shifting row.
        """
        # Rotate top face cubies if the most top layer selected.
        if row_index == 0:
            self._top_face.rotate_by_angle(angle=90)

        # Rotate down face cubies if the most down layer selected.
        if row_index == self._cube_max_index:
            self._down_face.rotate_by_angle(angle=90)

        # Save temp row.
        temp_row = self._left_face.get_row(row_index=row_index)

        # back -> right -> front -> left -> back
        self._left_face.fill_row(
            row_index=row_index,
            input_list=self._front_face.get_row(row_index=row_index)
        )
        self._front_face.fill_row(
            row_index=row_index,
            input_list=self._right_face.get_row(row_index=row_index)
        )
        self._right_face.fill_row(
            row_index=row_index,
            input_list=self._back_face.get_row(row_index=row_index)
        )
        self._back_face.fill_row(row_index=row_index, input_list=temp_row)

    def _shift_in_x_z(self, index: int):
        """Shift the cube clockwise in x, z plane.

        :param index: The index of the shifting column/row.
        """
        # Rotate back face cubies if the most back layer selected.
        if index == 0:
            self._back_face.rotate_by_angle(angle=90)

        # Rotate front face cubies if the most right layer selected.
        if index == self._cube_max_index:
            self._front_face.rotate_by_angle(angle=90)

        # Save temp column.
        temp_row = self._top_face.get_row(row_index=index)

        # top -> right -> down -> left -> top
        self._top_face.fill_row(
            row_index=index,
            input_list=self._left_face.get_col(col_index=index)
        )
        self._left_face.fill_col(
            col_index=index,
            input_list=self._down_face.get_row(
                row_index=self._cube_max_index - index
            )
        )
        self._down_face.fill_row(
            row_index=self._cube_max_index - index,
            input_list=self._right_face.get_col(
                col_index=self._cube_max_index - index
            )
        )
        self._right_face.fill_col(
            col_index=self._cube_max_index - index, input_list=temp_row
        )

    def _shift_in_y_z(self, col_index: int):
        """Shift the cube clockwise in y, z plane.

        :param col_index: The index of the shifting column.
        """
        # Rotate left face cubies if the most left layer selected.
        if col_index == 0:
            self._left_face.rotate_by_angle(angle=90)

        # Rotate right face cubies if the most right layer selected.
        if col_index == self._cube_max_index:
            self._right_face.rotate_by_angle(angle=90)

        # Save temp column.
        temp_col = self._front_face.get_col(col_index=col_index)

        # down -> back -> top -> front -> down
        self._front_face.fill_col(
            col_index=col_index,
            input_list=self._top_face.get_col(col_index=col_index)
        )
        self._top_face.fill_col(
            col_index=col_index,
            input_list=self._back_face.get_col(col_index=col_index)
        )
        self._back_face.fill_col(
            col_index=col_index,
            input_list=self._down_face.get_col(col_index=col_index)
        )
        self._down_face.fill_col(col_index=col_index, input_list=temp_col)

    # def shift(self, move: str, angle: int):
    #     """Shift the cube with a move in certain amount of angle.
    #
    #     :param move: The desired move the cube should shift.
    #     :param angle: The desired angle the cube should shift.
    #     """
    #     # Find number of movements.
    #     movements = int(angle / 90)
    #
    #     # Perform moves based on the inputs.
    #     if move == CubeMove.right.value:
    #         for __ in range(movements):
    #             self._shift_right()
    #
    #     elif move == CubeMove.left.value:
    #         for __ in range(movements):
    #             self._shift_left()
    #
    #     elif move == CubeMove.top.value:
    #         for __ in range(movements):
    #             self._shift_top()
    #
    #     elif move == CubeMove.bottom.value:
    #         for __ in range(movements):
    #             self._shift_bottom()
    #
    #     elif move == CubeMove.front.value:
    #         for __ in range(movements):
    #             self._shift_front()
    #
    #     elif move == CubeMove.back.value:
    #         for __ in range(movements):
    #             self._shift_back()
    #
    #     elif move == CubeMove.front_center_row.value:
    #         for __ in range(movements):
    #             self._shift_front_center_row()
    #
    #     elif move == CubeMove.top_center_row.value:
    #         for __ in range(movements):
    #             self._shift_top_center_row()
    #
    #     elif move == CubeMove.top_center_col.value:
    #         for __ in range(movements):
    #             self._shift_top_center_col()
    #
    #     # If the input movement was not defined.
    #     else:
    #         raise ValueError(WRONG_CUBE_MOVE)
    #
    # def get_cube_formatted(self) -> str:
    #     """Format the cube into a pretty displayable string.
    #
    #     :return: The formatted cube as a string.
    #     """
    #     # Format cube to a string.
    #     return \
    #         f"       {self.top_face.get_top_row_str()}\n" \
    #         f"       {self.top_face.get_central_row_str()}\n" \
    #         f"       {self.top_face.get_bottom_row_str()}\n" \
    #         f" - - -  - - -  - - -  - - -\n" \
    #         f"{self.left_face.get_top_row_str()}" \
    #         f"{self.front_face.get_top_row_str()}" \
    #         f"{self.right_face.get_top_row_str()}" \
    #         f"{self.back_face.get_top_row_str()}\n" \
    #         f"{self.left_face.get_central_row_str()}" \
    #         f"{self.front_face.get_central_row_str()}" \
    #         f"{self.right_face.get_central_row_str()}" \
    #         f"{self.back_face.get_central_row_str()}\n" \
    #         f"{self.left_face.get_bottom_row_str()}" \
    #         f"{self.front_face.get_bottom_row_str()}" \
    #         f"{self.right_face.get_bottom_row_str()}" \
    #         f"{self.back_face.get_bottom_row_str()}\n" \
    #         f" - - -  - - -  - - -  - - -\n" \
    #         f"       {self.bottom_face.get_top_row_str()}\n" \
    #         f"       {self.bottom_face.get_central_row_str()}\n" \
    #         f"       {self.bottom_face.get_bottom_row_str()}\n"
