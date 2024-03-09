def square_matrix_simple(matrix=[]):
    
    newMatrix = []
    
    for row in matrix:
        itemRow = []
        for item in row:
            #items = item**2
            itemRow.append(item**2)
                
        newMatrix.append(itemRow)
            
    return newMatrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


if __name__ == "__main__":
    new_matrix = square_matrix_simple(matrix)

    print(new_matrix)
    print(matrix)
