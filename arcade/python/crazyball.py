from itertools import combinations

def crazyball(players, k):
    return sorted([sorted(i) for i in list(combinations(players, k))])
