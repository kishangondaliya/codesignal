# TE
def calkinWilfSequence(number):
    def fractions():
        num = [[1,1]]
        while len(num):
            r = num.pop(0)
            yield r 
            a,b = r
            num.append([a, (a+b)])
            num.append([(a+b), b])
            
    gen = fractions()
    res = 0
    while next(gen) != number:
        res += 1
    return res

def calkinWilfSequence(number):
    def fractions():
        n = 1
        d = 1
        yield [n, d]
        while True:
            n, d = d, 2 * (n // d) * d + d - n
            yield [n, d]
            
    gen = fractions()
    res = 0
    while next(gen) != number:
        res += 1
    return res
