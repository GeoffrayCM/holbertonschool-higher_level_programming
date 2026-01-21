#!/usr/bin/python3
# 10-best_score.py

def best_score(a_dictionary):
    """returns a key with the biggest integer value."""

     if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    best_key = None
    best_value = float('-inf')

    for key, value in a_dictionary.items():
        if value > best_value:
            best_value = value
            best_key = key

    return best_key
