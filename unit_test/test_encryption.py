from cube_encryption.encryption import Encryption
from cube_encryption.constants import MOVE_ANGLE, CUBE_MOVE, Key


class TestEncryptionOneCube:
    # Set the test plain message.
    message = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwX"

    # Set the testing protocol.
    protocol = Encryption(message=message, cube_side_length=4)

    def test_init(self):
        # Check initialization.
        assert len(self.protocol._key) == 0
        assert len(self.protocol._cubes) == 1

    def test_pad_string(self):
        # See if the padding works correctly.
        assert self.protocol.get_pad_content() == \
            "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwX@"

    def test_un_pad_string(self):
        # See if the un-pad works correctly.
        assert self.protocol.get_un_pad_content() == self.message

    def test_gen_t_b_l_index(self):
        protocol = Encryption(message="1" * 7 * 7 * 3, cube_side_length=7)
        index_set = set([protocol._get_t_b_l_index() for _ in range(1000)])
        assert index_set == {0, 1, 2}

    def test_gen_d_f_r_index(self):
        protocol = Encryption(message="1" * 7 * 7 * 3, cube_side_length=7)
        index_set = set([protocol._get_d_f_r_index() for _ in range(1000)])
        assert index_set == {4, 5, 6}

    def test_key_gen(self):
        # Generate key and extract the only key.
        key_list = self.protocol.generate_random_key(length=100)
        key_angle = [key.angle for key in key_list]
        key_move = [key.move for key in key_list]
        key_index = [key.index for key in key_list]
        assert set(key_angle).issubset(MOVE_ANGLE)
        assert set(key_move).issubset(CUBE_MOVE)
        assert set(key_index).issubset([0, 1, 2, 3])

    def test_encryption(self):
        self.protocol.encrypt(
            key=[
                Key(move="right", angle=360, index=0),
                Key(move="left", angle=360, index=0),
                Key(move="top", angle=360, index=0),
                Key(move="down", angle=360, index=0),
                Key(move="front", angle=360, index=0),
                Key(move="back", angle=360, index=0)
            ]
        )
        assert self.protocol.get_un_pad_content() == self.message

    def test_decrypt(self):
        self.protocol.encrypt(
            key=[
                Key(move="right", angle=90, index=0)
            ]
        )
        self.protocol.decrypt()
        assert self.protocol.get_un_pad_content() == self.message
