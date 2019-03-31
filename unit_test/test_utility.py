import pandas as pd
import content.helper.utility as helper
from content.helper.constant import CUBE_MOVE, MOVE_ANGLE, Key


class TestHelper:
    def test_key_gen(self):
        # Generate key and extract important information to test.
        keys = helper.generate_random_keys(length=100, max_index=2)
        key_angle = [key.angle for key in keys]
        key_move = [key.move for key in keys]
        key_index = [key.index for key in keys]
        assert set(key_angle).issubset(MOVE_ANGLE)
        assert set(key_move).issubset(CUBE_MOVE)
        assert set(key_index).issubset([1, 2])

    def test_cube_layout(self):
        pd.testing.assert_frame_equal(
            helper.get_cube_layout(cube_side_length=2),
            pd.DataFrame(
                data=0, index=["T1", "D1"], columns=["L1", "R1"]
            )
        )

    def test_key_table(self):
        pd.testing.assert_frame_equal(
            helper.get_key_table(
                key=[
                    Key(move="right", index=1, angle=180),
                    Key(move="top", index=2, angle=90),
                    Key(move="back", index=1, angle=270),
                ]
            ),
            pd.DataFrame(
                data=[["right", 1, 180], ["top", 2, 90], ["back", 1, 270]],
                index=[1, 2, 3],
                columns=["Movement", "Index", "Angle"]
            )
        )

    def test_xor(self):
        # Test all possible combinations for XOR.
        str_one = "1001"
        str_two = "1100"
        assert helper.xor(str_one=str_one, str_two=str_two) == "0101"

    def test_string_to_binary(self):
        assert helper.string_to_binary(input_string="A") == "01000001"

    def test_binary_to_string(self):
        assert helper.binary_to_string(input_binary="01000001") == "A"

    def test_cube_frame_column(self):
        assert self.cube_face.get_frame_column(cube_side_length=4) == \
            deque(["L2", "L1", "R1", "R2"])
        assert self.cube_face.get_frame_column(cube_side_length=5) == \
            deque(["L2", "L1", "C", "R1", "R2"])

    def test_cube_frame_index(self):
        assert self.cube_face.get_frame_index(cube_side_length=4) == \
            deque(["T2", "T1", "D1", "D2"])
        assert self.cube_face.get_frame_index(cube_side_length=5) == \
            deque(["T2", "T1", "C", "D1", "D2"])
