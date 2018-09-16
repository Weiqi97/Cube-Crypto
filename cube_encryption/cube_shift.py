# Define shift for a cube.
from cube_encryption.constants import SIDE_LENGTH, WRONG_LENGTH


class CubeShift:
    def __init__(self, cube_input: str):
        """Initialize entire cube with a string of desired length."""
        # Check length of the input.
        assert len(cube_input) == SIDE_LENGTH ** 2 * 6, WRONG_LENGTH

        cube_input_list = [
            cube_input[index: index + SIDE_LENGTH ** 2]
            for index in range(0, len(cube_input), SIDE_LENGTH ** 2)
        ]

        # Assume that we fill the cube in the following order:
        #   - 1. Top face
        #   - 2. Front face
        #   - 3. Right face
        #   - 4. Back face
        #   - 5. Left face
        #   - 6. Bottom face
        self.top_face = cube_input_list[0]
        self.front_face = cube_input_list[1]
        self.right_face = cube_input_list[2]
        self.back_face = cube_input_list[3]
        self.left_face = cube_input_list[4]
        self.bottom_face = cube_input_list[5]
