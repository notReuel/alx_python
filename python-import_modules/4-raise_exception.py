# def raise_exception():
#     raise TypeError("Exception has been raised")    
    
# try:
#     raise_exception()
# except TypeError as te:
#     print("Exception raised")

class MyCustomTypeError(Exception):
    pass

def raise_exception():
    raise MyCustomTypeError("Exception has been raised")

try:
    raise_exception()
except MyCustomTypeError as te:
    print("Exception raised:", te)