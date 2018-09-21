def arrayMaxConsecutiveSum2(inputArray):
    if len(inputArray) == 1:
        return inputArray[0]
    
    max_in = 0
    max_here = inputArray[0]
    
    for i in inputArray:
        max_in += i
        if max_in < i:
            max_in = i
        if max_in > max_here:
            max_here = max_in 
            
            
    return max_here
