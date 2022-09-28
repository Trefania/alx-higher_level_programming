#!/usr/bin/python3
def uniq_add(my_list=[]):
    res_list = set(my_list)
    res = 0
    for uniqs in res_list:
        res += uniqs
    return res
