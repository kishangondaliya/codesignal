def checkPalindrome(inputString):
    if len(inputString) == 1:
        return True
    else:
        if inputString[0] == inputString[len(inputString)-1]:
            return checkPalindrome(inputString[1:-1])
    return False
