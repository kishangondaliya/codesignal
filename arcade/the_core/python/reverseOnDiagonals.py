def reverseOnDiagonals(matrix):
    
    diag_left = []
    diag_right = []
    z = len(matrix)-1
    for i in range(len(matrix)):
        diag_left.append(matrix[i][i])

    i = 0
    while z >= 0:

        diag_right.append(matrix[z][i])
        z -=1
        i +=1 
    diag_left = list(reversed(diag_left))
    diag_right = list(reversed(diag_right))
        
    z = len(matrix)-1
    for i in range(len(matrix)):
        matrix[i][i] = diag_left[i]

    i = 0
    while z >= 0:

        matrix[z][i] = diag_right[i]
        z -=1
        i +=1 
        
    return matrix
