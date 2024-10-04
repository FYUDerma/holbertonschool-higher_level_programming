#!/usr/bin/python3
"""
Learn how to serialize and deserialize
Custom Python objects using the pickle module.
"""
import json
import pickle


class CustomObject:
    """
    A custom object to test serialization and deserialization.
    """
    def __init__(self, name, age, is_student):
        """
        Initialize the custom object.
        """
        self.__name__ = name
        self.__age__ = age
        self.__is_student__ = is_student

    def display(self):
        print("Name: {}".format(self.__name__))
        print("age: {}".format(self.__age__))
        print("is_student: {}".format(self.__is_student__))

    def serialize(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)
