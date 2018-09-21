def amendTheSentence(s):
    new_s = ''
    for i, e in enumerate(s):
        if ord(e) < 97:
            if i != 0:
                new_s += ' '
            new_s += chr(ord(e)+32)
        else:
            new_s += e
    return new_s
