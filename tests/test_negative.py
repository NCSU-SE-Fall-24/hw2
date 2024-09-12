import pytest
from hw2_debugging import merge_sort

def test_merge_sort_negative_numbers():
    arr = [-5, -3, -8, 4, 2]
    expected = [-8, -5, -3, 2, 4]
    assert mergeSort(arr) == expected