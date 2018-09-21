def validTime(time):
    
    arr = time.split(':')
    
    if len(arr) != 2:
        return False
    if int(arr[0]) > 23 or int(arr[0]) < 0:
        return False
    if int(arr[1]) > 59 or int(arr[1]) < 0:
        return False
    
    
    return True
