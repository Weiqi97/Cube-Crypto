"""Define contents and operations of the entire cube."""

import numpy as np
from cube_encryption.cube_face import CubeFace
from cube_encryption.constants import WRONG_CUBE_INPUT, CUBIE_LENGTH, \
    CubeMove, WRONG_CUBE_MOVE, WRONG_CUBE_SIDE_LENGTH


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
        assert cube_side_length > 1, WRONG_CUBE_SIDE_LENGTH

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

    def _get_t_b_l_index(self) -> int:
        """Get the index for movements: top, back and left."""
        # Find index upper bound. Note: for odd side, center is exclusive.
        upper_bound = np.ceil(self._cube_max_index / 2)
        # Return the random selected index.
        return np.random.randint(low=0, high=upper_bound)

    def _get_d_f_r_index(self) -> int:
        """Get the index for movements: down, front and right."""
        # Find index lower bound. Note: for odd side, center is exclusive.
        lower_bound = np.floor(self._cube_max_index / 2) + 1
        # Return the random selected index.
        return np.random.randint(low=lower_bound, high=self._side_length)

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
        """Shift the cube clockwise in x, y plane. (0 is top.)

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
        """Shift the cube clockwise in x, z plane. (0 is back.)

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
        """Shift the cube clockwise in y, z plane. (0 is left.)

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

    def _shift_in_x_y_by_num_movement(self, num_movement: int, row_index: int):
        """Shift the cube clockwise in x, y plane by number of movements.

        :param num_movement: The number of movements should be done.
        :param row_index: The index of the shifting row.
        """
        for _ in range(num_movement):
            self._shift_in_x_y(row_index=row_index)

    def _shift_in_x_z_by_num_movement(self, num_movement: int, index: int):
        """Shift the cube clockwise in x, y plane by number of movements.

        :param num_movement: The number of movements should be done.
        :param index: The index of the shifting row/column.
        """
        for _ in range(num_movement):
            self._shift_in_x_z(index=index)

    def _shift_in_y_z_by_num_movement(self, num_movement: int, col_index: int):
        """Shift the cube clockwise in x, y plane by number of movements.

        :param num_movement: The number of movements should be done.
        :param col_index: The index of the shifting column.
        """
        for _ in range(num_movement):
            self._shift_in_y_z(col_index=col_index)

    def shift(self, move: str, angle: int):
        """Shift the cube with a move in certain amount of angle.

        :param move: The desired move the cube should shift.
        :param angle: The desired angle the cube should shift.
        """
        # Perform moves based on the inputs.
        if move == CubeMove.left.value:
            self._shift_in_y_z_by_num_movement(
                num_movement=int(angle / 90),
                col_index=self._get_t_b_l_index()
            )
        elif move == CubeMove.right.value:
            self._shift_in_y_z_by_num_movement(
                num_movement=int((360 - angle) / 90),
                col_index=self._get_d_f_r_index()
            )
        elif move == CubeMove.top.value:
            self._shift_in_x_y_by_num_movement(
                num_movement=int(angle / 90),
                row_index=self._get_t_b_l_index()
            )

        elif move == CubeMove.down.value:
            self._shift_in_x_y_by_num_movement(
                num_movement=int((360 - angle) / 90),
                row_index=self._get_d_f_r_index()
            )

        elif move == CubeMove.back.value:
            self._shift_in_x_z_by_num_movement(
                num_movement=int(angle / 90),
                index=self._get_t_b_l_index()
            )

        elif move == CubeMove.front.value:
            self._shift_in_x_z_by_num_movement(
                num_movement=int((360 - angle) / 90),
                index=self._get_d_f_r_index()
            )

        # If the input movement was not defined.
        else:
            raise ValueError(WRONG_CUBE_MOVE)
