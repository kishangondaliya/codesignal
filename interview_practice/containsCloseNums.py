def containsCloseNums(nums, k):
    dic = {}
    for i, n in enumerate(nums):
        if n in dic:
            if abs(dic[n] - i) <= k:
                return True
            dic[n] =i
        else :
            dic[n] = i
    return False
