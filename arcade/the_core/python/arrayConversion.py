def add_adj(arr):
    new_arr = []
    i = 0
    while i < len(arr) -1:
        new_arr.append(arr[i] + arr[i+1])
        i +=2
    return new_arr
    

def do_product(arr):
    new_arr = []
    i = 0
    while i < len(arr) -1:
        new_arr.append(arr[i] * arr[i+1])
        i +=2
    return new_arr

def arrayConversion(inputArray):
    nb_iteration = 1
    while len(inputArray) > 1:
        if nb_iteration % 2 != 0:
            inputArray = add_adj(inputArray)
            nb_iteration += 1
        else:
            inputArray = do_product(inputArray)
            nb_iteration += 1
        
    return inputArray[0]
