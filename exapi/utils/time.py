"""Has utils for work with time."""

import time


def get_timestamp() -> int:
    """Returns current timestamp in milliseconds.

    Returns:
        int
    """

    return int(time.time() * 1000)
