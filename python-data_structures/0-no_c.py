def no_c(my_string):
    result = ""
    for char in my_string:
        if char != 'C' and char != 'c':
            result += char
    return result
    
# print(no_c("Holberton School"))
# print(no_c("Chicago"))
# print(no_c("C is fun!"))