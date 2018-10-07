from unittest.mock import patch, call
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

    # def test_key_gen(self):
    #     # Generate key and extract the only key.
    #     key = self.protocol.generate_random_key(length=1)[0]
    #     assert key.angle in MOVE_ANGLE
    #     assert key.move in CUBE_MOVE

    # def test_encryption(self):
    #     self.protocol.encrypt(
    #         key=[
    #             Key(move="right", angle=360), Key(move="left", angle=360),
    #             Key(move="top", angle=360), Key(move="down", angle=360),
    #             Key(move="front", angle=360), Key(move="back", angle=360)
    #         ]
    #     )
    #     assert self.protocol.get_un_pad_content() == self.message
    #
    # def test_decrypt(self):
    #     self.protocol.encrypt(
    #         key=[
    #             Key(move="right", angle=90), Key(move="left", angle=90),
    #             Key(move="top", angle=90), Key(move="down", angle=90),
    #             Key(move="front", angle=90), Key(move="back", angle=90)
    #         ]
    #     )
    #     self.protocol.decrypt()
    #     print("DONE")
    #     assert self.protocol.get_un_pad_content() == self.message
