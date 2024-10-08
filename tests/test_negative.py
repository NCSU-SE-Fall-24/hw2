"""
This is test case checking array with negative numbers
"""
from hw2_debugging import merge_sort


def test_merge_sort_negative_numbers():
    """
    This checks array with negative numbers
    """
    arr = [-5, -3, -8, 4, 2]
    expected = [-8, -5, -3, 2, 4]
    assert merge_sort(arr) == expected
