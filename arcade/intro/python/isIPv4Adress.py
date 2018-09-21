def isIPv4Address(inputString):
    arr = inputString.split('.')
    if len(arr) != 4:
        return False
    for e in arr:
        try:
            if int(e) >= 0 and int(e) <= 255:
                pass
            else:
                return False
        except:
            return False
    return True
