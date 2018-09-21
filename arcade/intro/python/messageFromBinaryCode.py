def messageFromBinaryCode(code):
    a = ''
    for i in range(0, len(code), 8):
        a += chr(int(code[i:i+8], 2))
    return a
