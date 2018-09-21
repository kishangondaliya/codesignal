import re
def increaseNumberRoundness(n):
    if re.match(r'[1-9]+[0]+[1-9]+', str(n)):
        return True
    return False
