import pytest
from hw2_debugging import mergeSort

def test_merge_sort_empty():
    arr = []
    expected = []
    assert mergeSort(arr) == expected