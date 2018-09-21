def isSumOfConsecutive2(n):
    res = 0
    for j in range(1,n):
        i = j
        total = 0
        while i < n:
            total += i
            if total == n:
                res += 1
            if total > n:
                break
            i += 1

    return res
