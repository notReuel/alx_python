"""A square module

This script calculates the area of
the square of a square
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

        """convert int to string for iteration"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size == '':
            self.__size = 0
        
        elif size <= 0:
            raise ValueError("size must be >= 0")            
        
        else: 
            self.__size = size
            #print("(Size initialized to: {})".format(self.__size))

    @property
    def size(self):
        return self.__size

    def __repr__(self):
        """
        Return string representation of the object
        """
        return str(self.__dict__)
    
    def area(self):
        areaOfSquare = self.__size**2
        return areaOfSquare
        # print("Area: {}".format(areaOfSquare))   
    
    @size.setter
    def size(self, size):
        # if value >= 0 and isinstance(value, int):
        self.__size = size
        # value = self.__size
        # return value

    @size.getter
    def size(self):
        sizeofSquare = self.__size
        return sizeofSquare
    
        """
        Getter to retrieve the size of the private variable
        """
            
        # if not isinstance(value, int):
        #     raise TypeError("size must be an integer")
        
        # elif value <= 0:
        #     raise ValueError("size must be >= 0")            
        
        # else: 
        #     self.__size = value

    def my_print(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
            
        
my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")
# mySquare.size(12)
# print("Area: {} for size: {}".format(mySquare.area(), mySquare.get_size))
# mySquare.get_size()
# print(mySquare)

# print(type(mySquare)) 
# print(mySquare.__repr__)