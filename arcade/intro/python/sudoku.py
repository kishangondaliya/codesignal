

def check_horizontal(grid):
    s = {1,2,3,4,5,6,7,8,9}
    ex_sum = sum([i for i in range(1,10)])
    for e in grid:
        if set(e) != s:
            return False
        if ex_sum != sum(e):
            return False
    return True

def check_vertical(grid):
    s = {1,2,3,4,5,6,7,8,9}
    ex_sum = sum([i for i in range(1,10)])
    row = 9
    col = 9
    i = 0
    while i < col:
        j = 0
        arr = []
        while j < row:
            arr.append(grid[j][i])
            j+=1
        if set(arr) != s:
            return False
        if sum(arr) !=ex_sum:
            return False
        i+=1
    return True

def check_each_sub(grid):
    arr = []
    s = {1,2,3,4,5,6,7,8,9}
    ex_sum = sum([i for i in range(1,10)])
    for i in range(0,9,3):
        for j in range(0,9,3):
            arr.append([i,j])
    
    for r in arr:
        rec = []
        print(r)
        for i in range(3):
            for j in range(3):
                rec.append(grid[r[0]+i][r[0]+j])
        if sum(rec) != ex_sum:
            return False
        if set(rec) != s: 
            return False
    return True

def sudoku(grid):
    horiz = check_horizontal(grid)
    verti = check_vertical(grid)
    rec = check_each_sub(grid)
    return all([horiz,verti,rec])
