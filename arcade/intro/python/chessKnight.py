
def valid(cell):
    if len(cell)> 2:
        return False
    try:
        if cell[0] not in ['a', 'b', 'c','d','e','f','g','h']:
            return False
        if int(cell[1]) not in [ i for i in range(1,9)]: 
            return False
    except:
        return False
    return True

def chessKnight(cell):
    a = 0
    if not valid(cell):
        return 0
    up = chr(ord(cell[0]) + 1) + str((int(cell[1]) + 2))
    if valid(up):
        a += 1
    upr = chr(ord(cell[0])+2) + str((int(cell[1]) + 1))
    if valid(upr):
        a += 1
    r = chr(ord(cell[0])+2) + str((int(cell[1]) - 1))
    if valid(r):
        a += 1
    dr = chr(ord(cell[0])+1) + str((int(cell[1]) - 2))
    if valid(dr):
        a += 1
    d = chr(ord(cell[0])-1) + str((int(cell[1]) - 2))
    if valid(d):
        a += 1
    dl = chr(ord(cell[0])-2) + str((int(cell[1]) -1))
    if valid(dl):
        a += 1
    ul = chr(ord(cell[0])-2) + str((int(cell[1]) + 1))
    if valid(ul):
        a += 1
    upl = chr(ord(cell[0])-1) + str((int(cell[1]) + 2))
    if valid(upl):
        a += 1
    return a
