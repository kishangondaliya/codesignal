def singleNumber(nums):
    z = 0
    for e in nums:
        z ^= e
    return z
