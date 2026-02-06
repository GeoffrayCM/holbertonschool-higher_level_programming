#!/usr/bin/env python3
"""Abstract Animal class and its subclasses Dog and Cat"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals"""

    @abstractmethod
    def sound(self):
        """Return the sound of the animal"""
        pass


class Dog(Animal):
    """Dog class"""

    def sound(self):
        """Return the sound of a dog"""
        return "Bark"


class Cat(Animal):
    """Cat class"""

    def sound(self):
        """Return the sound of a cat"""
        return "Meow"
