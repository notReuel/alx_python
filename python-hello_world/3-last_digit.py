import random
number = random.randint(-10000, 10000)

# Convert the number to a string

lastDigitCast = str(number)
# create an empty list
lastDigitList = []

# a for loop to iterate over the content of the string
# ...and save them as items in the list we created
for x in lastDigitCast:
    lastDigitList.append (x) 

# pick the last item on the list and save it in this variable
# use -1 as we are not sure of how many digit number will be generated.
lastDigit = (lastDigitList[-1])

# print(number)

if number < 0:
    lastDigit = '-' + lastDigit
    # print(lastDigit)

# convert the last item we saved from string back to an integer
intLastDigit = int(lastDigit)




# print(intLastDigit)



#an if statement to print the required output
if intLastDigit > 5:
    print('Last digit of {} is {} and is greater than 5'.format(number, lastDigit, ))
elif intLastDigit < 6 and intLastDigit < 0:
    print('Last digit of {} is {} and is less than 6 and not 0'.format(number, lastDigit))
elif intLastDigit == 0:
    print('Last digit of {} is {} and is 0'.format(number, lastDigit))

