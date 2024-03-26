'''
Square class
'''
from models.rectangle import Rectangle
'''
Import the class Rectangle from the models directory
'''

class Square(Rectangle):
    '''
    process definition of the the descedanr class rectangle
    
    The class constructor with all the parameters are called
    and the super class uses the logic of teh __init__ in the 
    Rectangle class.

    Howeer the width and height are assigned to the value of size

    the width and height are inheritted from the class Rectangle
    '''

    
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id) 
        #size to hold width and size to hold height

    def __str__(self):
        return "[square] {} {}/{} - {}".format(self.id, self.x, self.y, self.width)


