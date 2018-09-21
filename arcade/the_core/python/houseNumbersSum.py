def houseNumbersSum(inputArray):
    res = 0
    for e in inputArray:
        if e == 0:
            break
        res += e
    return res
