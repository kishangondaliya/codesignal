class Functions(object):
    def __init__(self):
        pass
    
    @staticmethod
    def sign(x):
        if x == 0:
            return 0
        if x > 0:
            return 1
        return -1

def sign(x):
    return Functions.sign(x)
