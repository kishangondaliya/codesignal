def additionWithoutCarrying(param1, param2):
    
    l1 = str(param1)
    l2 = str(param2)
    if len(l1) < len(l2):
        l1 = l1.zfill(len(l1) + (len(l2) - len(l1)))
    if len(l1) > len(l2):
        l2 = l2.zfill(len(l2) + (len(l1) - len(l2)))
    
    res = []
    for i, j in zip(l1,l2):
        print(i, j)
        res.insert(0, str(int(i) + int(j))[::-1][0])
    return int("".join(res[::-1]))
    
