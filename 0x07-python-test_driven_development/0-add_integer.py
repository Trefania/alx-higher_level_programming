#!/usr/bin/python3
"""def an int addition func"""


def add_integer(a, b=98):
    """Return the integer for both addition of a and b

    floats aare going to be typecasted to integer be4 adding to two.

    Error message is being raise if both are not floats or integer.
    """
    sum = int a + int b

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (sum)

