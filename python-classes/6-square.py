#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """A class that defines a square with position printing."""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    @property
    def size(self):
        """Gets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position with validation."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints the square with position offset."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
