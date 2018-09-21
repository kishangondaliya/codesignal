def reverseInteger(x):
    my_stack = []
    neg = False
    res = ""
    if x < 0:
        neg = True
        x = str(x)
        x = x[1:]
        
    x = str(x)
    for e in x:
        my_stack.append(e)
    while my_stack:
        res += my_stack.pop()
    if neg is True:
        return int(res) * -1
    return int(res)
