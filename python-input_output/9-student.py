#!/usr/bin/python3
"""class Student that defines a student"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns a dictionary description of an object for JSON serialization.

        Returns:
            A dictionary representation of the object's attributes
        """
        json_dict = {}
        for attrs in dir(self):
            if not attr.startswith('__'):  # exclude special attributes
                value = getattr(self, attrs)
                if isinstance(value, (list, dict, str, int, bool)):
                    json_dict[attrs] = value
        return json_dict
