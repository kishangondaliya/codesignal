def isLucky(n):
    n = str(n)
    mid = len(n)//2
    l = n[0:mid]
    r = n[mid:]
    s1 = 0
    s2 = 0
    for e in l:
        s1 += int(e)
    for i in r:
        s2 += int(i)
    return s1 == s2
