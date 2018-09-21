
def convert_to_hash_map(solution):
    dic = {}
    for e in solution:
        dic[e[0]] = e[1]

    return dic

def isCryptSolution(crypt, solution):
    dic = convert_to_hash_map(solution)
    new_arr = []
    for elem in crypt:
        new_word = ""
        for letter in elem:
            new_word += dic[letter]
        new_arr.append(new_word)
    for e in new_arr:
        if len(e) > 1 and e[0] == '0':
            return False
    int_arr = [int(i) for i in new_arr]

    return sum(int_arr[:-1]) == int_arr[-1:][0]
        
