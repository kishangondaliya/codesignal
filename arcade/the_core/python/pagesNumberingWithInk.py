

def pagesNumberingWithInk(current, numberOfDigits):
    digit_cur = len(str(current))
    res = 0
    while numberOfDigits >= digit_cur:
        numberOfDigits -= digit_cur
        res +=1
        current += 1
        digit_cur = len(str(current))
    return current -1
