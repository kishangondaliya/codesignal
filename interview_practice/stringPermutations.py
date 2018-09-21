

def permutation(s):
    sec_max = -1
    for i in range(len(s)-1):
        if s[i] < s[i+1]:
            sec_max = i
    if sec_max == -1:
        return 'end'
    swap_to = -1
    for i in range(len(s)):
        if s[sec_max] < s[i]:
            swap_to = i
    if swap_to == -1:
        return "end"
    s[sec_max] , s[swap_to] = s[swap_to] , s[sec_max]
    s[sec_max+1:] = s[sec_max+1:][::-1]
    return s
    

def stringPermutations(s):
    s = sorted(s)
    res = ""
    arr = ["".join(s)]
    while res != 'end' or res != 'error':
        s = permutation(list(s))
        # print("s:", s)
        if s == 'end':
            break
        arr.append("".join(s))
    return arr
