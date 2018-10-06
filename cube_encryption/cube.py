"""Define contents and operations of the entire cube."""

import binascii
import numpy as np
from cube_encryption.constants import CubeMove, SIDE_LENGTH, WRONG_LENGTH, \
    WRONG_CUBE_MOVE, WRONG_CUBE_INPUT, CUBIE_LENGTH
from cube_encryption.cube_face import CubeFace


class Cube:
    """Create a full cube with desired side length on inputs."""

    def __init__(self, cube_input: str, cube_side_length: int):
        """Initialize entire cube with a string of desired length."""
        # Check length of the input.
        assert len(cube_input) == cube_side_length ** 2 * 3, WRONG_CUBE_INPUT

        # Save the cube side length.
        self._side_length = cube_side_length

        B = self.string_to_binary(input_string=cube_input)
        C = len(B)

        # Split the cube input into six arrays.
        cube_input_list = np.array_split(
            ary=list(self.string_to_binary(input_string=cube_input)),
            indices_or_sections=6
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

    @staticmethod
    def string_to_binary(input_string: str) -> str:
        string_to_byte = binascii.a2b_qp(input_string)
        byte_to_binary = bin(int.from_bytes(string_to_byte, byteorder="big"))
        return byte_to_binary.replace("b", "")

    @staticmethod
    def binary_to_string(input_binary: str) -> str:
        binary_to_byte = binascii.b2a_qp(input_binary)
        return binary_to_byte.decode("utf-8")

    @property
    def content_binary(self) -> str:
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

    @property
    def content_string(self) -> str:
        return self.binary_to_string(input_binary=self.content_binary)

    def shift_cubie_content(self):
        # Obtain the shifted content by padding the last bit to the first.
        shifted_content = f"{self.content_binary[-1]}" \
                          f"{self.content_binary[:-1]}"
        self.__init__(
            cube_input=shifted_content, cube_side_length=self._side_length
        )

    def shift_cubie_content_back(self):
        # Obtain the shifted content by padding the first bit to the last.
        shifted_content = f"{self.content_binary[1:]}" \
                          f"{self.content_binary[0]}"
        self.__init__(
            cube_input=shifted_content, cube_side_length=self._side_length
        )

    def _shift_in_x_y(self, row_index: int):
        """Shift the top layer clockwise by 90 degrees."""
        # Rotate top face cubies if the most top layer selected.
        if row_index == 0:
            self._top_face.rotate_by_angle(angle=90)

        # Rotate down face cubies if the most down layer selected.
        if row_index == self._side_length - 1:
            self._down_face.rotate_by_angle(angle=270)

        # back -> right -> front -> left -> back
        temp_row = self._left_face.get_row(row_index=row_index)
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

    # def _shift_bottom(self):
    #     """Shift the bottom layer clockwise by 90 degrees."""
    #     # front -> right -> back -> left -> front
    #        self._left_face.fill_bottom_row(self._back_face.get_bottom_row())
    #     self._back_face.fill_bottom_row(self._right_face.get_bottom_row())
    #     self._right_face.fill_bottom_row(self._front_face.get_bottom_row())
    #     self._front_face.fill_bottom_row(temp_row)
    #
    # def _shift_front_center_row(self):
    #     """Shift the central horizontal layer clockwise by 90 degrees."""
    #     # Assume this shift is in the same direction as top shift.
    #     temp_row = self._left_face.get_central_row()
    #     self._left_face.fill_central_row(self._front_face.get_central_row())
    #     self._front_face.fill_central_row(self._right_face.get_central_row())
    #     self._right_face.fill_central_row(self._back_face.get_central_row())
    #     self._back_face.fill_central_row(temp_row)
    #
    # def _shift_right(self):
    #     """Shift the right layer clockwise by 90 degrees."""
    #     # top -> back -> bottom -> front -> top
    #     temp_col = self._front_face.get_right_col()
    #     self._front_face.fill_right_col(self._bottom_face.get_right_col())
    #     self._bottom_face.fill_right_col(self._back_face.get_right_col())
    #     self._back_face.fill_right_col(self._top_face.get_right_col())
    #     self._top_face.fill_right_col(temp_col)
    #
    # def _shift_left(self):
    #     """Shift the left layer clockwise by 90 degrees."""
    #     # bottom -> back -> top -> front -> bottom
    #     temp_col = self._front_face.get_left_col()
    #     self._front_face.fill_left_col(self._top_face.get_left_col())
    #     self._top_face.fill_left_col(self._back_face.get_left_col())
    #     self._back_face.fill_left_col(self._bottom_face.get_left_col())
    #     self._bottom_face.fill_left_col(temp_col)
    #
    # def _shift_top_center_col(self):
    #     """Shift the central vertical layer clockwise by 90 degrees."""
    #     # Assume this shift is in the same direction as right shift.
    #     temp_col = self._front_face.get_central_col()
    #     self._front_face.fill_central_col(self._bottom_face.get_central_col())
    #     self._bottom_face.fill_central_col(self._back_face.get_central_col())
    #     self._back_face.fill_central_col(self._top_face.get_central_col())
    #     self._top_face.fill_central_col(temp_col)
    #
    # def _shift_front(self):
    #     """Shift the front layer clockwise by 90 degrees."""
    #     temp_col = self._top_face.get_bottom_row()
    #     self._top_face.fill_bottom_row(self._left_face.get_right_col())
    #     self._left_face.fill_right_col(self._bottom_face.get_top_row())
    #     self._bottom_face.fill_top_row(self._right_face.get_left_col())
    #     self._right_face.fill_left_col(temp_col)
    #
    # def _shift_back(self):
    #     """Shift the back layer clockwise by 90 degrees."""
    #     temp_col = self._top_face.get_top_row()
    #     self._top_face.fill_top_row(self._right_face.get_right_col())
    #     self._right_face.fill_right_col(self._bottom_face.get_bottom_row())
    #     self._bottom_face.fill_bottom_row(self._left_face.get_left_col())
    #     self._left_face.fill_left_col(temp_col)
    #
    # def _shift_top_center_row(self):
    #     """Shift the central horizontal layer clockwise by 90 degrees."""
    #     # Assume this shift is in the same direction as front shift.
    #     temp_col = self._top_face.get_central_row()
    #     self._top_face.fill_central_row(self._left_face.get_central_col())
    #     self._left_face.fill_central_col(self._bottom_face.get_central_row())
    #     self._bottom_face.fill_central_row(self._right_face.get_central_col())
    #     self._right_face.fill_central_col(temp_col)
    #
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


