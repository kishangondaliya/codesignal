def swapDiagonals(matrix):
    z = len(matrix) -1
    for i in range(len(matrix)):
        
        tmp = matrix[i][i]
        matrix[i][i] = matrix[i][z]
        matrix[i][z] = tmp
        z -=1
    return matrix
