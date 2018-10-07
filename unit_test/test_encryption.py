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

    def test_key_gen(self):
        # Generate key and extract the only key.
        key = self.protocol.generate_random_key(length=1)[0]
        assert key.angle in MOVE_ANGLE
        assert key.move in CUBE_MOVE
#
#     @patch("builtins.print")
#     def test_encryption(self, print_output):
#         self.protocol.encrypt(key=[Key(move="right", angle=90)])
#         self.protocol.print_message()
#         assert print_output.mock_calls == [
#             call("112112112226226226333333333441441441555555555664664664")
#         ]
#
#     @patch("builtins.print")
#     def test_decryption(self, print_output):
#         self.protocol.decrypt()
#         self.protocol.print_message()
#         assert print_output.mock_calls == [
#             call(self.message)
#         ]
#
#     @patch("builtins.print")
#     def test_print_formatted_cube(self, print_output):
#         self.protocol.print_formatted_cube()
#         assert print_output.mock_calls == [
#             call(
#                 "       |1|1|1|\n"
#                 "       |1|1|1|\n"
#                 "       |1|1|1|\n"
#                 " - - -  - - -  - - -  - - -\n"
#                 "|5|5|5||2|2|2||3|3|3||4|4|4|\n"
#                 "|5|5|5||2|2|2||3|3|3||4|4|4|\n"
#                 "|5|5|5||2|2|2||3|3|3||4|4|4|\n"
#                 " - - -  - - -  - - -  - - -\n"
#                 "       |6|6|6|\n"
#                 "       |6|6|6|\n"
#                 "       |6|6|6|\n"
#             )
#         ]
