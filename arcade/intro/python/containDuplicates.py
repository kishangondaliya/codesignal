def containsDuplicates(a):
    dic = {}
    for e in a:
        if e in dic:
            return True
        else:
            dic[e] = True
    return False
