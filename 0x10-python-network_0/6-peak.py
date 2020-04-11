#!/usr/bin/python3
"""find the peak in a list of unsorted integers"""


def findFpeak(int_list, low, high):
    """find the peak in the list"""
    middle = int(low + (high - low) / 2)

    if ((middle == 0 or int_list[middle - 1] <= int_list[middle]) and (
            middle == len(int_list) - 1 or int_list[middle + 1] <=
            int_list[middle])):
        return int_list[middle]
    elif (middle > 0 and int_list[middle - 1] > int_list[middle]):
        return findFpeak(int_list, low, (middle - 1))
    else:
        return findFpeak(int_list, (middle + 1), high)


def find_peak(list_of_integers):
    """find the peak in the list"""
    if not list_of_integers:
        return None

    return findFpeak(list_of_integers, 0, len(list_of_integers) - 1)
