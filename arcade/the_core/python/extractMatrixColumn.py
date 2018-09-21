def extractMatrixColumn(matrix, column):
    res = []
    for i in range(len(matrix)):
        res.append(matrix[i][column])
    return res
        
