def electionsWinners(votes, k):
    r = 0
    m = max(votes)
    for i in votes:
        if i + k > m:
            r += 1
    if r == 0:
        if votes.count(max(votes)) > 1:
            return 0
        else:
            return 1
    return r
