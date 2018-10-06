from collections import deque
from cube_encryption.cubie import Cubie
from cube_encryption.constants import WRONG_CUBIE_INPUT, WRONG_ROTATION_ANGLE


class TestCubie:
    cubie = Cubie(cubie_input=["1", "0", "1", "0"])

    def test_get_content(self):
        assert self.cubie.get_content() == deque("1010")

    def test_get_content_string(self):
        assert self.cubie.get_content_string() == "1010"

    def test_rotation(self):
        self.cubie.rotate_by_angle(angle=90)
        assert self.cubie.get_content_string() == "0101"


class TestCubieErrorCheck:
    def test_init(self):
        try:
            Cubie(cubie_input="abracadabra".split(""))
            raise AssertionError("Error message did not raise.")
        except AssertionError as error:
            assert str(error) == WRONG_CUBIE_INPUT

    def test_rotate(self):
        try:
            Cubie(cubie_input=["1", "0", "1", "0"]).rotate_by_angle(angle=123)
            raise AssertionError("Error message did not raise.")
        except AssertionError as error:
            assert str(error) == WRONG_ROTATION_ANGLE
