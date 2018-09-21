def makeArrayConsecutive2(statues):
    s = sorted(statues)
    
    i = min(s) 
    arr = []
    while i < max(s):
        if i not in s:
            arr.append(i)
        i += 1
    return len(arr)
        
    
