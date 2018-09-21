def higherVersion2(ver1, ver2):
    vs1 = ver1.split('.')
    vs2 = ver2.split('.')

    for v1, v2 in zip(vs1, vs2):
        print(v1,v2)
        if int(v1) > int(v2):
            return 1
        if int(v2) > int(v1):
            return -1
        
        
    return 0
