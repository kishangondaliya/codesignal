def sortCodefighters(codefighters):
    res = [CodeFighter(*codefighter) for codefighter in codefighters]
    res.sort(reverse=True)
    return map(str, res)

class CodeFighter():
    def __init__(self, username, ID, xp):
        self.username = username
        self.ID = ID
        self.xp = xp
        
    # def __lt__(self, other):
    #     return ((int(self.xp) > int(other.xp)) and (int(self.id)  < int(other.id)))
    
    # def __gt__(self, other):
    #     return int(self.xp) > int(other.xp)
    
    def __str__(self):
        return self.username
    
    
    def __cmp__(self, other):
        if (int(self.xp) > int(other.xp)):
            return 1
        elif (int(self.xp) < int(other.xp)):
            return -1
        else:
            if (int(self.ID) > int(other.ID)):
                return -1
            elif (int(self.ID) < int(other.ID)):
                return 1
            else:
                return 0
