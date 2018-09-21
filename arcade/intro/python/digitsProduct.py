


def digitsProduct(product):
    if product == 1:
        return 1
    if product == 0:
        return 10
    
    if product < 10:
        if product in [2,3,7,9]:
            return product
        return 10 + product
    arr = []
    n = 9
    while n > 1:
        if product % n == 0:
            product = product / n 
            arr.append(n)
            n = 10
        n -= 1
    if product != 1:
        return -1

    a = sorted(arr)
    s = 0
    s = int("".join([str(i) for i in a]))
    return s
    
