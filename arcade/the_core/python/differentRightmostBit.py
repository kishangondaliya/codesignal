def differentRightmostBit(n, m):
    return 2 ** [i for i, e in enumerate(bin(n ^ m)[2:][::-1]) if e == '1'][0]


#2 ** [ n  for n, e in enumerate(zip(bin(n)[2:][::-1], bin(m)[2:][::-1])) if e[0]  != e[1]  ][0] if len([ n  for n, e in enumerate(zip(bin(n)[2:][::-1], bin(m)[2:][::-1])) if e[0]  != e[1]  ]) else 1
