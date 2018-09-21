def makeArrayConsecutive2(statues):
    statues = sorted(statues)
    end = statues[len(statues)-1]
    print(end)
    i = statues[0]
    n = 0
    arr = []
    while i < end:
        if i == statues[n]:
            n += 1
        else:
            arr.append(i)
        i += 1
    return len(arr)
