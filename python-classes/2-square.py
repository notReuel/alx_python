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

    def area(self):
        """Public instance method: Returns the area of the square"""
        return (self.__size**2)