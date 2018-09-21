import itertools


def diff_by_one_charcter(a, b):
    if len(a) != len(b):
        return False
    if a == b:
        return False
    count = 0
    for z, y in zip(a, b):
        if z != y:
            count += 1
    if count == 1:
        return True
    return False


def stringsRearrangement(inputArray):
    all_perm = itertools.permutations(inputArray)
    all_perm = [i for i in all_perm]
    for sub_arr in all_perm:
        i = 0
        good = True
        while i < len(sub_arr)-1:
            if not diff_by_one_charcter(sub_arr[i], sub_arr[i + 1]):
                good = False
                break
            i += 1
        if good:
            return True
    return False
