import numpy as np
from collections import deque
from content.encryption.cube_face_for_item import CubeFaceForItem
from content.helper.constants import WRONG_CUBE_FACE_INPUT, \
    WRONG_SIDE_LENGTH, WRONG_FRAME_INDEX_NAME, WRONG_FRAME_COLUMN_NAME


class TestCubeFace:
    # Setup testing input.
    face_input = [item for item in range(9)]
    cube_face = CubeFaceForItem(cube_face_input=face_input, cube_side_length=3)

    def test_cube_face(self):
        assert np.array_equal(self.cube_face.get_item_list, self.face_input)

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
        assert row_t1[0] == 0
        row_d1 = self.cube_face.get_row(row_name="D1")
        assert row_d1[0] == 6

    def test_cube_fill_row(self):
        # Create new testing cube face since the value get changed.
        cube_face = CubeFaceForItem(
            cube_face_input=self.face_input,
            cube_side_length=3
        )
        cube_face.fill_row(row_name="T1", input_list=[100, 200, 300])
        # Get row and check if it contains desired value.
        row_t1 = cube_face.get_row(row_name="T1")
        assert row_t1[0] == 100

    def test_cube_col(self):
        # Get cols and check if they contain desired value.
        col_r1 = self.cube_face.get_col(col_name="R1")
        assert col_r1[0] == 2
        col_l1 = self.cube_face.get_col(col_name="L1")
        assert col_l1[0] == 0

    def test_cube_fill_col(self):
        # Create new testing cube face since the value get changed.
        cube_face = CubeFaceForItem(
            cube_face_input=self.face_input,
            cube_side_length=3
        )
        cube_face.fill_col(col_name="R1", input_list=[100, 200, 300])
        # Get col and check if it contains desired value.
        col_r1 = cube_face.get_col(col_name="R1")
        assert col_r1[1] == 200

    def test_cube_rotate(self):
        # Create new testing cube face since the value get changed.
        cube_face = CubeFaceForItem(
            cube_face_input=self.face_input,
            cube_side_length=3
        )
        # Rotate the face and check if it contains desired value.
        cube_face.rotate_by_angle(angle=90)
        assert np.array_equal(
            cube_face.get_item_list,
            [6, 3, 0, 7, 4, 1, 8, 5, 2]
        )


class TestCubeFaceErrorCheck:
    # Setup testing input.
    face_input = [item for item in range(9)]
    cube_face = CubeFaceForItem(cube_face_input=face_input, cube_side_length=3)

    def test_init(self):
        try:
            CubeFaceForItem(cube_face_input=list("wrong"), cube_side_length=3)
            raise AssertionError("Error message did not raise.")
        except AssertionError as error:
            assert str(error) == WRONG_CUBE_FACE_INPUT

    def test_fill_row(self):
        try:
            self.cube_face.fill_row(row_name="T1", input_list=[1])
            raise AssertionError("Error message did not raise.")
        except AssertionError as error:
            assert str(error) == WRONG_SIDE_LENGTH

        try:
            self.cube_face.fill_row(
                row_name="abracadabra",
                input_list=[1, 2, 3]
            )
            raise AssertionError("Error message did not raise.")
        except AssertionError as error:
            assert str(error) == WRONG_FRAME_INDEX_NAME

    def test_fill_col(self):
        try:
            self.cube_face.fill_col(col_name="R1", input_list=[1])
            raise AssertionError("Error message did not raise.")
        except AssertionError as error:
            assert str(error) == WRONG_SIDE_LENGTH

        try:
            self.cube_face.fill_col(
                col_name="abracadabra",
                input_list=[1, 2, 3]
            )
            raise AssertionError("Error message did not raise.")
        except AssertionError as error:
            assert str(error) == WRONG_FRAME_COLUMN_NAME
