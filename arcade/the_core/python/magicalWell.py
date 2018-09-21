def magicalWell(a, b, n):
    res = 0
    for i in range(n):
        res += a * b
        a +=1 
        b += 1
    return res
