def tennisSet(score1, score2):
    if score1 < 0 or score2 < 0:
        return False
    if score1 < 6 and score2 < 6:
        return False
    
    if score1 == 6 and score2 <= 4:
        return True
    elif score2 == 6 and score1 <= 4:
        return True
    elif (score2 == 6 and score1 !=7) or (score1 == 6 and score2 !=7):
        return False
    
    if score1 == 7 and score2 ==6:
        return True
    if score2 == 7 and score1 ==6:
        return True
    
    
    if score1 >= 7 and (score1 - score2) != 2 :
        return False
    
    if score2 >= 7 and (score2 - score1) != 2 :
        return False
    
    
    if score1 >= 7 and (score1 - score2) == 2:
        return True
    
    if score2 >= 7 and (score2 - score1) == 2:
        return True
    
