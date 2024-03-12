"""
A function to check if the object is an instance of a class

Called using is_same_class(objName, className), and passing
two  (2) seperate arguments to represent the obj and the class
to be checked
"""

def inherits_from(objName, className):

    """
    A function uses an issubclass within an if statement
    to check if the object is an instance of a class

    It passes the arrguments of for the parameters (objName, className), 
    which represent the obj and the class to be checked
    """
    
    if issubclass(objName, className):
        return True
    else:
        return False
    
    
    