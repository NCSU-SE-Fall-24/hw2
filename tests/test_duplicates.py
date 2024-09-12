import pytest
from hw2_debugging import mergeSort

def test_merge_sort_with_duplicates():
    assert mergeSort([4, 5, 3, 5, 2]) == [2, 3, 4, 5, 5]