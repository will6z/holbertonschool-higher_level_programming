#!/usr/bin/python3
class BaseGeometry:
    def area(self):
        raise Exception("area() no esta implementada")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} debe ser integer".format(name))
        if value <= 0:
            raise ValueError("{} debe ser mayor que 0".format(name))
