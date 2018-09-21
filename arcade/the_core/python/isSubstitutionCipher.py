


def isSubstitutionCipher(string1, string2):
    dic = {}
    for e in string1:
        if e in dic:
            dic[e] += 1
        else:
            dic[e] = 1
            
    d2 = {}
    for e in string2:
        if e in d2:
            d2[e] += 1
        else:
            d2[e] = 1

    if len(dic.keys()) != len(d2.keys()):
        return False
    
    new_d = {}
    for e, g in zip(string1, string2):
        if e not in new_d:
            new_d[e] = g
        else:
            f = new_d.get(e, None)
            print("f:", f)
            if f != g:
                return False

    
    return True
