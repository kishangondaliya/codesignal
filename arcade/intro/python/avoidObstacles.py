def avoidObstacles(inputArray):
    arr = sorted(inputArray)
    i = 0
    found = False
    my_gap = 0
    while not found:
        my_gap += 1
        found = True
        i = 0
        j = 0
        while i <= arr[len(arr)-1]:
            if i in arr:
                found = False
                break
            i += my_gap
            j += 1
        if found:
            return my_gap
