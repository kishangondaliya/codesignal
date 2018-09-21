def rounders(value):
    res = []
    prev = "None"
    for i, j in enumerate(str(value)[::-1]):
        n = int(j)
        if prev == "asc":
            if n == 9:
                n = 10
            else:
                n += 1
        if prev == "":
            print("do noth")
        if i == len(str(value))-1:
            res.insert(0, str(n))
            print("Last:", n)
        else:
            print("n:", n )
            if int(n) >= 5:
                res.insert(0, str(0))
                prev = "asc"
            if int(n) <= 4:
                res.insert(0, str(0))
                prev = ''
            if n == 0:
                prev = ''
    return int("".join(res))
