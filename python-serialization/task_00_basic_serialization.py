#!/usr/bin/env python3
"""
Basic Serialization Module
Provides functions to serialize a Python dictionary to a JSON file
and deserialize a JSON file back into a Python dictionary.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to JSON and save it to a file.

    Args:
        data (dict): The Python dictionary to serialize.
        filename (str): The name of the file to save the JSON data to.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load JSON data from a file and deserialize it into a Python dictionary.

    Args:
        filename (str): The name of the JSON file to read from.

    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
