import numpy as np
from cube_encryption.constants import WRONG_LENGTH
from cube_encryption.cube_face import CubeFace


class TestCubeFace:
    cube_face = CubeFace(face_input="123456789")

    def test_cube_face(self):
        np.testing.assert_array_equal(
            self.cube_face.get_face,
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

    def test_fill_cube_top_row(self):
        test_cube_face = CubeFace("123456789")
        test_cube_face.fill_top_row(["1", "1", "1"])
        np.testing.assert_array_equal(
            test_cube_face.get_top_row(),
            ["1", "1", "1"]
        )

        try:
            test_cube_face.fill_top_row([1])
            raise AssertionError("Wrong length error did not raise.")
        except AssertionError as error:
            assert str(error) == WRONG_LENGTH

    def test_fill_cube_bottom_row(self):
        test_cube_face = CubeFace(face_input="123456789")
        test_cube_face.fill_bottom_row(["1", "1", "1"])
        np.testing.assert_array_equal(
            test_cube_face.get_bottom_row(),
            ["1", "1", "1"]
        )

        try:
            test_cube_face.fill_bottom_row([1])
            raise AssertionError("Wrong length error did not raise.")
        except AssertionError as error:
            assert str(error) == WRONG_LENGTH

    def test_fill_cube_central_row(self):
        test_cube_face = CubeFace(face_input="123456789")
        test_cube_face.fill_central_row(["1", "1", "1"])
        np.testing.assert_array_equal(
            test_cube_face.get_central_row(),
            ["1", "1", "1"]
        )

        try:
            test_cube_face.fill_central_row([1])
            raise AssertionError("Wrong length error did not raise.")
        except AssertionError as error:
            assert str(error) == WRONG_LENGTH

    def test_fill_cube_right_col(self):
        test_cube_face = CubeFace(face_input="123456789")
        test_cube_face.fill_right_col(["1", "1", "1"])
        np.testing.assert_array_equal(
            test_cube_face.get_right_col(),
            ["1", "1", "1"]
        )

        try:
            test_cube_face.fill_right_col([1])
            raise AssertionError("Wrong length error did not raise.")
        except AssertionError as error:
            assert str(error) == WRONG_LENGTH

    def test_fill_cube_left_col(self):
        test_cube_face = CubeFace(face_input="123456789")
        test_cube_face.fill_left_col(["1", "1", "1"])
        np.testing.assert_array_equal(
            test_cube_face.get_left_col(),
            ["1", "1", "1"]
        )

        try:
            test_cube_face.fill_left_col([1])
            raise AssertionError("Wrong length error did not raise.")
        except AssertionError as error:
            assert str(error) == WRONG_LENGTH

    def test_fill_cube_central_col(self):
        test_cube_face = CubeFace(face_input="123456789")
        test_cube_face.fill_central_col(["1", "1", "1"])
        np.testing.assert_array_equal(
            test_cube_face.get_central_col(),
            ["1", "1", "1"]
        )

        try:
            test_cube_face.fill_central_col([1])
            raise AssertionError("Wrong length error did not raise.")
        except AssertionError as error:
            assert str(error) == WRONG_LENGTH


class TestCubeFaceClassError:
    try:
        _ = CubeFace(face_input="123")
        raise AssertionError("Wrong length error did not raise.")
    except AssertionError as error:
        assert str(error) == WRONG_LENGTH
