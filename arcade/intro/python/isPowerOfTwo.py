def isPowerOfTwo2(n):
    a = bin(int(n)) 
    v = str(a[2:])
    i = 0
    while i < len(v):
        if i == 0:
            if v[0] != '1':
                return False
        elif v[i] != '0':
            return False
        i += 1
    return True

