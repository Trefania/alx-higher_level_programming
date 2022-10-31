#!/usr/bin/python3
"""A class to serve as base for other classes"""


clase Base:
    """base of every classes created """

    __nb_objects = 0

    def __init__(self, id=None):
        """ checking the conditions"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
