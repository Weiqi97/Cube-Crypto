from cube_encryption.cubie import Cubie
from cube_encryption.cube_face import CubeFace


class TestCubeFace:
    # Setup testing input.
    face_input = "000100100101101010101010101010101010"
    cube_face = CubeFace(cube_face_input=face_input, cube_side_length=3)
    A = cube_face.get_col(col_index=0)
    print("DONE")

    def test_cube_face(self):
        assert self.cube_face.face_string == self.face_input

    def test_cube_row(self):
        # Get rows and check if they contain desired value.
        row_0 = self.cube_face.get_row(row_index=0)
        row_1 = self.cube_face.get_row(row_index=1)
        assert row_0[0].get_content_string() == "0001"
        assert row_1[1].get_content_string() == "1010"

    def test_cube_fill_row(self):
        # Create new testing cube face since the value get changed.
        cube_face = CubeFace(
            cube_face_input=self.face_input,
            cube_side_length=3
        )
        cube_face.fill_row(
            row_index=1,
            input_list=[
                Cubie(list("1111")),
                Cubie(list("1111")),
                Cubie(list("1111"))
            ]
        )
        # Get rows and check if they contain desired value.
        row_0 = cube_face.get_row(row_index=0)
        row_1 = cube_face.get_row(row_index=1)
        assert row_0[0].get_content_string() == "0001"
        assert row_1[1].get_content_string() == "1111"

    def test_cube_col(self):
        # Get cols and check if they contain desired value.
        col_0 = self.cube_face.get_col(col_index=0)
        col_1 = self.cube_face.get_col(col_index=1)
        assert col_0[0].get_content_string() == "0001"
        assert col_1[0].get_content_string() == "0010"

    def test_cube_fill_col(self):
        # Create new testing cube face since the value get changed.
        cube_face = CubeFace(
            cube_face_input=self.face_input,
            cube_side_length=3
        )
        cube_face.fill_col(
            col_index=1,
            input_list=[
                Cubie(list("1111")),
                Cubie(list("1111")),
                Cubie(list("1111"))
            ]
        )
        # Get cols and check if they contain desired value.
        col_0 = cube_face.get_col(col_index=0)
        col_1 = cube_face.get_col(col_index=1)
        assert col_0[0].get_content_string() == "0001"
        assert col_1[0].get_content_string() == "1111"


#     def test_cube_face_string(self):
#         assert self.cube_face.get_face_str == "123456789"
#
#     def test_cube_top_row(self):
#         np.testing.assert_array_equal(
#             self.cube_face.get_top_row(),
#             ["1", "2", "3"]
#         )
#
#     def test_cube_bottom_row(self):
#         np.testing.assert_array_equal(
#             self.cube_face.get_bottom_row(),
#             ["7", "8", "9"]
#         )
#
#     def test_cube_right_col(self):
#         np.testing.assert_array_equal(
#             self.cube_face.get_right_col(),
#             ["3", "6", "9"]
#         )
#
#     def test_cube_left_col(self):
#         np.testing.assert_array_equal(
#             self.cube_face.get_left_col(),
#             ["1", "4", "7"]
#         )
#
#     def test_cube_central_row(self):
#         np.testing.assert_array_equal(
#             self.cube_face.get_central_row(),
#             ["4", "5", "6"]
#         )
#
#     def test_cube_central_col(self):
#         np.testing.assert_array_equal(
#             self.cube_face.get_central_col(),
#             ["2", "5", "8"]
#         )
#
#     def test_cube_top_row_str(self):
#         assert self.cube_face.get_top_row_str() == "|1|2|3|"
#
#     def test_cube_bottom_row_str(self):
#         assert self.cube_face.get_bottom_row_str() == "|7|8|9|"
#
#     def test_cube_central_row_str(self):
#         assert self.cube_face.get_central_row_str() == "|4|5|6|"
#
#     def test_fill_cube_top_row(self):
#         test_cube_face = CubeFace("123456789")
#         test_cube_face.fill_top_row(["1", "1", "1"])
#         np.testing.assert_array_equal(
#             test_cube_face.get_top_row(),
#             ["1", "1", "1"]
#         )
#
#         try:
#             test_cube_face.fill_top_row([1])
#             raise AssertionError("Error message did not raise.")
#         except AssertionError as error:
#             assert str(error) == WRONG_LENGTH
#
#     def test_fill_cube_bottom_row(self):
#         test_cube_face = CubeFace(face_input="123456789")
#         test_cube_face.fill_bottom_row(["1", "1", "1"])
#         np.testing.assert_array_equal(
#             test_cube_face.get_bottom_row(),
#             ["1", "1", "1"]
#         )
#
#         try:
#             test_cube_face.fill_bottom_row([1])
#             raise AssertionError("Error message did not raise.")
#         except AssertionError as error:
#             assert str(error) == WRONG_LENGTH
#
#     def test_fill_cube_central_row(self):
#         test_cube_face = CubeFace(face_input="123456789")
#         test_cube_face.fill_central_row(["1", "1", "1"])
#         np.testing.assert_array_equal(
#             test_cube_face.get_central_row(),
#             ["1", "1", "1"]
#         )
#
#         try:
#             test_cube_face.fill_central_row([1])
#             raise AssertionError("Error message did not raise.")
#         except AssertionError as error:
#             assert str(error) == WRONG_LENGTH
#
#     def test_fill_cube_right_col(self):
#         test_cube_face = CubeFace(face_input="123456789")
#         test_cube_face.fill_right_col(["1", "1", "1"])
#         np.testing.assert_array_equal(
#             test_cube_face.get_right_col(),
#             ["1", "1", "1"]
#         )
#
#         try:
#             test_cube_face.fill_right_col([1])
#             raise AssertionError("Error message did not raise.")
#         except AssertionError as error:
#             assert str(error) == WRONG_LENGTH
#
#     def test_fill_cube_left_col(self):
#         test_cube_face = CubeFace(face_input="123456789")
#         test_cube_face.fill_left_col(["1", "1", "1"])
#         np.testing.assert_array_equal(
#             test_cube_face.get_left_col(),
#             ["1", "1", "1"]
#         )
#
#         try:
#             test_cube_face.fill_left_col([1])
#             raise AssertionError("Error message did not raise.")
#         except AssertionError as error:
#             assert str(error) == WRONG_LENGTH
#
#     def test_fill_cube_central_col(self):
#         test_cube_face = CubeFace(face_input="123456789")
#         test_cube_face.fill_central_col(["1", "1", "1"])
#         np.testing.assert_array_equal(
#             test_cube_face.get_central_col(),
#             ["1", "1", "1"]
#         )
#
#         try:
#             test_cube_face.fill_central_col([1])
#             raise AssertionError("Error message did not raise.")
#         except AssertionError as error:
#             assert str(error) == WRONG_LENGTH
#
#
# class TestCubeFaceClassError:
#     def test_special_case(self):
#         try:
#             CubeFace(face_input="123")
#             raise AssertionError("Error message did not raise.")
#         except AssertionError as error:
#             assert str(error) == WRONG_LENGTH
