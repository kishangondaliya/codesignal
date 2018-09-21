def reflectString(inputString):
    a1 = "abcdefghijklm" 
    a2 = "nopqrstuvwxyz"[::-1]
    
    r = ""
    for i in inputString:
        if i in a1:
            p = a1.find(i)
            r += a2[p]
        if i in a2:
            p = a2.find(i)
            r += a1[p]
    return r
