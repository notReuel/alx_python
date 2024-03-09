def is_prime(number):
    #prime number formula
    checkValid = False
    for div in range(2, number):
        # print(div, end=", ")
        # quite tricky, if you modulo a number by numbers between 2
        # and the number and anyone is equall zero, flag it
        # this is the best way to make it work
        # else your brain go just dey fire

        if number % div <= 0:
            checkValid = False
            break
        else : 
            checkValid = True
    return checkValid
        
print(is_prime(17))
print(is_prime(15))
print(is_prime(-4))
print(is_prime(0))