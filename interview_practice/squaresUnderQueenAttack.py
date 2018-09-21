

# queen_can_go = set()

# def diagonal_top_left_right(row, col, n):
#     i = row
#     j = col
#     while i >= 0 and i < n and j >= 0 and j < n:
#         queen_can_go.add(str(i)+ '-'+ str(j))
#         j+=1
#         i -= 1
#     i = row
#     j = col
#     while i >= 0 and i < n and j >= 0 and j < n:
#         queen_can_go.add(str(i) + '-' + str(j))
#         i-=1
#         j-=1

# def diagonal_down_left_right(row, col, n):
#     i = row
#     j = col
#     while i >= 0 and i < n  and j >= 0 and j < n:
#         queen_can_go.add(str(i)+'-'+ str(j))
#         i+=1
#         j-=1
#     i = row
#     j = col
#     while i >= 0 and i < n and j >= 0 and j < n:
#         queen_can_go.add(str(i)+'-'+ str(j))
#         i+=1
#         j+=1

# def add_queen(row, col, n):

#     for i in range(n):
#         #horizontal
#         queen_can_go.add(str(row)+ '-'+ str(i))
#         #vertical
#         queen_can_go.add( str(i)+ '-' + str(col))
#     # digonal
#     diagonal_top_left_right(row, col, n)
#     diagonal_down_left_right(row, col, n)





def squaresUnderQueenAttack(n, queens, queries):

    arr_res = []
    set_x = set()
    set_y = set()
    set_diag1 = set()
    set_diag2 = set()
    for qu in queens:
        set_x.add(qu[0])
        set_y.add(qu[1])
        set_diag1.add(qu[0] + qu[1])
        set_diag2.add(qu[0] - qu[1])

        
    for q in queries:
        if (q[0] in set_x or  
            q[1] in set_y or 
            (q[0] + q[1] ) in set_diag1 or
            (q[0] - q[1]) in set_diag2):
            arr_res.append(True)
        else:
            arr_res.append(False)

    return arr_res
