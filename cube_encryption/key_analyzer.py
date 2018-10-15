"""Defines the key length analyzer."""
from typing import List
from collections import namedtuple
from cube_encryption.constants import Key, CUBE_MOVE, COMMUTE_MOVE


class KeyAnalyzer:
    """Merge commute keys to check the effective length of the input key."""

    def __init__(self, key: List[Key]):
        """Initialize the analyzer with the key to be analyzing.

        :param key: A list of key object.
        """
        # Store the input list of keys to a class instance.
        self._key = key

    @staticmethod
    def _commute(move_one: CUBE_MOVE, move_two: CUBE_MOVE) -> bool:
        """Check if two keys commute.

        :param move_one: Name of the move.
        :param move_two: Name of the other move.
        :return: True if the two input moves commute, otherwise False.
        """
        # Two moves commute if they are the same.
        if move_one == move_two:
            return True
        # Check if the two different moves commute.
        elif {move_one, move_two} in COMMUTE_MOVE:
            return True
        # Otherwise, return False.
        else:
            return False

    def _get_commute_key_list(self) -> List[List[Key]]:
        """Split list of keys to list of lists of commute keys."""
        # Set the starting index to 0 and initialize the key index list.
        start_index = 0
        key_index_list = []

        # Define commute key index named tuple.
        commute_key_index = namedtuple("index", ("start_index", "end_index"))

        # While not at the end of the key list, keep checking.
        while start_index < len(self._key):
            # Let end index be the same as the start index.
            end_index = start_index
            # If current key and next key commute, increase end index by 1.
            while end_index + 1 < len(self._key) and \
                self._commute(move_one=self._key[end_index].move,
                              move_two=self._key[end_index + 1].move):
                end_index += 1
            # When the key stop commuting, store the start and end indexes.
            key_index_list.append(
                commute_key_index(start_index=start_index, end_index=end_index)
            )
            # Increase start index by 1.
            start_index = end_index + 1

        # Based on the start and end index, get list of lists of commute keys.
        commute_key_list = [
            self._key[key_index.start_index: key_index.end_index + 1]
            if key_index.start_index != key_index.end_index
            else [self._key[key_index.start_index]]
            for key_index in key_index_list
        ]

        return commute_key_list

    # def _merge_commute_keys(self):
    #     commute_key_list = self._get_commute_key_list()
    #     for commute_keys in commute_key_list:
    #
    #
    # def analyze(self):
    #     commutativity_list = [
    #         self._commutative(move_one=move_one, move_two=move_two)
    #         for move_one, move_two in zip(self._key[:-1], self._key[1:])
    #     ]
    #
    #     if True in commutativity_list:
