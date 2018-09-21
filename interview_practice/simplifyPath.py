def simplifyPath(path):
    arr = path.split('/')
    res = []
    for e in arr:
        if e == '' or e == '.':
            pass
        elif e == '..':
            if len(res) > 0:
                res.pop()
        else:
            res.append(e)
    if len(res) == 0:
        return '/'

    return "/"+'/'.join(res)
