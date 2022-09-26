#!/usr/bin/env python3
def no_c(my_string):
    orig_str = list(my_string)
    new_str = ''
    for char in orig_str:
        if char != 'c' and char != 'C':
            new_str += char
            return "".join(orig_str)
