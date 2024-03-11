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

    def __init__(self, size=0):
        '''initializing size 

        Initialzes the size of the square

        With an if statement to validate the inputed size type
        to check if the size value is valid - greater than 0 
        and not a string/word
        
        '''
        self.__size = size

        """convert int to string for iteration"""
        iterSize = str(size)
        if size <= 0:
            print("size must be >= 0")            
            raise ValueError
        
        if not any(char.isdigit() for char in iterSize):
            print("size must be an integer")
            raise TypeError
            
        else: 
            print("(Size initialized to: {})".format(size))
    
mySquare = Square(3)
# print(mySquare)
