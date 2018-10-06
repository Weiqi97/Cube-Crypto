# from unittest.mock import patch, call
# from cube_encryption.encryption import Encryption
# from cube_encryption.constants import MOVE_ANGLE, CUBE_MOVE, Key
#
#
# class TestEncryption:
#     # Set the test plain message.
#     message = "111111111222222222333333333444444444555555555666666666"
#
#     # Set the testing protocol.
#     protocol = Encryption(
#         message=message
#     )
#
#     def test_init(self):
#         assert len(self.protocol._key) == 0
#         assert self.protocol._cube.get_cube_string() == self.message
#
#     def test_key_gen(self):
#         # Generate key and extract the only key.
#         key = self.protocol.generate_random_key(length=1)[0]
#         assert key.angle in MOVE_ANGLE
#         assert key.move in CUBE_MOVE
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
