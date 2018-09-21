
cache = {}
cache[1] = 1
cache[2] = 2
cache[3] = 3

def climbingStairs(n):
    if n == 1:
        return 1
    if n < 0:
        return 0
    if n == 1:
        return 0
    if n in cache:
        return cache[n]
    else:
        cache[n] =  climbingStairs(n-1) + climbingStairs(n-2)
        return cache[n]
    return cache[n]
