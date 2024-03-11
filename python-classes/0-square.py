"""A square module

This script defines a square
And hides the size by making it
a private variable

Contains the function/method:
    tell - which prints out information 
    about the square

    can be called using:
    objectName = Square('ObjectArgument - value')
    objectName.tell() 

"""

class Square:

    """
    A class square that defines a square
    with 'size'

    Contains two methods
    1. the innit constructor with the size argument in parentheses
    2. the tell, which serves as the getter, as it displays the val
        value of the private attribute - __size
    """

    def __init__(self, size):
        '''initializing size 

        Initialzes the size of the square
        
        '''
        self.__size = size
    
    # def tell(self):
    #     '''Displaying the private size'''
    #     print("Size: {}".format(self.__size))


# sm = Square(44)
# print(__import__("0-square").Square.__doc__)
# sm.tell()
