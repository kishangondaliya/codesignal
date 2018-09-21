def sortByString(s, t):
    r = ''
    for e in t:
        for n in s:
            if n == e:
                r += n
    
    return r
