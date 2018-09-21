from functools import lru_cache

@lru_cache(maxsize=100)
def get_sum(num):
    n = [int(e) for e in str(num)]
    return sum(n)

@lru_cache(maxsize=100)
def is_comfortable(a, b):
    if a == b:
        return False
    return a - get_sum(a) <= b and b <= a + get_sum(a)


def comfortableNumbers(l, r):
    res = 0
    for i in range(l, r+1):
        for j in range(i+1, r+1):
            if is_comfortable(i,j) and is_comfortable(j,i):
                res +=1
    return res
        
        
