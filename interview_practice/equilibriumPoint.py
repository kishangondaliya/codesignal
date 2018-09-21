def equilibriumPoint(arr):
    if len(arr) == 1:
        return 1
    
    l = 0
    r = 0
    t_sum = sum(arr)
    left_sum =0
    while l < len(arr):
        t_sum -= arr[l]
        if left_sum == t_sum:
            return l + 1
        left_sum += arr[l]
        l += 1
    
    return -1
