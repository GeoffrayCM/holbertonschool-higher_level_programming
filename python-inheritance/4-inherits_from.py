#!/usr/bin/python3
"""Function that returns """


def inherits_from(obj, a_class):
    """Return True if obj"""
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
