# see http://blog.codefights.com/pressingbuttons-solution/
from itertools import product

def pressingButtons(buttons):
    numPad = [""   ,""    ,"abc","def" ,"ghi","jkl",
              "mno","pqrs","tuv","wxyz"]
    charArr = [numPad[int(digit)] for digit in buttons]
    return [''.join(s) for s in product(*charArr) if s]
