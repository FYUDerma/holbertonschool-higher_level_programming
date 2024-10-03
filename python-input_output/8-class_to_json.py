#!/usr/bin/python3
"""function that returns the dictionary description with simple data structure"""


def class_to_json(obj):
    """
    Returns a dictionary description of an object for JSON serialization.

    Args:
        obj: An instance of a class with serializable attributes (list, dictionary, string, integer, boolean)

    Returns:
        A dictionary representation of the object's attributes
    """
    json_dict = {}
    for attr in dir(obj):
        if not attr.startswith('__'):  # exclude special attributes
            value = getattr(obj, attr)
            if isinstance(value, (list, dict, str, int, bool)):
                json_dict[attr] = value
    return json_dict
