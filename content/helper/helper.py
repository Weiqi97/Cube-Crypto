"""Define the helper functions that may accessed by different parts."""

import random
import binascii
import pandas as pd
from typing import List
from content.helper.constants import Key, CUBE_MOVE, MOVE_ANGLE
from content.encrypt_bit.face import Face


def generate_random_keys(length: int, max_index: int) -> List[Key]:
    """Generate a random key with cube moves for a certain size cube.

    :param length: Desired number of moves of the key.
    :param max_index: Max index of the cube side.
    :return: A list of random keys.
    """
    return [
        Key(
            move=random.choice(CUBE_MOVE),
            angle=random.choice(MOVE_ANGLE),
            index=random.randint(1, max_index)
        ) for _ in range(length)
    ]


def get_cube_layout(cube_side_length: int) -> pd.DataFrame:
    """Show the cube layout by returning a DataFrame."""
    # Create the pandas DataFrame filled with 0.
    return pd.DataFrame(
        data=0,
        index=Face.get_frame_index(
            cube_side_length=cube_side_length
        ),
        columns=Face.get_frame_column(
            cube_side_length=cube_side_length
        )
    )


def get_key_table(key: List[Key]) -> pd.DataFrame:
    """Get list of keys as a DataFrame."""
    # Extract the values from NamedTuple to list.
    key_value_list = [[key.move, key.index, key.angle] for key in key]

    # Pack values into a DataFrame.
    return pd.DataFrame(
        data=key_value_list,
        index=[index + 1 for index in range(len(key))],
        columns=["Movement", "Index", "Angle"]
    )


def xor(str_one: str, str_two: str) -> str:
    """Find the XOR result of two strings.

    :param str_one: The first input string.
    :param str_two: The second input string.
    :return: The XOR result of these two input strings.
    """
    return "".join(
        [
            "0" if value == str_two[index] else "1"
            for index, value in enumerate(str_one)
        ]
    )


def string_to_binary(input_string: str) -> str:
    """Convert Ascii string to binary string.

    :param input_string: An input Ascii encoded string.
    :return: The binary encoded equivalence of the input Ascii string.
    """
    byte_from_str = binascii.a2b_qp(input_string)
    binary_from_byte = bin(int.from_bytes(byte_from_str, byteorder="big"))
    binary_from_byte = binary_from_byte.replace("b", "")
    # Make sure what ever being returned is multiple of 8.
    return f"{'0' * (8 - len(binary_from_byte) % 8)}{binary_from_byte}" \
        if len(binary_from_byte) % 8 != 0 \
        else binary_from_byte


def binary_to_string(input_binary: str) -> str:
    """Convert binary string to Ascii string.

    :param input_binary: An input binary encoded string.
    :return: The Ascii encoded equivalence of the input binary string.
    """
    binary_from_str = int(input_binary, 2)
    byte_from_binary = binary_from_str.to_bytes(
        length=(binary_from_str.bit_length() + 7) // 8, byteorder="big"
    )
    return byte_from_binary.decode("utf-8")
