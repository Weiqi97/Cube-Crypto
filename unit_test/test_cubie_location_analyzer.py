import numpy as np
from content.helper.constants import CUBE_MOVE, Key, MOVE_ANGLE
from content.analyzers.cubie_location_analyzer import CubieLocationAnalyzer


# noinspection PyProtectedMember
class TestCubieLocationAnalyzer:
    analyzer = CubieLocationAnalyzer(
        cube_side_length=3, track_item_location=0
    )

    def test_get_all_basic_key(self):
        assert self.analyzer._get_basic_key() == [
            Key(move=move, angle=90, index=1) for move in CUBE_MOVE
        ]

    def test_check_effective_key(self):
        assert self.analyzer._check_effective_key(
            key=Key(move="left", angle=90, index=1)
        )

    def test_get_effective_key(self):
        assert self.analyzer._get_effective_key() == [
            Key(move=move, angle=90, index=1)
            for move in ["left", "top", "back"]
        ]

    def test_get_all_effective_key(self):
        assert self.analyzer._get_all_effective_key() == [
            Key(move=move, angle=angle, index=1)
            for move in ["left", "top", "back"]
            for angle in MOVE_ANGLE
        ]

    def test_get_location(self):
        assert self.analyzer._get_location(
            key=Key(move="left", angle=90, index=1)) == 37

    def test_get_all_location(self):
        np.testing.assert_array_equal(
            self.analyzer.get_all_location(),
            [1, 37, 181, 143, 10, 35, 28, 172, 215, 82]
        )
