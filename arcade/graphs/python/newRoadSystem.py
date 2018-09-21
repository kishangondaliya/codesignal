def newRoadSystem(roadRegister):
    total_in = {}
    for i, value in enumerate(roadRegister):
        print(i, value)
        ct = 0
        for pos, j in enumerate(value):
            if j:
                ct +=1
        total_in[i] = ct
    total_out = {}
    row = 0
    cnt = 0
    while row < len(roadRegister):
        col = 0
        cnt = 0
        while col < len(roadRegister):
            if roadRegister[col][row]:
                cnt += 1
            col += 1
        total_out[row] = cnt
        row += 1
    if total_in != total_out:
        return False
        
    return True
