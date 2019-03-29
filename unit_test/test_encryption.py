from content.helper.constants import Key
from content.encrypt_bit.encryption import Encryption


# noinspection PyProtectedMember
class TestEncryptionOneCube:
    # Set the test plain message.
    message = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwX"
    # Set the testing protocol.
    protocol = Encryption(message=message, cube_side_length=4)

    # Set the padded binary string.
    binary_chunk = [cube.content for cube in protocol._cubes]

    def test_init(self):
        # Check initialization.
        assert len(self.protocol._key) == 0
        assert len(self.protocol._cubes) == 2

    def test_current_string(self):
        assert self.protocol.get_current_binary() == "".join(self.binary_chunk)

    def test_encryption(self):
        self.protocol.encrypt(
            key=[
                Key(move="right", angle=360, index=1),
                Key(move="top", angle=360, index=1),
                Key(move="front", angle=360, index=1),
                Key(move="left", angle=360, index=1),
                Key(move="down", angle=360, index=1),
                Key(move="back", angle=360, index=1)
            ]
        )

        assert self.protocol.get_current_binary() == "".join(
            chunk[-6:] + chunk[:-6] for chunk in self.binary_chunk
        )

    def test_decrypt(self):
        self.protocol.encrypt(
            key=[
                Key(move="left", angle=90, index=1)
            ]
        )

        assert self.protocol.get_decrypted_str() == self.message
