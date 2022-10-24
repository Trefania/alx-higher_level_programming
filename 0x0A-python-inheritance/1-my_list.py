#!/usr/bin/python3
"""This module inherits from the list class"""


class MyList(list):
    """A MyList class that inherits from list"""
    def print_sorted(self):
        """printing a sorted list"""
        print(sorted(self))
