def isSmooth(arr):
    if arr[0] == arr[-1:][0]:
        if len(arr) % 2 == 0:
            if arr[(len(arr)-1)//2] +  arr[((len(arr)-1)//2)+1] ==  arr[0] :
                return True
        else:
            if arr[(len(arr))//2]  ==  arr[0] :
                return True
        
    return False
