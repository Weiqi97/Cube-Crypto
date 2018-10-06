from collections import deque
from cube_encryption.cubie import Cubie


class TestCubie:
    cubie = Cubie("1010")

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

