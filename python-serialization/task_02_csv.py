#!/usr/bin/env python3
"""
CSV to JSON Conversion Module
Provides a function to convert CSV data into JSON format.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to JSON format and save it as data.json.

    Args:
        csv_filename (str): The path to the CSV file.

    Returns:
        bool: True if conversion was successful, False otherwise.
    """
    try:
        data_list = []

        # Open and read CSV file
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data_list.append(row)

        # Write to JSON file
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, indent=4)

        return True

    except (FileNotFoundError, OSError, csv.Error, json.JSONDecodeError):
        return False
