def isInfiniteProcess(a, b):
    if a > b:
        return True
    if b - a == 1:
        return True
    if (b - a) % 2 == 0:
        return False
    else:
        return True
    
    return False
