def remove_char(s, n):  
    f = s[:n]   
    l = s[n+1:]
    return f + l

def deleteDigit(n):
    arr = []
    n = str(n)
    for i,j in enumerate(n):
        arr.append(remove_char(n,i))
    print(arr)
    a = map(int, arr)
    return max(a)
