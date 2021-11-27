"""
Magic Index: A magic index in an array A [1. .. n -1] is defined to be an index such that A[i] = i.
Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in
array A.
FOLLOW UP
What if the values are not distinct?
"""


def magic_fast_distinct(arr):
    """ For distinct elements """
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def magic_fast(arr):
    return magic_fast_duplicate(arr, 0, len(arr) - 1)


def magic_fast_duplicate(arr, low, high):
    if low > high:
        return -1

    mid_index = (low + high) // 2
    mid_value = arr[mid_index]

    if mid_value == mid_index:
        return mid_index

    left_index = min(mid_index - 1, mid_value)
    left = magic_fast_duplicate(arr, low, left_index)
    if left > 0:
        return left

    right_index = max(mid_index + 1, mid_value)
    return magic_fast_duplicate(arr, right_index, high)
