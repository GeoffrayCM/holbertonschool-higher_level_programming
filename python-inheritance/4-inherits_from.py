#!/usr/bin/python3
"""Function that checks if an object is an instance of a subclass of a_class"""


def inherits_from(obj, a_class):
    # type(obj) is not a_class ensures obj is not exactly a_class
    # isinstance(obj, a_class) checks if obj is an instance or inherited
    return isinstance(obj, a_class) and type(obj) is not a_class
