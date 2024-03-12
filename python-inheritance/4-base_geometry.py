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
    

# bg = BaseGeometry()

# try:
#     print(bg.area())
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))


# # bg = BaseGeometry()

# # print(bg)
# # print(dir(bg))
# # print(dir(BaseGeometry))
    