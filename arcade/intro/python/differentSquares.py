
def find_all_around(row, column, matrix):
    arr = []
    try:
        c = matrix[row][column]
        d = matrix[row + 1][column]
        r = matrix[row][column + 1]
        dr = matrix[row + 1][column + 1]
        return [c, r, d, dr]
    except IndexError:
        pass
    
def differentSquares(matrix):
    row = 0
    arr = []
    while row < len(matrix):
        column = 0
        while column < len(matrix[row]):
            arr.append(find_all_around(row, column, matrix))
            column += 1     
        row += 1
    a = set(tuple(element) for element in arr if element is not None)
    return len(a)
