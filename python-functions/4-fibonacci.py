def fibonacci_sequence(n):
    a = 0
    b = 1
    list = [] #make sure you initialize your vars outside the loop// IF NOT!!!
    while a < n:
        list.append(a)
        a, b = b, a+b

    return list
    

print(fibonacci_sequence(6))
print(fibonacci_sequence(1))
print(fibonacci_sequence(0))
print(fibonacci_sequence(20))

