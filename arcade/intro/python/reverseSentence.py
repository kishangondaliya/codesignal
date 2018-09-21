def reverseSentence(sentence):
    arr = sentence.split(' ')
    arr_len = len(arr) -1
    new_arr = []
    while arr_len >= 0:
        new_arr.append(arr[arr_len])
        arr_len -= 1
    return " ".join(new_arr)
