def variableName(name):
    if name[0].isdigit():
        return False
    for e in name:

        if (e >='A' and e <= 'Z') or (e >='a' and e <= 'z') or e == '_' or (e >='0' and e <= '9'):
            pass
        else:
            return False
    return True
