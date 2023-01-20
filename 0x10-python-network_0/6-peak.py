#!/usr/bin/python3
"""A function that finds a peak in a list of unsorted integers."""


def find_peak(list_int):
    """
    Args:
        list_int(int): list of integers to find peak of
    Returns: peak of list_int or None
    """
    size = len(list_int)
    mid_e = size
    mid = size // 2

    if size == 0:
        return None

    while True:
        mid_e = mid_e // 2
        if (mid < size - 1 and
                list_int[mid] < list_int[mid + 1]):
            if mid_e // 2 == 0:
                mid_e = 2
            mid = mid + mid_e // 2
        elif mid_e > 0 and list_int[mid] < list_int[mid - 1]:
            if mid_e // 2 == 0:
                mid_e = 2
            mid = mid - mid_e // 2
        else:
            return list_int[mid]
