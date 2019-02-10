from collections import deque
from cube_encryption.cubie import Cubie
from cube_encryption.cube_face_for_cubie import CubeFaceForCubie
from cube_encryption.constants import WRONG_CUBE_FACE_INPUT, \
    WRONG_SIDE_LENGTH, WRONG_FRAME_INDEX_NAME, WRONG_FRAME_COLUMN_NAME


class TestCubeFace:
    # Setup testing input.
    face_input = list("000100100101101010101010101010101010")
    cube_face = CubeFaceForCubie(cube_face_input=face_input, cube_side_length=3)

    def test_cube_face(self):
        assert self.cube_face.face_string == "".join(self.face_input)

    def test_cube_frame_column(self):
        assert self.cube_face.get_frame_column(cube_side_length=4) == \
            deque(["L2", "L1", "R1", "R2"])
        assert self.cube_face.get_frame_column(cube_side_length=5) == \
            deque(["L2", "L1", "C", "R1", "R2"])

    def test_cube_frame_index(self):
        assert self.cube_face.get_frame_index(cube_side_length=4) == \
            deque(["T2", "T1", "D1", "D2"])
        assert self.cube_face.get_frame_index(cube_side_length=5) == \
            deque(["T2", "T1", "C", "D1", "D2"])

    def test_cube_row(self):
        # Get rows and check if they contain desired value.
        row_t1 = self.cube_face.get_row(row_name="T1")
        assert row_t1[0].get_content_string() == "0001"
        row_d1 = self.cube_face.get_row(row_name="D1")
        assert row_d1[0].get_content_string() == "1010"

    def test_cube_fill_row(self):
        # Create new testing cube face since the value get changed.
        cube_face = CubeFaceForCubie(
            cube_face_input=self.face_input,
            cube_side_length=3
        )
        cube_face.fill_row(
            row_name="T1",
            input_list=[
                Cubie(list("1111")),
                Cubie(list("1111")),
                Cubie(list("1111"))
            ]
        )
        # Get rows and check if they contain desired value.
        row_t1 = cube_face.get_row(row_name="T1")
        assert row_t1[0].get_content_string() == "1111"
        row_d1 = self.cube_face.get_row(row_name="D1")
        assert row_d1[0].get_content_string() == "1010"

    def test_cube_col(self):
        # Get cols and check if they contain desired value.
        col_r1 = self.cube_face.get_col(col_name="R1")
        assert col_r1[0].get_content_string() == "0101"
        col_l1 = self.cube_face.get_col(col_name="L1")
        assert col_l1[0].get_content_string() == "0001"

    def test_cube_fill_col(self):
        # Create new testing cube face since the value get changed.
        cube_face = CubeFaceForCubie(
            cube_face_input=self.face_input,
            cube_side_length=3
        )
        cube_face.fill_col(
            col_name="R1",
            input_list=[
                Cubie(list("1111")),
                Cubie(list("1111")),
                Cubie(list("1111"))
            ]
        )
        # Get cols and check if they contain desired value.
        col_r1 = cube_face.get_col(col_name="R1")
        assert col_r1[0].get_content_string() == "1111"
        col_l1 = cube_face.get_col(col_name="L1")
        assert col_l1[0].get_content_string() == "0001"

    def test_cube_row_str(self):
        # Get rows as strings and check if they equal to desired value.
        row_t1_str = self.cube_face.get_row_str(row_name="T1")
        row_d1_str = self.cube_face.get_row_str(row_name="D1")
        assert row_t1_str == "|0001|0010|0101|"
        assert row_d1_str == "|1010|1010|1010|"

    def test_cube_face_rotate(self):
        # Create new testing cube face since the value get changed.
        cube_face = CubeFaceForCubie(
            cube_face_input=self.face_input,
            cube_side_length=3
        )
        cube_face.rotate_by_angle(angle=90)
        assert cube_face.face_string == "100000011010010101010101010101010101"


class TestCubeFaceErrorCheck:
    # Setup testing input.
    face_input = list("000100100101101010101010101010101010")
    cube_face = CubeFaceForCubie(cube_face_input=face_input, cube_side_length=3)

    def test_init(self):
        try:
            CubeFaceForCubie(cube_face_input=list("abracadabra"), cube_side_length=3)
            raise AssertionError("Error message did not raise.")
        except AssertionError as error:
            assert str(error) == WRONG_CUBE_FACE_INPUT

    def test_fill_row(self):
        try:
            self.cube_face.fill_row(
                row_name="T1",
                input_list=[
                    Cubie(cubie_input=list("0000"))
                ]
            )
            raise AssertionError("Error message did not raise.")
        except AssertionError as error:
            assert str(error) == WRONG_SIDE_LENGTH

        try:
            self.cube_face.fill_row(
                row_name="abracadabra",
                input_list=[
                    Cubie(cubie_input=list("0000")),
                    Cubie(cubie_input=list("0000")),
                    Cubie(cubie_input=list("0000"))
                ]
            )
            raise AssertionError("Error message did not raise.")
        except AssertionError as error:
            assert str(error) == WRONG_FRAME_INDEX_NAME

    def test_fill_col(self):
        try:
            self.cube_face.fill_col(
                col_name="R1",
                input_list=[
                    Cubie(cubie_input=list("0000"))
                ]
            )
            raise AssertionError("Error message did not raise.")
        except AssertionError as error:
            assert str(error) == WRONG_SIDE_LENGTH

        try:
            self.cube_face.fill_col(
                col_name="abracadabra",
                input_list=[
                    Cubie(cubie_input=list("0000")),
                    Cubie(cubie_input=list("0000")),
                    Cubie(cubie_input=list("0000"))
                ]
            )
            raise AssertionError("Error message did not raise.")
        except AssertionError as error:
            assert str(error) == WRONG_FRAME_COLUMN_NAME
