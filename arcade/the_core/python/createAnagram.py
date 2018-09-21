

def createAnagram(s, t):

    s = list(s)
    t = list(t)
    
    for e in t:
        if e in s:
            s.remove(e)
    return len(s)
