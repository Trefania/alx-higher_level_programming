#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [replace if replace != search else find for replace in my_list]
    return new_list
