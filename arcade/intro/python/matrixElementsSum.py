def matrixElementsSum(matrix):
    i = 0
    while i < len(matrix):
        i+=1
    nb_of_rows = i
    print("NbofRows:", nb_of_rows)
    nb_columns =0
    for j in matrix[0]:
        nb_columns += 1
    print("nb_colums:", nb_columns)
    for j in range(nb_columns):
        for i in range(nb_of_rows):
            print(matrix[i][j])
