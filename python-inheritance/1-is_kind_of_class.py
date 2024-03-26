"""
A function to check if the object is an instance of a class

Called using is_same_class(objName, className), and passing
two  (2) seperate arguments to represent the obj and the class
to be checked
"""

def is_kind_of_class(objName, className):

    """
    A function uses an isinstance within an if statement
    to check if the object is an instance of a class

    It passes the arrguments of for the parameters (objName, className), 
    which represent the obj and the class to be checked
    """
    
    return isinstance(objName, className)
    

# a = 1
# if is_kind_of_class(a, int):
#     print("{} comes from {}".format(a, int.__name__))
# if is_kind_of_class(a, float):
#     print("{} comes from {}".format(a, float.__name__))
# if is_kind_of_class(a, object):
#     print("{} comes from {}".format(a, object.__name__))