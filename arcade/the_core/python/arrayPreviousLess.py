def arrayPreviousLess(items):
    arr = []
    for i, e in enumerate(items):
        temp = -1
        if len(items[:i]):
            z = len(items[:i]) -1
            while z >= 0:
                if items[:i][z] < e:
                    temp = items[:i][z]
                    break
                z -=1
                
        arr.append(temp)
    return arr
            
                
                
