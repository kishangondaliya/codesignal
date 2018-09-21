def properNounCorrection(noun):
    if len(noun) > 0:
        return noun[0].upper() + "".join([a.lower() for a in noun[1:]])
    return
