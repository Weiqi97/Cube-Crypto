from typing import List
from cube_encryption.constants import Key, CUBE_MOVE, COMMUTE_MOVE


class KeyAnalyzer:
    def __init__(self, key: List[Key]):
        # Store the given key.
        self._key = key

    @staticmethod
    def _commutative(move_one: CUBE_MOVE, move_two: CUBE_MOVE) -> bool:
        if move_one == move_two:
            return True
        elif [move_one, move_two] in COMMUTE_MOVE:
            return True
        else:
            return False




