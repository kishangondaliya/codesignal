import re

def isMAC48Address(inputString):
    if re.match("^([0-9A-Fa-f]{2}[-]){5}([0-9A-Fa-f]{2})$", inputString):
        return True
    return False
