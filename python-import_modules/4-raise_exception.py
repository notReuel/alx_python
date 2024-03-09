def raise_exception():
    sum = "a" + 1
    return sum    
    
    
try:
    raise_exception()
except TypeError as te:
    print("Exception raised")
