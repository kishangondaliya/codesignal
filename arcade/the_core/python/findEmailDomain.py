def findEmailDomain(address):
    pos = address.rfind('@')
    if pos <= 0:
        raise Exception("Invalid")
    return address[pos + 1:]

