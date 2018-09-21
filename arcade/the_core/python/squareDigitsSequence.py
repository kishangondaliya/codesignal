def squareDigitsSequence(a0):
    s = str(a0)
    arr = map(int, s)
    count = 1
    res = 0
    prev = res
    dic = set()
    while res != a0:
        res = sum((e*e for e in arr))
        arr = map(int, str(res))
        count += 1 
        if res in dic:
            break
        else:
            dic.add(res)
        if prev == res:
            break
        prev = res
    return count
