def create_dic(s):
    dic  = {}
    for e in s:
        if e not in dic:
            dic[e] = 1
        else:
            dic[e] += 1
    return dic

def constructSquare(s):
    l = len(s)
    res = []
    r = 0
    i = 0
    while len(str(r)) < len(s) + 1:
        r = i * i 
        if len(str(r)) == len(s):
            res.append(r)
        i += 1
    nn = set(s)
    m = -1
    
    dic_a = create_dic(s)
        

    for e in res:
        var = sorted(list(create_dic(str(e)).values()))
        z =  sorted(list(dic_a.values()))
        if z == var:
            if e > m:
                m = e
    
    return m
