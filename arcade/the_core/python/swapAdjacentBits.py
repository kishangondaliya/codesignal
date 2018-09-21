def swapAdjacentBits(n):
    return int(''.join([ bin(n)[2:][x:x+2][::-1] for x in range(0, len(bin(n)[2:]), 2) ]),2) if len(bin(n)[2:]) % 2 == 0 else int(''.join([   str('0'+ bin(n)[2:])[x:x+2][::-1]  for x in range(0, len(bin(n)[2:])+1, 2) ]),2)
