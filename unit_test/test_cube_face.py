from cube_encryption.cubie import Cubie
from cube_encryption.cube_face import CubeFace
from cube_encryption.constants import WRONG_CUBE_FACE_INPUT, \
    WRONG_SIDE_LENGTH, INDEX_OUT_CUBE_LENGTH


class TestCubeFace:
    # Setup testing input.
    face_input = "000100100101101010101010101010101010"
    cube_face = CubeFace(cube_face_input=face_input, cube_side_length=3)

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

    def test_cube_row_str(self):
        # Get rows as strings and check if they equal to desired value.
        row_str_0 = self.cube_face.get_row_str(row_index=0)
        row_str_1 = self.cube_face.get_row_str(row_index=1)
        assert row_str_0 == "|0001|0010|0101|"
        assert row_str_1 == "|1010|1010|1010|"


class TestCubeFaceErrorCheck:
    # Setup testing input.
    face_input = "000100100101101010101010101010101010"
    cube_face = CubeFace(cube_face_input=face_input, cube_side_length=3)

    def test_init(self):
        try:
            CubeFace(cube_face_input="abracadabra", cube_side_length=3)
            raise AssertionError("Error message did not raise.")
        except AssertionError as error:
            assert str(error) == WRONG_CUBE_FACE_INPUT

    def test_fill_row(self):
        try:
            self.cube_face.fill_row(
                row_index=1,
                input_list=[
                    Cubie(cubie_input=list("0000"))
                ]
            )
            raise AssertionError("Error message did not raise.")
        except AssertionError as error:
            assert str(error) == WRONG_SIDE_LENGTH

        try:
            self.cube_face.fill_row(
                row_index=3,
                input_list=[
                    Cubie(cubie_input=list("0000")),
                    Cubie(cubie_input=list("0000")),
                    Cubie(cubie_input=list("0000"))
                ]
            )
            raise AssertionError("Error message did not raise.")
        except AssertionError as error:
            assert str(error) == INDEX_OUT_CUBE_LENGTH

    def test_fill_col(self):
        try:
            self.cube_face.fill_col(
                col_index=1,
                input_list=[
                    Cubie(cubie_input=list("0000"))
                ]
            )
            raise AssertionError("Error message did not raise.")
        except AssertionError as error:
            assert str(error) == WRONG_SIDE_LENGTH

        try:
            self.cube_face.fill_col(
                col_index=3,
                input_list=[
                    Cubie(cubie_input=list("0000")),
                    Cubie(cubie_input=list("0000")),
                    Cubie(cubie_input=list("0000"))
                ]
            )
            raise AssertionError("Error message did not raise.")
        except AssertionError as error:
            assert str(error) == INDEX_OUT_CUBE_LENGTH
