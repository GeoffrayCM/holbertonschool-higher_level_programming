#!/usr/bin/python3
"""Function that checks if an object is an instance of a subclass of a_class"""


def inherits_from(obj, a_class):
    return isinstance(obj, a_class) and type(obj) is not a_class
