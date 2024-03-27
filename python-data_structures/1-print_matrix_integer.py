def print_matrix_integer(matrix=[[]]):
    if not any(matrix):
        print()
        return
    for i in range(len(matrix)):
        for j in range(len(matrix[i]-1)):
            print("{:d}".format(matrix[i][j]), end=" ")
        print("{:d}".format(matrix[i][-1]))
    

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

