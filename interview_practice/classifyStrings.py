def check_voyels_and_mixed(s, ret):
    voyels = ["a", "e", "i", "o", "u"]
    nb_v = 0
    nb_s = 0
    nb_c = 0
    for i in range(0, len(s)-2):
        print(s[i:i + 3])
        for v in s[i:i+3]:
            if v in voyels:
                nb_v += 1
            if v == '?':
                nb_s += 1

        if nb_v == 3:
            ret.append("bad")
        if nb_s + nb_v == 3:
            ret.append("mixed")
        if nb_c == 5:
            return "bad"
        nb_s = 0
        nb_v = 0
    return ret
    
def check_consone_and_mixed(s, ret):
    voyels = ["a", "e", "i", "o", "u"]
    nb_s = 0
    nb_c = 0
    for i in range(0, len(s)-4):
        print(s[i:i + 5])
        for v in s[i:i+5]:
            if v not in voyels and v !='?':
                nb_c += 1
            if v == '?':
                nb_s += 1
        if nb_c == 5:
            ret.append("bad")
        if nb_s + nb_c == 5:
            ret.append("mixed")
        nb_s = 0
        nb_c = 0
    return ret
    

def check_edge_case(s, ret):
    import re
    group = re.findall(r"([aeiou]{2}[\\?]{1}[^aeiou]{4})", s)
    if group:
        ret.append('bad')
    print("group1:",group )
    group3 = re.findall(r"([aeiou]{2}[\\?]{1}[^aeiou]{4})", s)
    if group3:
        ret.append('bad')

            
    return ret
    
def classifyStrings(s):
    ret = []
    voyels = ["a", "e", "i", "o", "u"]
    nb_s = 0
    nb_v = 0
    if len(s) < 3:
        return "good"
    if len(s) == 3:
        for v in s[0:3]:
            if v in voyels:
                nb_v += 1
            if v == '?':
                nb_s += 1
        if nb_v ==3:
            ret.append("bad")
        if nb_v + nb_s == 3:
            ret.append("mixed")
        
    ret = check_voyels_and_mixed(s,ret)
    ret = check_consone_and_mixed(s,ret)
    ret = check_edge_case(s, ret)
    
    if ret and "bad" in ret:
        return "bad"
    if ret and "mixed" in ret:
        return "mixed"
    return "good"
