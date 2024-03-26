"""
Base class
"""

class Base:
    '''
    This class will be the 'base' of all other classes
    '''

    __nb_objects = 0
    def __init__(self, id=None):
        '''
        defining the process of the function
        '''

        if id:
            '''
            manage id attribute in all your future classes
            '''            
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects


