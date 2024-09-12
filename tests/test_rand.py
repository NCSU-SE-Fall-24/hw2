"""
This is test case for generation of random_array
"""
from rand import random_array


def test_random_array():
    """
    This is test case for generation of random_array
    """
    array = [None] * 20
    random_array_output = random_array(array)
    assert len(random_array_output) == 20
