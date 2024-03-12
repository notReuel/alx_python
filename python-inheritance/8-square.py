"""
A module with a blank class called geometry

to be tested by the alx intranet checker
"""

class BaseGeometry:
    """
    A class called base geomtry

    with a public instance method called area that
    raises an exception if the area is not called.
    """
    pass

    def __init__(self):
        """
        Empty Innit Constructor
        """
        # self.area = area
        pass

    @property
    def area(self):
        """
        A method that returns or raises the Exception signalling that
        the area has not yet been implememted
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        A function to validate the user input and check if 
        a proper value or type was used.
        
        """
        self.name = name

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(self.name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
        else: 
            self.value = value
        return self.value
    
# //////// INHERITANCE STARTS HERE ////////////
class Rectangle(BaseGeometry):
    """
    A class called Rectangle inheriting from a
    the base class 'BaseGeometry'
    """
    
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def integer_validator(self, width, height):
        # BaseGeometry.integer_validator(self, name, value)
        self.__width = width
        self.__height = height
    
    def area(self):
        self.area = self.__width * self.__height
        return self.area
    
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
    
# ////// INHERITANCE FROM RECTANGLE -  A GRAND CHILD OF CLASS BASEGEOMETRY
class Square(Rectangle):
    
    def __init__(self, size):
        # super().__init__(width, height)
        self.__size = size

    
    @property
    def integer_validator(self, size):
        self.__size = size

    def area(self):
        self.area = self.__size*self.__size
        return self.area
        # return the self.area
    
    def __str__(self):
        return "[Rectangle] {0}/{0}".format(self.__size)
        # add the return string here

s = Square(13)

print(s)
print(s.area())