
def until_last_paranthesis_number(s):
    i = s.rfind('(')
    if i == -1:
        return s
    else:
        return s[:i]


def get_number_inside_partenthesis(s):
    i = s.rfind('(')
    j = s.rfind(')')
    return int(s[i+1:j])


def add_in_array(d_r, r):
    if '(' in r:
        v = until_last_paranthesis_number(r)
        n = get_number_inside_partenthesis(r)
        if v in d_r:
            d_r[v] = d_r[v] + [n]
        else:
            d_r[v] = [n]
    else:
        if r in d_r:
            d_r[r] = d_r[r] + [0]
            return d_r
        d_r[r] = [0]
    return d_r


def return_min(d_r, v):
    i = 0
    if '(' in v:
        i = 1
    while 1:
        if i in d_r[v]:
            i += 1
        else:
            break

    d_r[v] = d_r[v] + [i]
    return d_r, i


def fileNaming(names):
    arr = []
    d_r = {}
    for e in names:

        if e in arr:
            if '(' in e:
                print("-------")
                if e not in d_r:
                    d_r[e] = [1]
                    arr.append(e + "(1)")
                    continue
            d_r, v = return_min(d_r, e)
            print("dr:",d_r)
            arr.append(e + "({})".format(v))
        else:
            arr.append(e)
            d_r = add_in_array(d_r, e)
        print(arr)
        print(d_r)
    return arr
