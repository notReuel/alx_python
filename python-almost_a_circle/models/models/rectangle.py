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
    
# if __name__ == "__main__":

#     r1 = Rectangle(10, 2)
#     print(r1.id)
    

#     r2 = Rectangle(2, 10)
#     print(r2.id)

#     r3 = Rectangle(10, 2, 0, 0, 12)
#     print(r3.id)   
    
    
    