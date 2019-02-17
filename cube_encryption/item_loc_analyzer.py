import numpy as np
from cube_encryption.cube_for_item import CubeForItem
from cube_encryption.constants import WRONG_CUBE_SIDE_LENGTH


class ItemLocAnalyzer:
    def __init__(self, cube_side_length: int):
        assert cube_side_length > 1, WRONG_CUBE_SIDE_LENGTH
        self.cube = CubeForItem(
            cube_input=[
                num for num in range(1, cube_side_length ** 2 * 6 + 1)
            ],
            cube_side_length=cube_side_length
        )

        self._cube_max_index = int(np.floor(cube_side_length / 2))
