

def replace_in(n):
    s = ""
    for e in n:
        if e in string.ascii_letters:
            s += e
        else:
            s += ' '
    return s

def longestWord(text):
    s = replace_in(text)
    arr = s.split()
    print(arr)
    return max(arr, key=len)
