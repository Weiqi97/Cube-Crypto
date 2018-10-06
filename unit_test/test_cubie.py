from collections import deque
from cube_encryption.cubie import Cubie


class TestCubie:
    cubie = Cubie(cubie_input="1010")

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
            Cubie(cubie_input="abracadabra")
            raise AssertionError("Error message did not raise.")
        except AssertionError as error:
            assert str(error) == ""

