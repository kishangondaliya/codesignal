def appleBoxes(k):
    yellow = []
    red = []
    for i in range(1, k + 1):
        if i % 2 == 0:
            red.append(i)
        if i % 2 != 0:
            yellow.append(i)
            
    red = [ i*i for i in red]
    yellow = [ i*i for i in yellow]
    return sum(red) - sum(yellow)
