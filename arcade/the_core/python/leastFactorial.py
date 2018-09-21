def leastFactorial(n):
    fac = 1
    i = 1
    while fac < n:
        fac *= i
        i +=1
    return fac
