#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [replace if search == n else n for n in my_list]
    return new_list
