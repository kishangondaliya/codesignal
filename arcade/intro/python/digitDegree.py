def digitDegree(n):
    if n < 10:
        return 0
    t = 0
    while n >= 10:
        a = str(n)
        n = 0
        for e in a:
            n += int(e)
        t += 1
    return t

