import numpy as np
from cube_encryption.encryption import Encryption
from cube_encryption.key_analyzer import KeyAnalyzer


# Initialize the protocol.
protocol = Encryption(message="Dummy Message", cube_side_length=3)
# Find the reduced key length in average.
key_length = [
    len(KeyAnalyzer(key=protocol.generate_random_key(length=27)).analyze())
    for _ in range(10000)
]
# Print the mean.
print(np.mean(key_length))

# When key length is 20, the reduced key length is around: 15.05.
# When key length is 21, the reduced key length is around: 15.79.
# When key length is 25, the reduced key length is around: 18.73.
# When key length is 26, the reduced key length is around: 19.50.
# When key length is 27, the reduced key length is around: 20.20.
# When key length is 28, the reduced key length is around: 20.90.
