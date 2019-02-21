from content.encryption.encryption import Encryption
from content.helper.constants import MOVE_ANGLE, CUBE_MOVE, Key


class TestEncryptionOneCube:
    # Set the test plain message.
    message = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwX"

    # Set the testing protocol.
    protocol = Encryption(message=message, cube_side_length=4)

    # noinspection PyProtectedMember
    def test_init(self):
        # Check initialization.
        assert len(self.protocol._key) == 0
        assert len(self.protocol._cubes) == 1

    def test_pad_string(self):
        # See if the padding works correctly.
        assert self.protocol.get_pad_string() == \
            "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwX@"

    def test_un_pad_string(self):
        # See if the un-pad works correctly.
        assert self.protocol.get_un_pad_string() == self.message

    def test_encryption(self):
        self.protocol.encrypt(
            key=[
                Key(move="right", angle=360, index=1),
                Key(move="left", angle=360, index=1),
                Key(move="top", angle=360, index=1),
                Key(move="down", angle=360, index=1),
                Key(move="front", angle=360, index=1),
                Key(move="back", angle=360, index=1)
            ]
        )
        assert self.protocol.get_un_pad_string() == self.message

    def test_decrypt(self):
        self.protocol.encrypt(
            key=[
                Key(move="right", angle=90, index=1)
            ]
        )
        self.protocol.decrypt()
        assert self.protocol.get_un_pad_string() == self.message
