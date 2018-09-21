def validTime(time):
    if len(time)> 5:
        return False
    t = time.split(':')
    h = int(t[0])
    m = int(t[1])

    if h < 0 or h >= 24:
        return False
    if m < 0 or m > 59 :
        return False
    return True
