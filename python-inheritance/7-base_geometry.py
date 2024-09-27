#!/usr/bin/python3
"""Define a class BaseGeometry"""


class BaseGeometry:
    """
    This class represents a BaseGeometry.

    It does not have any attributes or methods currently.
    """
    def area(self):
        """
        Return the area of the BaseGeometry
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate a parameter as an integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        return value
