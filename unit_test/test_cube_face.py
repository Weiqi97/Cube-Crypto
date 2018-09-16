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

    def test_cube_bottom_row(self):
        np.testing.assert_array_equal(
            self.cube_face.get_bottom_row(),
            ["7", "8", "9"]
        )

    def test_cube_right_col(self):
        np.testing.assert_array_equal(
            self.cube_face.get_right_col(),
            ["3", "6", "9"]
        )

    def test_cube_left_col(self):
        np.testing.assert_array_equal(
            self.cube_face.get_left_col(),
            ["1", "4", "7"]
        )

    def test_cube_central_row(self):
        np.testing.assert_array_equal(
            self.cube_face.get_central_row(),
            ["4", "5", "6"]
        )

    def test_cube_central_col(self):
        np.testing.assert_array_equal(
            self.cube_face.get_central_col(),
            ["2", "5", "8"]
        )
