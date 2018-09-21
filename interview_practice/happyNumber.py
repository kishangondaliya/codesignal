def happyNumber(n):
    my_set = set()
    while n != 1:
        tmp = 0
        for e in str(n):
            tmp += int(e) * int(e)
        n = tmp
        if n in my_set:
            return False
        my_set.add(n) 
    return True
