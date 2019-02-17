"""Define contents and operations of the entire cube."""

import numpy as np
from cube_encryption.cube_face_for_cubie import CubeFaceForCubie
from cube_encryption.constants import WRONG_CUBE_INPUT, CUBIE_LENGTH, \
    CubeMove, WRONG_CUBE_MOVE, WRONG_CUBE_SIDE_LENGTH, Key


class CubeForCubie:
    """Create a full cube with desired side length on inputs."""

    def __init__(self, cube_input: str, cube_side_length: int):
        """Initialize entire cube with a string of desired length.

        :param cube_input: The binary representation of the plain text.
        :param cube_side_length: The desired side length of the cube.
        """
        # Check length of the input.
        assert len(cube_input) == cube_side_length ** 2 * 6 * CUBIE_LENGTH, \
            WRONG_CUBE_INPUT
        assert cube_side_length > 1, WRONG_CUBE_SIDE_LENGTH

        # Save the cube side length and cube max index.
        self._side_length = cube_side_length
        self._cube_max_index = int(np.floor(cube_side_length / 2))

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
        self._top_face = CubeFaceForCubie(
            cube_face_input=cube_input_list[0],
            cube_side_length=cube_side_length
        )
        self._front_face = CubeFaceForCubie(
            cube_face_input=cube_input_list[1],
            cube_side_length=cube_side_length
        )
        self._right_face = CubeFaceForCubie(
            cube_face_input=cube_input_list[2],
            cube_side_length=cube_side_length
        )
        self._back_face = CubeFaceForCubie(
            cube_face_input=cube_input_list[3],
            cube_side_length=cube_side_length
        )
        self._left_face = CubeFaceForCubie(
            cube_face_input=cube_input_list[4],
            cube_side_length=cube_side_length
        )
        self._down_face = CubeFaceForCubie(
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
        shifted_content = f"{self.content[-1]}{self.content[:-1]}"

        # Re-Init the class with new content.
        self.__init__(
            cube_input=shifted_content, cube_side_length=self._side_length
        )

    def shift_cubie_content_back(self):
        """Shift the cube binary representation to left by one bit."""
        # Obtain the shifted content by padding the first bit to the last.
        shifted_content = f"{self.content[1:]}{self.content[0]}"

        # Re-Init the class with new content.
        self.__init__(
            cube_input=shifted_content, cube_side_length=self._side_length
        )

    def _shift_t(self, index: int):
        """Shift the top layer with the index clockwise by 90 degrees.

        :param index: The layer selected for the move.
        """
        # If the most outer layer was selected, rotate the corresponding face.
        if index == self._cube_max_index:
            self._top_face.rotate_by_angle(angle=90)

        # Save temp row.
        temp_row = self._left_face.get_row(row_name=f"T{index}").values

        # back -> right -> front -> left -> back
        self._left_face.fill_row(
            row_name=f"T{index}",
            input_list=self._front_face.get_row(row_name=f"T{index}").values
        )
        self._front_face.fill_row(
            row_name=f"T{index}",
            input_list=self._right_face.get_row(row_name=f"T{index}").values
        )
        self._right_face.fill_row(
            row_name=f"T{index}",
            input_list=self._back_face.get_row(row_name=f"T{index}").values
        )
        self._back_face.fill_row(row_name=f"T{index}", input_list=temp_row)

    def _shift_d(self, index: int):
        """Shift the down layer with the index clockwise by 90 degrees.

        :param index: The layer selected for the move.
        """
        # If the most outer layer was selected, rotate the corresponding face.
        if index == self._cube_max_index:
            self._down_face.rotate_by_angle(angle=90)

        # Save temp row.
        temp_row = self._left_face.get_row(row_name=f"D{index}").values

        # back -> left -> front -> right -> back
        self._left_face.fill_row(
            row_name=f"D{index}",
            input_list=self._back_face.get_row(row_name=f"D{index}").values
        )
        self._back_face.fill_row(
            row_name=f"D{index}",
            input_list=self._right_face.get_row(row_name=f"D{index}").values
        )
        self._right_face.fill_row(
            row_name=f"D{index}",
            input_list=self._front_face.get_row(row_name=f"D{index}").values
        )
        self._front_face.fill_row(row_name=f"D{index}", input_list=temp_row)

    def _shift_f(self, index: int):
        """Shift the front layer with the index clockwise by 90 degrees.

        :param index: The layer selected for the move.
        """
        # If the most outer layer was selected, rotate the corresponding face.
        if index == self._cube_max_index:
            self._front_face.rotate_by_angle(angle=90)

        # Save temp row.
        temp_row = self._top_face.get_row(row_name=f"D{index}").values

        # top -> right -> down -> left -> top
        self._top_face.fill_row(
            row_name=f"D{index}",
            input_list=[
                cubie.get_rotate_by_angle(angle=90)
                for cubie in
                self._left_face.get_col(col_name=f"R{index}").values
            ]
        )
        self._left_face.fill_col(
            col_name=f"R{index}",
            input_list=[
                cubie.get_rotate_by_angle(angle=90)
                for cubie in
                self._down_face.get_row(row_name=f"T{index}").values
            ]
        )
        self._down_face.fill_row(
            row_name=f"T{index}",
            input_list=[
                cubie.get_rotate_by_angle(angle=90)
                for cubie in
                self._right_face.get_col(col_name=f"L{index}").values
            ]
        )
        self._right_face.fill_col(
            col_name=f"L{index}",
            input_list=[
                cubie.get_rotate_by_angle(angle=90) for cubie in temp_row
            ]
        )

    def _shift_b(self, index: int):
        """Shift the back layer with the index clockwise by 90 degrees.

        :param index: The layer selected for the move.
        """
        # If the most outer layer was selected, rotate the corresponding face.
        if index == self._cube_max_index:
            self._back_face.rotate_by_angle(angle=90)

        # Save temp row.
        temp_row = self._top_face.get_row(row_name=f"T{index}").values

        # top -> left -> down -> right -> top
        self._top_face.fill_row(
            row_name=f"T{index}",
            input_list=[
                cubie.get_rotate_by_angle(angle=270)
                for cubie in
                self._right_face.get_col(col_name=f"L{index}").values
            ]
        )
        self._right_face.fill_col(
            col_name=f"L{index}",
            input_list=[
                cubie.get_rotate_by_angle(angle=270)
                for cubie in
                self._down_face.get_row(row_name=f"D{index}").values
            ]
        )
        self._down_face.fill_row(
            row_name=f"D{index}",
            input_list=[
                cubie.get_rotate_by_angle(angle=270)
                for cubie in
                self._left_face.get_col(col_name=f"R{index}").values
            ]
        )
        self._left_face.fill_col(
            col_name=f"R{index}",
            input_list=[
                cubie.get_rotate_by_angle(angle=270) for cubie in temp_row
            ]
        )

    def _shift_r(self, index: int):
        """Shift the right layer with the index clockwise by 90 degrees.

        :param index: The layer selected for the move.
        """
        # If the most outer layer was selected, rotate the corresponding face.
        if index == self._cube_max_index:
            self._right_face.rotate_by_angle(angle=90)

        # Save temp column.
        temp_col = self._front_face.get_col(col_name=f"R{index}").values

        # top -> back -> down -> front -> top
        self._front_face.fill_col(
            col_name=f"R{index}",
            input_list=[
                cubie
                for cubie in
                self._down_face.get_col(col_name=f"R{index}").values
            ]
        )
        self._down_face.fill_col(
            col_name=f"R{index}",
            input_list=[
                cubie.get_rotate_by_angle(angle=180)
                for cubie in
                self._back_face.get_col(col_name=f"R{index}").values
            ]
        )
        self._back_face.fill_col(
            col_name=f"R{index}",
            input_list=[
                cubie.get_rotate_by_angle(angle=180)
                for cubie in
                self._top_face.get_col(col_name=f"R{index}").values
            ]
        )
        self._top_face.fill_col(col_name=f"R{index}", input_list=temp_col)

    def _shift_l(self, index: int):
        """Shift the left layer with the index clockwise by 90 degrees.

        :param index: The layer selected for the move.
        """
        # If the most outer layer was selected, rotate the corresponding face.
        if index == self._cube_max_index:
            self._left_face.rotate_by_angle(angle=90)

        # Save temp column.
        temp_col = self._front_face.get_col(col_name=f"L{index}").values

        # top -> front -> down -> back -> top
        self._front_face.fill_col(
            col_name=f"L{index}",
            input_list=[
                cubie
                for cubie in
                self._top_face.get_col(col_name=f"L{index}").values
            ]
        )
        self._top_face.fill_col(
            col_name=f"L{index}",
            input_list=[
                cubie.get_rotate_by_angle(angle=180)
                for cubie in
                self._back_face.get_col(col_name=f"L{index}").values
            ]
        )
        self._back_face.fill_col(
            col_name=f"L{index}",
            input_list=[
                cubie.get_rotate_by_angle(angle=180)
                for cubie in
                self._down_face.get_col(col_name=f"L{index}").values
            ]
        )
        self._down_face.fill_col(col_name=f"L{index}", input_list=temp_col)

    def shift(self, key: Key):
        """Shift the cube with a move in certain amount of angle.

        :param key: A named tuple that holds information for one shift.
        """
        # Calculate the number of movements.
        number_of_movements = int(key.angle / 90)
        # Perform moves based on the inputs.
        if key.move == CubeMove.left.value:
            for _ in range(number_of_movements):
                self._shift_l(index=key.index)

        elif key.move == CubeMove.right.value:
            for _ in range(number_of_movements):
                self._shift_r(index=key.index)

        elif key.move == CubeMove.top.value:
            for _ in range(number_of_movements):
                self._shift_t(index=key.index)

        elif key.move == CubeMove.down.value:
            for _ in range(number_of_movements):
                self._shift_d(index=key.index)

        elif key.move == CubeMove.back.value:
            for _ in range(number_of_movements):
                self._shift_b(index=key.index)

        elif key.move == CubeMove.front.value:
            for _ in range(number_of_movements):
                self._shift_f(index=key.index)

        # If the input movement was not defined.
        else:
            raise ValueError(WRONG_CUBE_MOVE)
