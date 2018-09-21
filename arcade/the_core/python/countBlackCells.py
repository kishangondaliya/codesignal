def countBlackCells(n, m):
    import math
    return n + m + math.gcd(n, m) -2
