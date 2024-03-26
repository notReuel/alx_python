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
    

# bg = BaseGeometry()

# bg.integer_validator("my_int", 12)
# bg.integer_validator("width", 89)

# try:
#     bg.integer_validator("name", "John")
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))

# try:
#     bg.integer_validator("age", 0)
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))

# try:
#     bg.integer_validator("distance", -4)
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))
    