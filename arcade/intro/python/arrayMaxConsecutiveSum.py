def arrayMaxConsecutiveSum(inputArray, k):
    i = 0
    max = 0
    sum = 0
    n =  len(inputArray)
    while i < k:
        sum += inputArray[i]
        i += 1
    if sum > max:
        max = sum
    v = sum
    for j in range(k , n):
        v = v - inputArray[j - k] + inputArray[j]
        if v > max:
            max = v
    return max






# def arrayMaxConsecutiveSum(inputArray, k):
#     i = 0
#     res = []
#     while i < len(inputArray):
#         j = i
#         stop = 0
#         v = 0
#         while j < len(inputArray):
#             v += inputArray[j]
#             stop += 1
#             j+=1
#             if stop == k:
#                 res.append(v)
#         i += 1
#     return max(res)
        
