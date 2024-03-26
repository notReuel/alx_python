"""
A function to check if the object is an instance of a class

Called using is_same_class(objName, className), and passing
two  (2) seperate arguments to represent the obj and the class
to be checked
"""

def is_same_class(objName, className):

    """
    A function uses an isinstance within an if statement
    to check if the object is an instance of a class

    It passes the arrguments of for the parameters (objName, className), 
    which represent the obj and the class to be checked
    """
    
    return (type(objName) == className)
    

