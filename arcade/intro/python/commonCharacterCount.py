def commonCharacterCount(s1, s2):
    d1 = {}
    d2 = {}
    for i in set(s1):
        d1[i] = s1.count(i)
    for i in set(s2):
        d2[i] = s2.count(i)

    sum = 0
    for k,v in d1.items():
        if k in d2:
            a = min(d1[k], d2[k])
            sum += a
    return sum
