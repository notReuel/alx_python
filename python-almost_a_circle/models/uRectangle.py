from base import Base

class Rectangle(Base):

    # def __init__(self, id=None):
    #     super().__init__(id)

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    
    #///PROPERTIES
    @property
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height
    
    def x(self):
        return self.__x

    def y(self):
        return self.__y
    
    #/////////SETTERS
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    # @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value
            
    # @x.setter
    def x(self, value):
        if value <= 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value 

    # @y.setter
    def y (self, value):
        if value <= 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    #///// GETTERS ///// 
    @width.getter
    def width(self):
        return self.__width
    
    def height(self):
        return self.__height
    
    def x(self):
        return self.__x

    def y(self):
        return self.__y    

    
    
# if __name__ == "__main__":

#     r1 = Rectangle(10, 2)
#     print(r1.id)

#     r2 = Rectangle(2, 10)
#     print(r2.id)

#     r3 = Rectangle(10, 2, 0, 0, 12)
#     print(r3.id)   
        
# if __name__ == "__main__":

#     try:
#         Rectangle(10, "2")
#     except Exception as e:
#         print("[{}] {}".format(e.__class__.__name__, e))

#     try:
#         r = Rectangle(10, 2)
#         r.width = -10
#     except Exception as e:
#         print("[{}] {}".format(e.__class__.__name__, e))

#     try:
#         r = Rectangle(10, 2)
#         r.x = {}
#     except Exception as e:
#         print("[{}] {}".format(e.__class__.__name__, e))

#     try:
#         Rectangle(10, 2, 3, -1)
#     except Exception as e:
#         print("[{}] {}".format(e.__class__.__name__, e))
        