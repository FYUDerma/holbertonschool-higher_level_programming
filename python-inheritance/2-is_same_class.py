#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_same_class(obj, a_class):
    """
    Checks if an object is of the same class as the provided class.

    Args:
        obj (object): The object to check.
        a_class (class): The class to compare with.

    Returns:
        bool: True if the object is of the same class, False otherwise.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
