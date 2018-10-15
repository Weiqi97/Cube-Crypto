from cube_encryption.constants import Key
from cube_encryption.key_analyzer import KeyAnalyzer


class TestKeyAnalyzer:
    # Set up the test key.
    key = [
        Key(move="right", angle=90, index=2),
        Key(move="left", angle=90, index=0),
        Key(move="right", angle=90, index=2),
        Key(move="top", angle=90, index=0),
        Key(move="right", angle=90, index=2),
        Key(move="down", angle=90, index=2),
        Key(move="top", angle=90, index=0),
        Key(move="left", angle=90, index=0),
        Key(move="front", angle=90, index=2),
        Key(move="back", angle=90, index=0),
        Key(move="front", angle=90, index=2),
        Key(move="right", angle=90, index=2),
        Key(move="right", angle=90, index=2)
    ]
    # Set up the key analyzer object.
    analyzer = KeyAnalyzer(key=key)

    def test_check_commute(self):
        assert self.analyzer._commute(move_one="left", move_two="left")
        assert self.analyzer._commute(move_one="right", move_two="left")
        assert not self.analyzer._commute(move_one="top", move_two="left")

    def test_get_commute_key_list(self):
        assert self.analyzer._get_commute_key_list() == [
            [
                Key(move="right", angle=90, index=2),
                Key(move="left", angle=90, index=0),
                Key(move="right", angle=90, index=2)
            ],
            [
                Key(move="top", angle=90, index=0)
            ],
            [
                Key(move="right", angle=90, index=2)
            ],
            [
                Key(move="down", angle=90, index=2),
                Key(move="top", angle=90, index=0)
            ],
            [
                Key(move="left", angle=90, index=0)
            ],
            [
                Key(move="front", angle=90, index=2),
                Key(move="back", angle=90, index=0),
                Key(move="front", angle=90, index=2)
            ],
            [
                Key(move="right", angle=90, index=2),
                Key(move="right", angle=90, index=2)
            ]
        ]
