"""def BaseGeometry class"""
class MetaClass(type):
    def __dir__(cls):
        ''''
        ovrides dir() method to execlude __init_subclasses__
        '''
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
class BaseGeometry(metaclass=MetaClass):
    '''Base class for Geometry'''
    def __dir__ (cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    def area(self):
        """Public instance method: def area(self): that raises an Exception with the message area() is not implemented"""
        raise Exception('area() is not implemented')
    def integer_validator(self, name, value):
        '''Public instance method: that validates value:'''
        if not (type(value) == int):
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))