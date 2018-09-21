def incorrectPasscodeAttempts(passcode, attempts):
    i = 0
    for e in attempts:
        if passcode == e:
            i = 0
        else:
            i += 1
        if i >= 10:
            return True
    
    return False
            
        
