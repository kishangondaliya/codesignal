def mirrorBits(a):
    m =  bin(a)[2:]
    return int(m[::-1],2)
