def adjacentElementsProduct(inputArray):
    if len(inputArray) == 2:
        return inputArray[0] * inputArray[1]
    i = 1
    max_sum = inputArray[0] * inputArray[1]
    while i < len(inputArray):
        sum = inputArray[i] * inputArray[i-1]
        print("Sum:", sum)
        if sum > max_sum:
            max_sum = sum
        i+=1
    return max_sum
