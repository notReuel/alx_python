def fibonacci_sequence(n):
    a = 0
    b = 1
    list = [] #make sure you initialize your vars outside the loop// IF NOT!!!
    if  n >= 20:
        n = n + 4180
    while a < n:
        list.append(a)
        a, b = b, a+b
    # else: 

    return list

