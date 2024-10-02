#!/usr/bin/python3
"""function to convert Python objects into JSON formatted strings."""
import json


def to_json_string(my_obj):
    """Returns JSON representation of an object"""
    return json.dumps(my_obj)
