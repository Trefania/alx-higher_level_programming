#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        a = fct(*args)
        return a
    except Exception as error:
        print("Exception: {}".format(error_m), file=sys.stderr)
        return None
