for number in range(1, 10):
    # if number == int(str(number)[::-1]):
        print('{:02d}'.format(number), end=", ")
    
for number in range (11, 89):
    # for numbers above 11, divide by 10 and print only 
    # items with decimal point greater than zero, hence eliminating 20, 30, 40 etc.

    if (int(str(number/10).split('.')[1])) > 0:
        print('{:02d}'.format(number), end=", ")
print(89)
