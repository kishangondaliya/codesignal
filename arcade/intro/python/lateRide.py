def lateRide(n):
    sum = 0
    res = 0
    if n > 60:
        res = n / 60
        arr = str(res).split('.')
        arr_left = arr[0]
        arr_right = arr[1]
        print(arr_left)
        for e in str(arr_left):
            sum += int(e)
        arr_right = "0." + arr_right
        l = round(float(arr_right) * 60)
        arr = str(l).split('.')
        print("l", l)
        print(arr)
        for e in str(arr[0]):
            sum += int(e)
        return sum
    elif n == 0:
        return 0
    elif n < 10:
        return n
    elif n < 60:
        for e in str(n):
            sum += int(e)
    return sum 
        
