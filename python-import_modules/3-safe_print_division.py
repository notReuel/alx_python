
def safe_print_division(a, b):
    try: 
        return a / b
    except: 
        if b != 0:
            result = 'None'
            return result
    finally:
        if b == 0:
            result = 'None'
        else: 
            result = a / b
        print("Inside result: {}".format(result))
        return result
        

a = 12
b = 6
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))