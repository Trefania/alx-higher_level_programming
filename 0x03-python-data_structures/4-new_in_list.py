#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx >= (len(my_list)-1):
        return my_list
    temporary_list = list(my_list)
    temporary_list[idx] = element
    return temporary_list
