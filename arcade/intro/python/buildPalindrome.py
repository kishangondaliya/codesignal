# 1-find longest palindrome at the end
# not found all reverse
# else from i to begin

def is_palindrome(s):
    if s == s[::-1]:
        return True
    return False
    
def buildPalindrome(st):
    
    if st == st[::-1]:
        return st

    s = st[::-1]
    i = 0
    arr = []

    while i < len(s):
        if is_palindrome(s[0:i]):
            arr.append(s[0:i])
        i += 1
    max_p =  max(arr)
    if len(max_p) > 1 :
        max_p =  max(arr)
        print(max_p)
        n = len(s)-len(max_p)
        s2 = st[:n]
        s2 = s2[::-1]
        return (st + s2)
    else:
        a =  st[:-1]
        r = st + a[::-1]
        return r

