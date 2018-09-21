def sumOfTwo(a, b, v):
    dica = {}
    dicb  = {}
    for e in b:
        dicb[e] = 1
    for e in a:
        if (v-e) in dicb:
            return True
    return False
