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
    __size = None

    def __init__(self, size=0):
        '''initializing size 

        Initialzes the size of the square

        With an if statement to validate the inputed size type
        to check if the size value is valid - greater than 0 
        and not a string/word
        
        '''

        """convert int to string for iteration"""
        if isinstance(size, int):
            self.__size = size 
        else: 
            raise TypeError('size must be an integer')
        if size >= 0:
            self.__size = size
        else: 
            raise ValueError('size must be >= 0')


#         iterSize = str(size)

#         if not isinstance(size, int):
#             raise TypeError("size must be an integer")

#         elif size == '':
#             self.__size = 0
        
#         elif size <= 0:
#             raise ValueError("size must be >= 0")            
        
#         else: 
#             self.__size = size
#             #print("(Size initialized to: {})".format(self.__size))

#     def __repr__(self):
#         """
#         Return string representation of the object
#         """
#         return str(self.__dict__)
    
# # mySquare = Square(1)
# # # print(mySquare)

# # print(type(mySquare)) 
# # print(mySquare.__repr__)

#     def __repr__(self):
#         """
#         Return string representation of the object
#         """
#         return str(self.__dict__)

#     def __call__(self):
#         return self.__dict__
    
# #mySquare = Square(-1)
# # print(mySquare)

# # print(type(mysquare)) 
# # print(mysquare.dict_)
