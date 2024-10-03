#!/usr/bin/python3
"""function to convert Python objects into JSON formatted strings."""
import json


def load_from_json_file(filename):
    """Write an object to a text file using JSON representation."""
    with open(filename) as f:
        return json.load(f)
