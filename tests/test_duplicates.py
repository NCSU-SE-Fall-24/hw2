"""
This is test case for checking array with duplicates
"""
from hw2_debugging import merge_sort


def test_merge_sort_with_duplicates():
    """
    This function checks that array with duplicates are properly sorted
    """
    assert merge_sort([4, 5, 3, 5, 2]) == [2, 3, 4, 5, 5]
