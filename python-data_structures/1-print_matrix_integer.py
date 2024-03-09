def print_matrix_integer(matrix=None):
    if matrix is None:
        print("$")
        return
    
    if isinstance(matrix, str):   #If input is a string, just print it
        print("{}$".format(matrix))
        return
    
    for row in matrix:
        formattedRow = ' '.join(str(item) for item in row)
        print("{}$".format(formattedRow))

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
if __name__ == "__main__":
    print_matrix_integer(matrix)
    print_matrix_integer("--")
    print_matrix_integer()