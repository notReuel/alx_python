import random
number = random.randint(-10, 10)
# YOUR CODE HERE
if number > 0:
    print('{} is positive'.format(number))
elif number < 0:
    print('{} is negative\n'.format(number))
else:
    print('{} is zero\n'.format(number))
    
    