"""
rand.py

This module provides functions for generating random number array.

Functions:
- random_array: Generates random number array between 1 to 20
"""
import subprocess

def random_array(arr):
    """
    Generates random array

    Parameters:
    arr (array): Input array, with 'None'/ dummy values 

    Returns:
    array: Randomly generated number array return
    """
    shuffled_num = None
    for i, _ in enumerate(arr):
        shuffled_num = subprocess.run(["shuf", "-i1-20", "-n1"], capture_output=True, check=True)
        arr[i] = int(shuffled_num.stdout)
    return arr
