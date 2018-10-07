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

    def test_normal_x_y_shift(self):
        # This is the case for a normal x - y rotate. (4 by 4 by 4 cube)
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

    def test_back_shift(self):
        # This is the case where the back face rotate. (4 by 4 by 4 cube)
        cube = Cube(cube_input=self.cube_input, cube_side_length=4)
        cube._shift_in_x_z(index=0)
        assert cube.content == "50505050505050501010101010101010" \
                               "10101010101010101010101010101010" \
                               "20202020202020202020202020202020" \
                               "20202020202020202020202020202020" \
                               "30303030303010103030303030301010" \
                               "30303030303010103030303030301010" \
                               "04040404040404040404040404040404" \
                               "04040404040404040404040404040404" \
                               "60605050505050506060505050505050" \
                               "60605050505050506060505050505050" \
                               "60606060606060606060606060606060" \
                               "60606060606060603030303030303030"

    def test_normal_x_z_shift(self):
        # This is the case for a normal y - z rotate. (4 by 4 by 4 cube)
        cube = Cube(cube_input=self.cube_input, cube_side_length=4)
        cube._shift_in_x_z(index=1)
        assert cube.content == "10101010101010105050505050505050" \
                               "10101010101010101010101010101010" \
                               "20202020202020202020202020202020" \
                               "20202020202020202020202020202020" \
                               "30303030101030303030303010103030" \
                               "30303030101030303030303010103030" \
                               "40404040404040404040404040404040" \
                               "40404040404040404040404040404040" \
                               "50506060505050505050606050505050" \
                               "50506060505050505050606050505050" \
                               "60606060606060606060606060606060" \
                               "30303030303030306060606060606060"

    def test_left_shift(self):
        # This is the case where the left face rotate. (4 by 4 by 4 cube)
        cube = Cube(cube_input=self.cube_input, cube_side_length=4)
        cube._shift_in_y_z(col_index=0)
        assert cube.content == "40401010101010104040101010101010" \
                               "40401010101010104040101010101010" \
                               "10102020202020201010202020202020" \
                               "10102020202020201010202020202020" \
                               "30303030303030303030303030303030" \
                               "30303030303030303030303030303030" \
                               "60604040404040406060404040404040" \
                               "60604040404040406060404040404040" \
                               "05050505050505050505050505050505" \
                               "05050505050505050505050505050505" \
                               "20206060606060602020606060606060" \
                               "20206060606060602020606060606060"

    def test_normal_y_z_shift(self):
        # This is the case for a normal y - z rotate. (4 by 4 by 4 cube)
        cube = Cube(cube_input=self.cube_input, cube_side_length=4)
        cube._shift_in_y_z(col_index=1)
        assert cube.content == "10104040101010101010404010101010" \
                               "10104040101010101010404010101010" \
                               "20201010202020202020101020202020" \
                               "20201010202020202020101020202020" \
                               "30303030303030303030303030303030" \
                               "30303030303030303030303030303030" \
                               "40406060404040404040606040404040" \
                               "40406060404040404040606040404040" \
                               "50505050505050505050505050505050" \
                               "50505050505050505050505050505050" \
                               "60602020606060606060202060606060" \
                               "60602020606060606060202060606060"

    def test_x_y_shift_by_movement(self):
        cube = Cube(cube_input=self.cube_input, cube_side_length=4)
        cube._shift_in_x_y_by_num_movement(num_movement=4, row_index=0)
        assert cube.content == self.cube_input

    def test_x_z_shift_by_movement(self):
        cube = Cube(cube_input=self.cube_input, cube_side_length=4)
        cube._shift_in_x_z_by_num_movement(num_movement=4, index=0)
        assert cube.content == self.cube_input

    def test_y_z_shift_by_movement(self):
        cube = Cube(cube_input=self.cube_input, cube_side_length=4)
        cube._shift_in_y_z_by_num_movement(num_movement=4, col_index=0)
        assert cube.content == self.cube_input

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
