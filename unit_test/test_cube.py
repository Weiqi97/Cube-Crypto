import copy
from cube_encryption.cube import Cube


class TestCube:
    # Setup testing inputs.
    cube_input = \
        "1010101010101010101010101010101010101010101010101010101010101010" \
        "2020202020202020202020202020202020202020202020202020202020202020" \
        "3030303030303030303030303030303030303030303030303030303030303030" \
        "4040404040404040404040404040404040404040404040404040404040404040" \
        "5050505050505050505050505050505050505050505050505050505050505050" \
        "6060606060606060606060606060606060606060606060606060606060606060"

    # Create the cube.
    cube = Cube(
        cube_input=copy.deepcopy(cube_input),
        cube_side_length=4
    )

    def test_cube_content(self):
        assert self.cube.content == self.cube_input

    def test_cube_shift_cubie_content(self):
        self.cube.shift_cubie_content()
        assert self.cube.content == f"{self.cube_input[-1]}" \
                                    f"{self.cube_input[: -1]}"

    def test_cube_shift_cubie_content_back(self):
        self.cube.shift_cubie_content_back()
        assert self.cube.content == self.cube_input

    def test_top_shift(self):
        # This is the case where the top face rotate. (4 by 4 by 4 cube)
        cube = Cube(cube_input=self.cube_input, cube_side_length=4)
        cube._shift_in_x_y(row_index=0)
        assert cube.content == "01010101010101010101010101010101" \
                               "01010101010101010101010101010101" \
                               "30303030303030302020202020202020" \
                               "20202020202020202020202020202020" \
                               "40404040404040403030303030303030" \
                               "30303030303030303030303030303030" \
                               "50505050505050504040404040404040" \
                               "40404040404040404040404040404040" \
                               "20202020202020205050505050505050" \
                               "50505050505050505050505050505050" \
                               "60606060606060606060606060606060" \
                               "60606060606060606060606060606060"

    def test_down_shift(self):
        # This is the case where the top face rotate. (4 by 4 by 4 cube)
        cube = Cube(cube_input=self.cube_input, cube_side_length=4)
        cube._shift_in_x_y(row_index=4 - 1)
        assert cube.content == "10101010101010101010101010101010" \
                               "10101010101010101010101010101010" \
                               "20202020202020202020202020202020" \
                               "20202020202020203030303030303030" \
                               "30303030303030303030303030303030" \
                               "30303030303030304040404040404040" \
                               "40404040404040404040404040404040" \
                               "40404040404040405050505050505050" \
                               "50505050505050505050505050505050" \
                               "50505050505050502020202020202020" \
                               "06060606060606060606060606060606" \
                               "06060606060606060606060606060606"

    def test_normal_x_y_shift(self):
        # This is the case where the top face rotate. (4 by 4 by 4 cube)
        cube = Cube(cube_input=self.cube_input, cube_side_length=4)
        cube._shift_in_x_y(row_index=1)
        assert cube.content == "10101010101010101010101010101010" \
                               "10101010101010101010101010101010" \
                               "20202020202020203030303030303030" \
                               "20202020202020202020202020202020" \
                               "30303030303030304040404040404040" \
                               "30303030303030303030303030303030" \
                               "40404040404040405050505050505050" \
                               "40404040404040404040404040404040" \
                               "50505050505050502020202020202020" \
                               "50505050505050505050505050505050" \
                               "60606060606060606060606060606060" \
                               "60606060606060606060606060606060"

#     def test_right_shift(self):
#         cube = Cube(cube_input=self.CUBE_INPUT)
#         cube.shift(move="right", angle=90)
#         np.testing.assert_array_equal(
#             cube.top_face.get_right_col(),
#             ["2", "2", "2"]
#         )
#
#     def test_left_shift(self):
#         cube = Cube(cube_input=self.CUBE_INPUT)
#         cube.shift(move="left", angle=90)
#         np.testing.assert_array_equal(
#             cube.top_face.get_left_col(),
#             ["4", "4", "4"]
#         )
#
#     def test_top_shift(self):
#         cube = Cube(cube_input=self.CUBE_INPUT)
#         cube.shift(move="top", angle=180)
#         np.testing.assert_array_equal(
#             cube.front_face.get_top_row(),
#             ["4", "4", "4"]
#         )
#
#     def test_bottom_shift(self):
#         cube = Cube(cube_input=self.CUBE_INPUT)
#         cube.shift(move="bottom", angle=180)
#         np.testing.assert_array_equal(
#             cube.front_face.get_bottom_row(),
#             ["4", "4", "4"]
#         )
#
#     def test_front_shift(self):
#         cube = Cube(cube_input=self.CUBE_INPUT)
#         cube.shift(move="front", angle=270)
#         np.testing.assert_array_equal(
#             cube.top_face.get_bottom_row(),
#             ["3", "3", "3"]
#         )
#
#     def test_back_shift(self):
#         cube = Cube(cube_input=self.CUBE_INPUT)
#         cube.shift(move="back", angle=270)
#         np.testing.assert_array_equal(
#             cube.top_face.get_top_row(),
#             ["5", "5", "5"]
#         )
#
#     def test_top_center_row_shift(self):
#         cube = Cube(cube_input=self.CUBE_INPUT)
#         cube.shift(move="top_center_row", angle=90)
#         np.testing.assert_array_equal(
#             cube.left_face.get_top_row(),
#             ["5", "6", "5"]
#         )
#
#     def test_top_center_col_shift(self):
#         cube = Cube(cube_input=self.CUBE_INPUT)
#         cube.shift(move="top_center_col", angle=90)
#         np.testing.assert_array_equal(
#             cube.front_face.get_top_row(),
#             ["2", "6", "2"]
#         )
#
#     def test_front_center_row_shift(self):
#         cube = Cube(cube_input=self.CUBE_INPUT)
#         cube.shift(move="front_center_row", angle=90)
#         np.testing.assert_array_equal(
#             cube.front_face.get_central_row(),
#             ["3", "3", "3"]
#         )
#
#     def test_print_cube(self):
#         cube = Cube(cube_input=self.CUBE_INPUT)
#         assert cube.get_cube_string() == self.CUBE_INPUT
#
#     def test_cube_string(self):
#         cube = Cube(cube_input=self.CUBE_INPUT)
#
#         assert cube.get_cube_formatted() == \
#             "       |1|1|1|\n" \
#             "       |1|1|1|\n" \
#             "       |1|1|1|\n" \
#             " - - -  - - -  - - -  - - -\n" \
#             "|5|5|5||2|2|2||3|3|3||4|4|4|\n" \
#             "|5|5|5||2|2|2||3|3|3||4|4|4|\n" \
#             "|5|5|5||2|2|2||3|3|3||4|4|4|\n" \
#             " - - -  - - -  - - -  - - -\n" \
#             "       |6|6|6|\n" \
#             "       |6|6|6|\n" \
#             "       |6|6|6|\n"
#
#     def test_invalid_length(self):
#         try:
#             Cube(cube_input="magic")
#             raise AssertionError("Error message did not raise.")
#         except AssertionError as error:
#             assert str(error) == WRONG_LENGTH
#
#     def test_invalid_move(self):
#         try:
#             cube = Cube(cube_input=self.CUBE_INPUT)
#             cube.shift(move="magic", angle=90)
#             raise AssertionError("Error message did not raise.")
#         except ValueError as error:
#             assert str(error) == WRONG_CUBE_MOVE
