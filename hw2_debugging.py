"""
hw2_debugging.py

This module provides functions performing merge sort

Functions:
- merge_sort: Main function for performing merge_sort, performs Divide and conquer
- recombine: Compare the elements and combine the array
"""
import rand


def merge_sort(arr):
    """
    Performs the merge sort using divide and conquer algorithm

    Parameters:
    arr (array): Number array that needs to be sorted

    Returns:
    array: Returns sorted array
    """
    if len(arr) == 1:
        return arr

    half = len(arr) // 2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(left_arr, right_arr):
    """
    Combines and sort divided array

    Parameters:
    left_arr (array): First half of number array that needs to be sorted and combined
    right_arr (array): Second half of number array that needs to be sorted and combined

    Returns:
    array: Returns combined array in sorted form
    """
    left_index = 0
    right_index = 0
    merge_arr = []

    # Merge elements from both arrays in sorted order
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr.append(left_arr[left_index])
            left_index += 1
        else:
            merge_arr.append(right_arr[right_index])
            right_index += 1

    # Append the remaining elements from both arrays
    merge_arr.extend(left_arr[left_index:])
    merge_arr.extend(right_arr[right_index:])
    return merge_arr


if __name__ == "__main__":
    local_arr = rand.random_array([None] * 20)
    arr_out = merge_sort(local_arr)

    print(arr_out)
