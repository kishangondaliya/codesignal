from itertools import permutations, islice

def kthPermutation(numbers, k):
    return next(islice(permutations(numbers), k-1, None), numbers)
