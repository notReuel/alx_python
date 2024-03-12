"""
A function to check if the object is an instance of a class

Called using is_same_class(objName, className), and passing
two  (2) seperate arguments to represent the obj and the class
to be checked
"""

def is_same_class(objName, className):
    
    if isinstance(objName, className):
        return True
    else:
        return False
    