"""
This is test case checking for empty array
"""
from hw2_debugging import merge_sort


def test_merge_sort_empty():
    """
    This is test case checking for empty array
    """
    arr = []
    expected = []
    assert merge_sort(arr) == expected
