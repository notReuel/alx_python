import sys
def length_arguments(*argv):  
    return argv, len(*argv)

#carries everything passed into the function, both list and number of arguments
# contentOfArgv = length_arguments(12, 50, 0)

# recieves content/arguments from the commandline
argv = sys.argv
contentOfArgv = length_arguments(argv)
# print(contentOfArgv)

# # targets the item on index 0 of the list = list of arguments
listOfArgv = contentOfArgv[0]
print(listOfArgv[0][2])
# # targets the item on index 1 of the list = length of arguments
lengthOfArgv = contentOfArgv[1]
print(lengthOfArgv)
# # prints the length of arguments
print("{} arguments".format(lengthOfArgv))

# # prints the list of arguments
# count = 0
# while count < lengthOfArgv:
#     print("{}: {}".format((count + 1), listOfArgv[count]))
#     count = count + 1