#!/usr/bin/python3
"""
basic serialization module that adds the functionality to serialize
A Python dictionary to a JSON file and deserialize the JSON file
to recreate the Python Dictionary.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    Args:
        data (dict): The Python dictionary to serialize.
        filename (str): The filename of the output JSON file.

    Returns:
        None
    """
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def load_and_deserialize(filename):
    """
    Load and deserialize a JSON file to a Python dictionary.

    Args:
        filename (str): The filename of the input JSON file.

    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, 'r') as f:
        data = json.load(f)
    return data
