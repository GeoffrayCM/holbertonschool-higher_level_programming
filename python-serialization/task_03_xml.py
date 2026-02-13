#!/usr/bin/env python3
"""
XML Serialization Module
Provides functions to serialize a Python dictionary to XML
and deserialize XML back into a Python dictionary.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into XML format and save to a file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the XML output file.
    """
    try:
        # Create root element
        root = ET.Element("data")

        # Add dictionary items as child elements
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        # Create ElementTree and write to file
        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=False)

    except (OSError, TypeError):
        return None


def deserialize_from_xml(filename):
    """
    Deserialize XML data from a file into a Python dictionary.

    Args:
        filename (str): The XML file to read.

    Returns:
        dict or None: The reconstructed dictionary, or None if error occurs.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            result[child.tag] = child.text

        return result

    except (ET.ParseError, FileNotFoundError, OSError):
        return None
