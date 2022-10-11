#!/usr/bin/python3
"""Defs a class Square"""


class Square:
    """showing a square"""
    def __init__(self, size=0):
        """square class is being initialized
        size - is an arguement that is being passed
        """
        if (size != int):
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")

            self.__size = size
