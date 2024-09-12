import pytest
from hw2_debugging import mergeSort

def test_merge_sort_basic():
    arr = [5, 3, 8, 4, 2]
    expected = [2, 3, 4, 5, 8]
    assert mergeSort(arr) == expected