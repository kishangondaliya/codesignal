def addBorder(picture):
    border_picture = []
    for e in picture:
        l = list(e)
        l.insert(0,'*')
        l.append('*')
        border_picture.append(''.join(l))
    a = len(border_picture[0])
    z = '*' * a
    border_picture.insert(0,z)
    border_picture.append(z)
    return border_picture
