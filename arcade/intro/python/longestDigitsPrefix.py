def longestDigitsPrefix(inputString):
    i = 0
    arr = []
    s = ""
    if ' ' in inputString:
        return "".join([])
    while i < len(inputString):
        if inputString[i].isdigit():
            s += inputString[i]
        else:
            arr.append(s)
            s = ""
        i+=1
    arr.append(s)
    a = [i for i in arr if i !='']
    a.sort(key=len, reverse=True)
    try:
        return a[0]
    except:
        return  "".join([])
