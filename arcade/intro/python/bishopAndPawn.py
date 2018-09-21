

def up_right(l, bishop):
    b = bishop[0]
    d = bishop[1]
    e = int(d)
    arr = []
    if d == '8':
        return []
    f = ""
    for i in l[l.index(b)+1:]:
        e += 1
        f = i + str(e) 
        arr.append(f)
    return arr
    
    
def down_right(l, bishop):
    b = bishop[0]
    d = bishop[1]
    e = int(d)
    arr = []
    f = ""
    if d == '1':
        return []
    for i in l[l.index(b)+1:]:
        if e == 0:
            break
        e -= 1
        f = i + str(e) 
        arr.append(f)
    return arr

def down_left(l, bishop):
    b = bishop[0]
    d = bishop[1]
    e = int(d)
    arr = []
    if d == '1':
        return []
    f = ""
    l = l[:l.index(b)]
    l = l[::-1]
    for i in l:
        e -=1
        if e == 0:
            break
        f =  i + str(e)
        arr.append(f)
    return arr

def up_left(l, bishop):
    b = bishop[0]
    d = bishop[1]
    e = int(d)
    arr = []
    if d == '8':
        return []
    f = ""
    l = l[:l.index(b)]
    l = l[::-1]
    for i in l:
        e +=1
        if e == 0:
            break
        f =  i + str(e)
        arr.append(f)
    return arr



def bishopAndPawn(bishop, pawn):
    l = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h']
    u_r = up_right(l, bishop)
    if pawn in u_r:
        return True
    d_r = down_right(l, bishop)
    if pawn in d_r:
        return True
    u_l = up_left(l, bishop)
    if pawn in u_l:
        return True
    d_l = down_left(l, bishop)
    if pawn in d_l:
        return True
    return False
    
    

