"""Define contents and operations of the entire cube."""

import numpy as np
from cube_encryption.cube_face_for_item import CubeFace
from cube_encryption.constants import Key, CubeMove, WRONG_CUBE_MOVE, \
    WRONG_CUBE_INPUT, WRONG_CUBE_SIDE_LENGTH


class Cube:
    """Create a full cube with desired side length on inputs."""

    def __init__(self, cube_input: list, cube_side_length: int):
        """Initialize entire cube with a string of desired length.

        :param cube_input: The binary representation of the plain text.
        :param cube_side_length: The desired side length of the cube.
        """
        # Check length of the input.
        assert len(cube_input) == cube_side_length ** 2 * 6, WRONG_CUBE_INPUT
        assert cube_side_length > 1, WRONG_CUBE_SIDE_LENGTH

        # Save the cube side length and cube max index.
        self._side_length = cube_side_length
        self._cube_max_index = int(np.floor(cube_side_length / 2))

        # Split the cube input into six arrays.
        cube_input_list = np.array_split(ary=cube_input, indices_or_sections=6)

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
    def content(self) -> list:
        """Put all face contents in to a list.

        :return: A list with all items in the correct order.
        """
        # Get all cube faces as string in the right order.
        return \
            self._top_face.get_item_list + \
            self._front_face.get_item_list + \
            self._right_face.get_item_list + \
            self._back_face.get_item_list + \
            self._left_face.get_item_list + \
            self._down_face.get_item_list

    def shift_cubie_content(self):
        """Shift the cube binary representation to right by one bit."""
        # Obtain the shifted content by padding the last bit to the first.
        shifted_content = self.content[-1] + self.content[:-1]
        # Re-Init the class with new content.
        self.__init__(
            cube_input=shifted_content, cube_side_length=self._side_length
        )

    def shift_cubie_content_back(self):
        """Shift the cube binary representation to left by one bit."""
        # Obtain the shifted content by padding the first bit to the last.
        shifted_content = self.content[1:] + self.content[0]
        # Re-Init the class with new content.
        self.__init__(
            cube_input=shifted_content, cube_side_length=self._side_length
        )

    def _shift_t(self, index: int):
        """Shift the top layer with the index clockwise by 90 degrees.

        :param index: The layer selected for the move.
        """
        # Save temp row.
        temp_row = self._left_face.get_row(row_name=f"T{index}")

        # back -> right -> front -> left -> back
        self._left_face.fill_row(
            row_name=f"T{index}",
            input_list=self._front_face.get_row(row_name=f"T{index}")
        )
        self._front_face.fill_row(
            row_name=f"T{index}",
            input_list=self._right_face.get_row(row_name=f"T{index}")
        )
        self._right_face.fill_row(
            row_name=f"T{index}",
            input_list=self._back_face.get_row(row_name=f"T{index}")
        )
        self._back_face.fill_row(row_name=f"T{index}", input_list=temp_row)

    def _shift_d(self, index: int):
        """Shift the down layer with the index clockwise by 90 degrees.

        :param index: The layer selected for the move.
        """
        # Save temp row.
        temp_row = self._left_face.get_row(row_name=f"D{index}")

        # back -> left -> front -> right -> back
        self._left_face.fill_row(
            row_name=f"D{index}",
            input_list=self._back_face.get_row(row_name=f"D{index}")
        )
        self._back_face.fill_row(
            row_name=f"D{index}",
            input_list=self._right_face.get_row(row_name=f"D{index}")
        )
        self._right_face.fill_row(
            row_name=f"D{index}",
            input_list=self._front_face.get_row(row_name=f"D{index}")
        )
        self._front_face.fill_row(row_name=f"D{index}", input_list=temp_row)

    def _shift_f(self, index: int):
        """Shift the front layer with the index clockwise by 90 degrees.

        :param index: The layer selected for the move.
        """
        # Save temp row.
        temp_row = list(self._top_face.get_row(row_name=f"D{index}"))

        # top -> right -> down -> left -> top
        self._top_face.fill_row(
            row_name=f"D{index}",
            input_list=list(self._left_face.get_col(col_name=f"R{index}"))
        )
        self._left_face.fill_col(
            col_name=f"R{index}",
            input_list=list(self._down_face.get_row(row_name=f"T{index}"))
        )
        self._down_face.fill_row(
            row_name=f"T{index}",
            input_list=list(self._right_face.get_col(col_name=f"L{index}"))
        )
        self._right_face.fill_col(col_name=f"L{index}", input_list=temp_row)

    def _shift_b(self, index: int):
        """Shift the back layer with the index clockwise by 90 degrees.

        :param index: The layer selected for the move.
        """
        # Save temp row.
        temp_row = list(self._top_face.get_row(row_name=f"T{index}"))

        # top -> left -> down -> right -> top
        self._top_face.fill_row(
            row_name=f"T{index}",
            input_list=list(self._right_face.get_col(col_name=f"L{index}"))
        )
        self._right_face.fill_col(
            col_name=f"L{index}",
            input_list=list(self._down_face.get_row(row_name=f"D{index}"))
        )
        self._down_face.fill_row(
            row_name=f"D{index}",
            input_list=list(self._left_face.get_col(col_name=f"R{index}"))
        )
        self._left_face.fill_col(col_name=f"R{index}", input_list=temp_row)

    def _shift_r(self, index: int):
        """Shift the right layer with the index clockwise by 90 degrees.

        :param index: The layer selected for the move.
        """
        # Save temp column.
        temp_col = self._front_face.get_col(col_name=f"R{index}")

        # top -> back -> down -> front -> top
        self._front_face.fill_col(
            col_name=f"R{index}",
            input_list=self._down_face.get_col(col_name=f"R{index}")
        )
        self._down_face.fill_col(
            col_name=f"R{index}",
            input_list=self._back_face.get_col(col_name=f"R{index}")
        )
        self._back_face.fill_col(
            col_name=f"R{index}",
            input_list=self._top_face.get_col(col_name=f"R{index}")
        )
        self._top_face.fill_col(col_name=f"R{index}", input_list=temp_col)

    def _shift_l(self, index: int):
        """Shift the left layer with the index clockwise by 90 degrees.

        :param index: The layer selected for the move.
        """
        # Save temp column.
        temp_col = self._front_face.get_col(col_name=f"L{index}")

        # top -> front -> down -> back -> top
        self._front_face.fill_col(
            col_name=f"L{index}",
            input_list=self._top_face.get_col(col_name=f"L{index}")
        )
        self._top_face.fill_col(
            col_name=f"L{index}",
            input_list=self._back_face.get_col(col_name=f"L{index}")
        )
        self._back_face.fill_col(
            col_name=f"L{index}",
            input_list=self._down_face.get_col(col_name=f"L{index}")
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
