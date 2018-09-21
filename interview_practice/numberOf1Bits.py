def numberOf1Bits(n):
    a = bin(n)
    a = a[2:]
    res = 0
    for e in str(a):
        print("e:",e)
        res += int(e)
    return res
