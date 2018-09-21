
def check_pos(s1,s2):
    print("s1, s2", s1, s2)
    if s1 == 180 and s2 == -180:
        return True
    if s1 == -180 and s2 == 180:
        return True
    if s1 == 0 and s2 == 360:
        return True
    if s1 == 360 and s2 == 0:
        return True
    if s1 ==  0 and s2 == 0:
        return True 
    if s1 ==  180 and s2 == 180:
        return True 
    if s1 % 180 == 0 and s2 % 180 == 0:
        return True
    return False
    

def lineUp(commands):
    s1 = 0
    s2 = 0
    i = 0
    res = 0
    for c in commands:
        if c == 'L':
            s1 -= 90
            s2 += 90
        if c == 'R':
            s1 += 90
            s2 -= 90
        if c == 'A':
            s1 += 180
            s2 += 180
        if check_pos(s1, s2):
            res += 1
        i += 1
                
    return res
