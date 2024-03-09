def raise_exception(a, b):
    raise TypeError("Exception has been raised")    
    
try:
    raise_exception()
except TypeError as te:
    print("Exception raised")
