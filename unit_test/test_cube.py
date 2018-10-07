import copy
from cube_encryption.cube import Cube
from cube_encryption.constants import CubeMove, WRONG_CUBE_MOVE, \
    WRONG_CUBE_INPUT, WRONG_CUBE_SIDE_LENGTH, Key


class TestCubeOperations:
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

    def test_gen_t_b_l_index(self):
        cube = Cube(cube_input="1" * 7 * 7 * 6 * 4, cube_side_length=7)
        index_set = set([cube._get_t_b_l_index() for _ in range(1000)])
        assert index_set == {0, 1, 2}

    def test_gen_d_f_r_index(self):
        cube = Cube(cube_input="1" * 7 * 7 * 6 * 4, cube_side_length=7)
        index_set = set([cube._get_d_f_r_index() for _ in range(1000)])
        assert index_set == {4, 5, 6}

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


class TestCubeShift:
    # Setup testing inputs.
    cube_input = \
        "101010101010101020202020202020203030303030303030" \
        "404040404040404050505050505050506060606060606060"

    def test_right_90(self):
        # Create the cube.
        cube = Cube(cube_input=self.cube_input, cube_side_length=2)
        cube.shift(Key(move=CubeMove.right.value, angle=90, index=1))
        assert cube.content == \
            "101020201010202020206060202060600303030303030303" \
            "404010104040101050505050505050506060404060604040"

    def test_left_90(self):
        # Create the cube.
        cube = Cube(cube_input=self.cube_input, cube_side_length=2)
        cube.shift(Key(move=CubeMove.left.value, angle=90, index=0))
        assert cube.content == \
            "404010104040101010102020101020203030303030303030" \
            "606040406060404005050505050505052020606020206060"

    def test_front_90(self):
        # Create the cube.
        cube = Cube(cube_input=self.cube_input, cube_side_length=2)
        cube.shift(Key(move=CubeMove.front.value, angle=90, index=1))
        assert cube.content == \
            "101010103030303002020202020202026060303060603030" \
            "404040404040404050501010505010105050505060606060"

    def test_back_90(self):
        # Create the cube.
        cube = Cube(cube_input=self.cube_input, cube_side_length=2)
        cube.shift(Key(move=CubeMove.back.value, angle=90, index=0))
        assert cube.content == \
            "505050501010101020202020202020203030101030301010" \
            "040404040404040460605050606050506060606030303030"

    def test_top_90(self):
        # Create the cube.
        cube = Cube(cube_input=self.cube_input, cube_side_length=2)
        cube.shift(Key(move=CubeMove.top.value, angle=90, index=0))
        assert cube.content == \
            "010101010101010130303030202020204040404030303030" \
            "505050504040404020202020505050506060606060606060"

    def test_down_90(self):
        # Create the cube.
        cube = Cube(cube_input=self.cube_input, cube_side_length=2)
        cube.shift(Key(move=CubeMove.down.value, angle=90, index=1))
        assert cube.content == \
            "101010101010101020202020505050503030303020202020" \
            "404040403030303050505050404040400606060606060606"

    def test_special(self):
        # Create the cube.
        cube = Cube(cube_input=self.cube_input, cube_side_length=2)
        try:
            cube.shift(Key(move="abracadabra", angle=90, index=0))
            raise AssertionError("Error message did not raise.")
        except ValueError as error:
            assert str(error) == WRONG_CUBE_MOVE


class TestCubeErrorCheck:
    def test_wrong_input_length(self):
        try:
            Cube(cube_input="abracadabra", cube_side_length=100)
            raise AssertionError("Error message did not raise.")
        except AssertionError as error:
            assert str(error) == WRONG_CUBE_INPUT

    def test_wrong_cube_side_length(self):
        try:
            Cube(cube_input="1" * 24, cube_side_length=1)
            raise AssertionError("Error message did not raise.")
        except AssertionError as error:
            assert str(error) == WRONG_CUBE_SIDE_LENGTH
