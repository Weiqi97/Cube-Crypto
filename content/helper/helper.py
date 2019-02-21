import numpy as np
from typing import List
from content.helper.constants import Key, CUBE_MOVE, MOVE_ANGLE


def generate_random_keys(length: int, max_index: int) -> List[Key]:

    return [
        Key(
            move=np.random.choice(CUBE_MOVE, size=1)[0],
            angle=np.random.choice(MOVE_ANGLE, size=1)[0],
            index=np.random.randint(low=1, high=max_index + 1)
        ) for _ in range(length)
    ]
