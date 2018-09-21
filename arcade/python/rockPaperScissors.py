from itertools import permutations

def rockPaperScissors(players):
    return sorted(set([ i[0:2]  if len(i) > 2 else i for i in list(permutations(players))]))
