from collections import OrderedDict

def firstNotRepeatingCharacter(s):
    al = OrderedDict()
    for e in s:
        if e in al:
            al[e] += 1
        else:
            al[e] = 0
    
    for k, v in al.items():
        if v == 0:
            return k

    return '_'
