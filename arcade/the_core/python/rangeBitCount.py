def rangeBitCount(a, b):
    res = []
    while a <= b:
        res.append(bin(a)[2:])
        a += 1
    r = 0
    for e in "".join(res):
        print(int(e))
        r += int(e)
    return r
