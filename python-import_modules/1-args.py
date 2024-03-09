import sys

def dynamic_argv(*argv):
    return argv, len(*argv)

# receive arguments from commandline
argv = sys.argv

# use dynamic as the store to keep returned value from the function - dynamic_argv
# always put the var name in the parentheses -  values where applicable, else response is null
dynamic = dynamic_argv(argv)

'''
the function returns 2 values seperated by a comma

1. at index 0 is the list of arguments recieved from
 the command line or anywhere

2. at index 1 is the number of the total arguments entered

BELOW, WE WOULD BE PICKING OUR CHOICE AND SAVING THEM IN 
SEPARATE STORAGE CONTAINERS

SEPERATING THE list of received arguments and the the 
total number of arguments recieved
'''

# variable to hold the list of arguments
listOfArguments = dynamic[0]

# variable to hold number of arguments entered
lengthOfArguments = dynamic[1] - 1
'''subtract one because by default the name of our 
file/script is added to the list as an argument so we 
subtract one to match the actual number of arguments 
entered'''

print("{} arguments".format(lengthOfArguments))

# loop to print the arguments and corresponding number
count = 1
while count <= lengthOfArguments:
    print("{}: {}".format(count, listOfArguments[0][count]))
    count = count + 1

if __name__ == "__main__":
