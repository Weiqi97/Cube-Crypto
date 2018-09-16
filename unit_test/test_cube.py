import numpy as np
from cube_encryption.cube import Cube


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
