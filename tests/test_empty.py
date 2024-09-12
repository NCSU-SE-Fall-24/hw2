import pytest
from hw2_debugging import merge_sort

def test_merge_sort_empty():
    arr = []
    expected = []
    assert merge_sort(arr) == expected