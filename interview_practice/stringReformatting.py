def stringReformatting(s, k):
    s = s.replace('-','')
    s_l = len(s) -1
    i = 0
    new_str = []
    while s_l >= 0:
        if i == k:
            i = 0
            new_str.insert(0, '-')
        new_str.insert(0, s[s_l])
        i += 1
        s_l -= 1
    return "".join(new_str)
