from content.helper.helper import xor, generate_random_keys, \
    binary_to_string, string_to_binary
from content.helper.constants import CUBE_MOVE, MOVE_ANGLE


class TestHelper:
    def test_key_gen(self):
        # Generate key and extract important information to test.
        keys = generate_random_keys(length=100, max_index=2)
        key_angle = [key.angle for key in keys]
        key_move = [key.move for key in keys]
        key_index = [key.index for key in keys]
        assert set(key_angle).issubset(MOVE_ANGLE)
        assert set(key_move).issubset(CUBE_MOVE)
        assert set(key_index).issubset([1, 2])

    def test_xor(self):
        # Test all possible combinations for XOR.
        str_one = "1001"
        str_two = "1100"
        assert xor(str_one=str_one, str_two=str_two) == "0101"

    def test_string_to_binary(self):
        assert string_to_binary(input_string="A") == "01000001"

    def test_binary_to_string(self):
        assert binary_to_string(input_binary="01000001") == "A"
