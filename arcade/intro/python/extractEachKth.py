def extractEachKth(inputArray, k):
    del inputArray[k-1::k]
    return inputArray

