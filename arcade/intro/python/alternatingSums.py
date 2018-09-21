def alternatingSums(a):
    t1 = 0
    t2 = 0
    for i, e in enumerate(a):
        if i % 2 == 0:
            t1 += e
        else:
            t2 += e
    return [t1,t2]
