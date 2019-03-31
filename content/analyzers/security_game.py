"""Play the game that defines security."""

import random
from content.encrypt_bit.encryption import Encryption
from content.helper.utility import generate_random_keys

# key_length = int(input("Type in desired key length: "))
# message_one = input("Type in the first message: ")
# message_two = input("Type in the second message: ")
#
# message_one = "1" * 108 if message_one == "1" else message_one
# message_one = "0" * 108 if message_one == "0" else message_one
# message_two = "1" * 108 if message_two == "1" else message_two
# message_two = "0" * 108 if message_two == "0" else message_two
#
# cube_one = Encryption(message=message_one, cube_side_length=3)
# cube_two = Encryption(message=message_two, cube_side_length=3)
# key = generate_random_keys(length=key_length, max_index=1)
#
# random_bit = random.choice([True, False])
#
# if random_bit:
#     cube_one.encrypt(key=key)
#     print(cube_one.get_current_binary())
# else:
#     cube_two.encrypt(key=key)
#     print(cube_two.get_current_binary())
#
# guess = int(input("Type in 1 or 2."))
#
# if guess == 1 and random_bit:
#     print("Congrats!")
# else:
#     print("Try Again.")

# Track how bits travel.
# How many bits are different with the same message and same key.
# At each stage how many 1's I have.
# Key length.

key = generate_random_keys(length=20, max_index=1)

for _ in range(20):

    cube = Encryption(message="\0" * 108, cube_side_length=3)
    content = cube.get_current_binary()
    print(f"The number of 0 is {content.count('0')} and the number of 1 is "
          f"{content.count('1')}")
    cube.encrypt(key=key)
    content = cube.get_current_binary()
    print(f"The number of 0 is {content.count('0')} and the number of 1 is "
          f"{content.count('1')}")
    print("")
    print("")



