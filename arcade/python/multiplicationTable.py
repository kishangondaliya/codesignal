def multiplicationTable(n):
    return [[e*i for e in range(1,n+1)] for i, e in enumerate(range(1,n+2)) if i != 0]
