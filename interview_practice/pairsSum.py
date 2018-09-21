def pairsSum(a):
    i = 0
    ct = 0
    my_set = set(a)
    while i < len(a):
        j = i +1
        while j < len(a):
            if (a[i] + a[j]) in my_set:
                ct +=1
            j+=1
        i +=1
    return ct

