from collections import Counter

def palindromeRearranging(inputString):
    cnt = Counter(inputString)
    pair = 0
    nb_not_pair = 0
    for k,v in cnt.items():
        if v % 2 == 0:
            pair += 1
        else:
            nb_not_pair += 1
    if pair > 0 and nb_not_pair == 0:
        return True
    if pair % 2 == 0 and nb_not_pair == 1:
        return True
    if nb_not_pair > 1:
        return False
    return False
