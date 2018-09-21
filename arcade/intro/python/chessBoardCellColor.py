


def chessBoardCellColor(cell1, cell2):
    d = {}
    first_color = 'a'
    second_color = 'b'
    color  = None
    for i, e in enumerate("ABCDEFGH"):
        if i % 2 == 0:
            color = 'a'
        else:
            color = 'b'
        for i in range(1,9):
            k = e + str(i)
            d[k] = color
            if color == 'a':
                color = 'b'
            else:
                color = 'a'
    return d[cell1] == d[cell2]
