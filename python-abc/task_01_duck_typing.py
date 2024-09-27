#!/usr/bin/env python3
"""Module for demonstrating shapes and their properties."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for all shapes.

    This class defines the interface for all shapes.
    """

    @abstractmethod
    def area(self):
        """
        Calculates the area of the shape.

        Returns:
            float: The area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculates the perimeter of the shape.

        Returns:
            float: The perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Represents a circle shape.

    Attributes:
        radius (float): The radius of the circle.
    """

    def __init__(self, radius):
        """
        Initializes a circle with a given radius.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle (πr^2).
        """
        return math.pi * self.radius * self.radius

    def perimeter(self):
        """
        Calculates the perimeter of the circle.

        Returns:
            float: The perimeter of the circle (2πr).
        """
        return abs(2 * math.pi * self.radius)


class Rectangle(Shape):
    """
    Represents a rectangle shape.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a rectangle with a given width and height.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            float: The area of the rectangle (width * height).
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle (2 * (width + height)).
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Displays the area and perimeter of a given shape.

    Args:
        shape (Shape): An instance of a shape class.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
