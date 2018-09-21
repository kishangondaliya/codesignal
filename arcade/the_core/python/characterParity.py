def characterParity(symbol):
    if not symbol.isdigit():
        return "not a digit"
    else:
        if int(symbol) % 2 == 0:
            return "even"
        else:
            return "odd"
    
