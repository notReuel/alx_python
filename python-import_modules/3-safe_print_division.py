
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

if __name__ == "__main__":
    print("{:d} / {:d} = {}".format(a, b, safe_print_division(a, b)))