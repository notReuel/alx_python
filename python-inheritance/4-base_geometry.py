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
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

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
    