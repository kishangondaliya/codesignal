def countSumOfTwoRepresentations2(n, l, r):
    res = 0
    s = set()
    j = l
    while j <= r:
        s.add(j)
        j += 1
    i = l
    added = set()
    while i <= r:
        if (n - i) in s:
            #print("->",[n-i], i)
            if "{}.{}".format(n-i,i) not in added  or "{}.{}".format(i, n-i) not in added:
                added.add("{}.{}".format(n-i,i))
                added.add("{}.{}".format(i, n-i))
                res += 1
        i += 1
    return res



# def countSumOfTwoRepresentations2(n, l, r):
#     res = 0
#     while l <= r:
#         j = l
#         while j <= r:
#             if l + j == n:
#                 res += 1
#             if l + j > n:
#                 break
#             j +=1
#         if l + l > n:
#             break
#         l+= 1
#     return res
    
