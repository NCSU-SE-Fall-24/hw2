import pytest
from hw2_debugging import merge_sort


def test_merge_sort_with_duplicates():
    assert merge_sort([4, 5, 3, 5, 2]) == [2, 3, 4, 5, 5]
