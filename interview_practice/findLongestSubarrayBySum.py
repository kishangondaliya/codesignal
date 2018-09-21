def findLongestSubarrayBySum(s, arr):
    res = []
    new_arr = []
    left = 0
    i = 0
    sum_ = 0
    while i < len(arr):
        if sum_ <= s:
            sum_ += arr[i]
        while sum_ > s:
            sum_ -= arr[left]
            left += 1
        if sum_ == s:
            while i < len(arr) -1 and sum_ + arr[i+1] == s:
                sum_ += arr[i+1]
                i+=1
            res.append(([left+1, i+1], i - left))
        i +=1

    if res:
        res.sort(key=lambda x: x[1])
        res = list(reversed(res))
        return res[0][0]
    return [-1]
