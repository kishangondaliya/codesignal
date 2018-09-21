def replaceMiddle(arr):
    if len(arr) % 2 == 0:

        return arr[:(len(arr)-1)//2] + [ arr[(len(arr)-1)//2] +  arr[((len(arr)-1)//2)+1] ] + arr[((len(arr)-1)//2)+2:]
    else:
        return arr
    return arr
