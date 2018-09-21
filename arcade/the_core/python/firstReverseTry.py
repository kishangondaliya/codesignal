def firstReverseTry(arr):
    if len(arr) == 1:
        return arr
    return arr[-1:]  + arr[1:len(arr)-1] + arr[:1] 
