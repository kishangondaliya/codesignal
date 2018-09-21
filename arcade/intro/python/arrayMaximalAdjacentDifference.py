def arrayMaximalAdjacentDifference(inputArray):
    i = 1
    max = 0
    while i < len(inputArray):
        r = inputArray[i-1] - inputArray[i]
        if r < 0:
            r *= -1
        if r > max:
            max = r
        i += 1
    return max
