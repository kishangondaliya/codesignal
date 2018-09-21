def findEmailDomain(address):
    a = re.search(r'@[\w.]+$', address)
    return a.group()
