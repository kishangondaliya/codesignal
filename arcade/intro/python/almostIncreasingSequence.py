def almostIncreasingSequence(sequence):
    inc = False
    nb = 0
    while not inc:
        if nb > 1:
            return False
        inc = True
        i = 0
        while i < len(sequence)-1:
            if sequence[i] > sequence[i+1]:
                inc = False
                try:    
                    if sequence[i] < sequence[i+2]:
                        del sequence[i+1]
                        nb += 1
                        break
                except:
                    pass
                try:    
                    if (i == len(sequence)-2) and sequence[i] > sequence[i+1]:
                        del sequence[i+1]
                        nb += 1
                        break
                except:
                    pass
                del sequence[i]
                nb += 1
                break
            elif sequence[i] == sequence[i+1]:
                inc = False
                del sequence[i]
                nb +=1
                break
            else:
                inc = True
            i += 1
    if nb > 1:
        return False
    return True
