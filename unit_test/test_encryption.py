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
        key = self.protocol.generate_random_key(length=1)[0]
        assert key.angle in MOVE_ANGLE
        assert key.move in CUBE_MOVE
        assert key.index < 4

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
