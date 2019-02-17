import copy
from content.encryption.cube_for_cubie import CubeForCubie
from content.encryption.constants import CubeMove, WRONG_CUBE_MOVE, \
    WRONG_CUBE_INPUT, WRONG_CUBE_SIDE_LENGTH, Key


# noinspection PyProtectedMember
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
    cube = CubeForCubie(
        cube_input=copy.deepcopy(cube_input),
        cube_side_length=4,
        track_location=10
    )

    def test_cube_content(self):
        assert self.cube.content == self.cube_input

    def test_cube_location_tracker(self):
        assert self.cube.get_tracked_location() == 10

    def test_cube_shift_cubie_content(self):
        self.cube.shift_cubie_content()
        assert self.cube.content == f"{self.cube_input[-1]}" \
                                    f"{self.cube_input[: -1]}"

    def test_cube_shift_cubie_content_back(self):
        self.cube.shift_cubie_content_back()
        assert self.cube.content == self.cube_input

    def test_top_shift(self):
        # This is the case where the top face rotate. (4 by 4 by 4 cube)
        cube = CubeForCubie(cube_input=self.cube_input, cube_side_length=4)
        cube._shift_t(index=2)
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
        # This is the case where the down face rotate. (4 by 4 by 4 cube)
        cube = CubeForCubie(cube_input=self.cube_input, cube_side_length=4)
        cube._shift_d(index=2)
        assert cube.content == "10101010101010101010101010101010" \
                               "10101010101010101010101010101010" \
                               "20202020202020202020202020202020" \
                               "20202020202020205050505050505050" \
                               "30303030303030303030303030303030" \
                               "30303030303030302020202020202020" \
                               "40404040404040404040404040404040" \
                               "40404040404040403030303030303030" \
                               "50505050505050505050505050505050" \
                               "50505050505050504040404040404040" \
                               "06060606060606060606060606060606" \
                               "06060606060606060606060606060606"

    def test_right_shift(self):
        # This is the case where the right face rotate. (4 by 4 by 4 cube)
        cube = CubeForCubie(cube_input=self.cube_input, cube_side_length=4)
        cube._shift_r(index=2)
        assert cube.content == "10101010101020201010101010102020" \
                               "10101010101020201010101010102020" \
                               "20202020202060602020202020206060" \
                               "20202020202060602020202020206060" \
                               "03030303030303030303030303030303" \
                               "03030303030303030303030303030303" \
                               "10104040404040401010404040404040" \
                               "10104040404040401010404040404040" \
                               "50505050505050505050505050505050" \
                               "50505050505050505050505050505050" \
                               "60606060606040406060606060604040" \
                               "60606060606040406060606060604040"

    def test_left_shift(self):
        # This is the case where the left face rotate. (4 by 4 by 4 cube)
        cube = CubeForCubie(cube_input=self.cube_input, cube_side_length=4)
        cube._shift_l(index=2)
        assert cube.content == "40401010101010104040101010101010" \
                               "40401010101010104040101010101010" \
                               "10102020202020201010202020202020" \
                               "10102020202020201010202020202020" \
                               "30303030303030303030303030303030" \
                               "30303030303030303030303030303030" \
                               "40404040404060604040404040406060" \
                               "40404040404060604040404040406060" \
                               "05050505050505050505050505050505" \
                               "05050505050505050505050505050505" \
                               "20206060606060602020606060606060" \
                               "20206060606060602020606060606060"

    def test_front_shift(self):
        # This is the case where the front face rotate. (4 by 4 by 4 cube)
        cube = CubeForCubie(cube_input=self.cube_input, cube_side_length=4)
        cube._shift_f(index=2)
        assert cube.content == "10101010101010101010101010101010" \
                               "10101010101010100505050505050505" \
                               "02020202020202020202020202020202" \
                               "02020202020202020202020202020202" \
                               "01013030303030300101303030303030" \
                               "01013030303030300101303030303030" \
                               "40404040404040404040404040404040" \
                               "40404040404040404040404040404040" \
                               "50505050505006065050505050500606" \
                               "50505050505006065050505050500606" \
                               "03030303030303036060606060606060" \
                               "60606060606060606060606060606060"

    def test_back_shift(self):
        # This is the case where the back face rotate. (4 by 4 by 4 cube)
        cube = CubeForCubie(cube_input=self.cube_input, cube_side_length=4)
        cube._shift_b(index=2)
        assert cube.content == "03030303030303031010101010101010" \
                               "10101010101010101010101010101010" \
                               "20202020202020202020202020202020" \
                               "20202020202020202020202020202020" \
                               "30303030303006063030303030300606" \
                               "30303030303006063030303030300606" \
                               "04040404040404040404040404040404" \
                               "04040404040404040404040404040404" \
                               "01015050505050500101505050505050" \
                               "01015050505050500101505050505050" \
                               "60606060606060606060606060606060" \
                               "60606060606060600505050505050505"

    def test_middle_shift(self):
        # This is the case where the back face rotate. (4 by 4 by 4 cube)
        cube = CubeForCubie(cube_input=self.cube_input, cube_side_length=4)
        cube._shift_r(index=1)
        assert cube.content == "10101010202010101010101020201010" \
                               "10101010202010101010101020201010" \
                               "20202020606020202020202060602020" \
                               "20202020606020202020202060602020" \
                               "30303030303030303030303030303030" \
                               "30303030303030303030303030303030" \
                               "40401010404040404040101040404040" \
                               "40401010404040404040101040404040" \
                               "50505050505050505050505050505050" \
                               "50505050505050505050505050505050" \
                               "60606060404060606060606040406060" \
                               "60606060404060606060606040406060"


class TestCubeShift:
    # Setup testing inputs.
    cube_input = \
        "123456789012345678901234567890123456789012345678" \
        "123456789012345678901234567890123456789012345678"

    def test_right_90(self):
        # Create the cube.
        cube = CubeForCubie(cube_input=self.cube_input, cube_side_length=2)
        cube.shift(Key(move=CubeMove.right.value, angle=90, index=1))
        assert cube.content == \
            "123412349012901278907890567856784123634585670789" \
            "563456787856345678901234567890123456129012343412"

    def test_left_90(self):
        # Create the cube.
        cube = CubeForCubie(cube_input=self.cube_input, cube_side_length=2)
        cube.shift(Key(move=CubeMove.left.value, angle=90, index=1))
        assert cube.content == \
            "563456787856345612341234901290123456789012345678" \
            "123434129012563485670789290141237890789056785678"

    def test_front_90(self):
        # Create the cube.
        cube = CubeForCubie(cube_input=self.cube_input, cube_side_length=2)
        cube.shift(Key(move=CubeMove.front.value, angle=90, index=1))
        assert cube.content == \
            "123456782901412385670789290141232901789063455678" \
            "123456789012345678906345567807894123634512345678"

    def test_back_90(self):
        # Create the cube.
        cube = CubeForCubie(cube_input=self.cube_input, cube_side_length=2)
        cube.shift(Key(move=CubeMove.back.value, angle=90, index=1))
        assert cube.content == \
            "890767859012345678901234567890123456678512342341" \
            "290141236345856767851234234190123456789089076785"

    def test_top_90(self):
        # Create the cube.
        cube = CubeForCubie(cube_input=self.cube_input, cube_side_length=2)
        cube.shift(Key(move=CubeMove.top.value, angle=90, index=1))
        assert cube.content == \
            "290141236345856734567890567890121234567812345678" \
            "789012349012345678901234567890123456789012345678"

    def test_down_90(self):
        # Create the cube.
        cube = CubeForCubie(cube_input=self.cube_input, cube_side_length=2)
        cube.shift(Key(move=CubeMove.down.value, angle=90, index=1))
        assert cube.content == \
            "123456789012345678901234567890123456789056789012" \
            "123456781234567878901234901234564123634585670789"

    def test_special(self):
        # Create the cube.
        cube = CubeForCubie(cube_input=self.cube_input, cube_side_length=2)
        try:
            cube.shift(Key(move="abracadabra", angle=90, index=0))
            raise AssertionError("Error message did not raise.")
        except ValueError as error:
            assert str(error) == WRONG_CUBE_MOVE


class TestCubeErrorCheck:
    def test_wrong_input_length(self):
        try:
            CubeForCubie(cube_input="abracadabra", cube_side_length=100)
            raise AssertionError("Error message did not raise.")
        except AssertionError as error:
            assert str(error) == WRONG_CUBE_INPUT

    def test_wrong_cube_side_length(self):
        try:
            CubeForCubie(cube_input="1" * 24, cube_side_length=1)
            raise AssertionError("Error message did not raise.")
        except AssertionError as error:
            assert str(error) == WRONG_CUBE_SIDE_LENGTH
