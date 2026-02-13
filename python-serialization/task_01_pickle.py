#!/usr/bin/env python3
"""
Pickling Custom Classes Module
Provides a CustomObject class with serialization and deserialization
methods using the pickle module.
"""

import pickle


class CustomObject:
    """
    A custom class that can be serialized and deserialized using pickle.
    """

    def __init__(self, name, age, is_student):
        """
        Initialize the CustomObject instance.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Student status.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes in the required format.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance to a file using pickle.

        Args:
            filename (str): The file where the object will be saved.

        Returns:
            None
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an instance of CustomObject from a file.

        Args:
            filename (str): The file to load the object from.

        Returns:
            CustomObject or None: The deserialized object, or None if an error occurs.
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                if isinstance(obj, cls):
                    return obj
        except (OSError, pickle.PickleError, EOFError):
            return None

        return None
