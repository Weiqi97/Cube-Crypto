import numpy as np
from unittest.mock import patch, call
from cube_encryption.cube import Cube
from cube_encryption.constants import WRONG_CUBE_MOVE, WRONG_LENGTH


class TestCubeShift:
    # Define the testing input for the cube.
    CUBE_INPUT = "111111111222222222333333333444444444555555555666666666"

    def test_right_shift(self):
        cube = Cube(cube_input=self.CUBE_INPUT)
        cube.shift(move="right", angle=90)
        np.testing.assert_array_equal(
            cube.top_face.get_right_col(),
            ["2", "2", "2"]
        )

    def test_left_shift(self):
        cube = Cube(cube_input=self.CUBE_INPUT)
        cube.shift(move="left", angle=90)
        np.testing.assert_array_equal(
            cube.top_face.get_left_col(),
            ["4", "4", "4"]
        )

    def test_top_shift(self):
        cube = Cube(cube_input=self.CUBE_INPUT)
        cube.shift(move="top", angle=180)
        np.testing.assert_array_equal(
            cube.front_face.get_top_row(),
            ["4", "4", "4"]
        )

    def test_bottom_shift(self):
        cube = Cube(cube_input=self.CUBE_INPUT)
        cube.shift(move="bottom", angle=180)
        np.testing.assert_array_equal(
            cube.front_face.get_bottom_row(),
            ["4", "4", "4"]
        )

    def test_front_shift(self):
        cube = Cube(cube_input=self.CUBE_INPUT)
        cube.shift(move="front", angle=270)
        np.testing.assert_array_equal(
            cube.top_face.get_bottom_row(),
            ["3", "3", "3"]
        )

    def test_back_shift(self):
        cube = Cube(cube_input=self.CUBE_INPUT)
        cube.shift(move="back", angle=270)
        np.testing.assert_array_equal(
            cube.top_face.get_top_row(),
            ["5", "5", "5"]
        )

    def test_top_center_row_shift(self):
        cube = Cube(cube_input=self.CUBE_INPUT)
        cube.shift(move="top_center_row", angle=90)
        np.testing.assert_array_equal(
            cube.left_face.get_top_row(),
            ["5", "6", "5"]
        )

    def test_top_center_col_shift(self):
        cube = Cube(cube_input=self.CUBE_INPUT)
        cube.shift(move="top_center_col", angle=90)
        np.testing.assert_array_equal(
            cube.front_face.get_top_row(),
            ["2", "6", "2"]
        )

    def test_front_center_row_shift(self):
        cube = Cube(cube_input=self.CUBE_INPUT)
        cube.shift(move="front_center_row", angle=90)
        np.testing.assert_array_equal(
            cube.front_face.get_central_row(),
            ["3", "3", "3"]
        )

    def test_invalid_length(self):
        try:
            Cube(cube_input="magic")
            raise AssertionError("Error message did not raise.")
        except AssertionError as error:
            assert str(error) == WRONG_LENGTH

    def test_invalid_move(self):
        try:
            cube = Cube(cube_input=self.CUBE_INPUT)
            cube.shift(move="magic", angle=90)
            raise AssertionError("Error message did not raise.")
        except ValueError as error:
            assert str(error) == WRONG_CUBE_MOVE

    @patch("builtins.print")
    def test_print_cube(self, print_output):
        cube = Cube(cube_input=self.CUBE_INPUT)
        cube.print_cube()
        assert print_output.mock_calls == [
            call("       |1|1|1|\n       |1|1|1|\n       |1|1|1|\n "
                 "- - - - - - - - - - - - - - \n"
                 "|5|5|5||2|2|2||3|3|3||4|4|4|\n"
                 "|5|5|5||2|2|2||3|3|3||4|4|4|\n"
                 "|5|5|5||2|2|2||3|3|3||4|4|4|\n "
                 "- - - - - - - - - - - - - - \n       "
                 "|6|6|6|\n       |6|6|6|\n       |6|6|6|\n")
        ]
