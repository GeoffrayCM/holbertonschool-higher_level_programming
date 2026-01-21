#!/usr/bin/python3
# 8-simple_delete.py

def simple_delete(a_dictionary, key=""):
    """delete a key in a dictionary."""
    
    if key in a_dictionary:
        del a_dictionary[key]

    return (a_dictionary)
