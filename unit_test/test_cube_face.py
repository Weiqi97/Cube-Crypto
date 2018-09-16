import numpy as np
from cube_shift import CubeFace


class TestCubeFace:
    cube_face = CubeFace("123456789")

    def test_cube_face(self):
        np.testing.assert_array_equal(
            self.cube_face.get_face(),
            [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        )

    def test_cube_top_row(self):
        np.testing.assert_array_equal(
            self.cube_face.get_top_row(),
            ["1", "2", "3"]
        )

    # def test_cube
