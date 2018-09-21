def isTandemRepeat(inputString):
    if len(inputString) % 2 != 0:
        return False
    else:
        mid =  len(inputString) // 2
        #print(inputString[mid:] + "-" + inputString[:mid])
        return inputString[mid:] == inputString[:mid]
