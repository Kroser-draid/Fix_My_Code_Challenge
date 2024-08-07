#!/usr/bin/python3
"""
Module for square class
"""


class Square():
    """ Class for square """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ initiating of the class """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """ perimeter of the square """
        return ((self.width + self.height) * 2)

    def __str__(self):
        """ method to return string to the print function if called the object """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
