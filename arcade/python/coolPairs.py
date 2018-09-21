def coolPairs(a, b):
    uniqueSums = {e+f for e,f in [(bb,aa) for bb in b for aa in a if ((aa * bb) % (aa + bb)) == 0 ]}
    return len(uniqueSums)
