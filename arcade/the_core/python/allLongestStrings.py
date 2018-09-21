def allLongestStrings(inputArray):
    max_len = max([len(e) for e in inputArray])
    return [e for  e in inputArray if len(e) == max_len]
