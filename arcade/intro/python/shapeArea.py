def shapeArea(n):
    res =  1
    fac = 4
    i = 1
    if n == 1:
        return 1
    while i < n:
        res += fac
        i += 1
        fac += 4
    return res
