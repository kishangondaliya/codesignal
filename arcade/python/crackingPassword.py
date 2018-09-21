from itertools import combinations_with_replacement,permutations, product

def crackingPassword(digits, k, d):
    def createNumber(digs):
        return "".join(map(str, digs))

    return [i for i in sorted([createNumber(i) for i in set(
        # list(combinations_with_replacement(digits,k)) + 
        # list(permutations(digits,k)) + 
        list(product(createNumber(digits), repeat=k)) ) ]) if ( 
        (int(i) % d == 0) or (int(i.lstrip("0")) % d == 0)
    ) ]
