class Team(object):
    def __init__(self, names):
        self.names = names

    def __nonzero__(self):
        first_letter = []
        last_letter = []
        for name in self.names:
            first_letter.append(name.lower()[0])
            last_letter.append(name.lower()[-1])
        
        for f in first_letter:
            try:
                last_letter.remove(f)
            except:
                pass
        if len(last_letter) == 1 or not len(last_letter):
            return 1
        return 0

def isCoolTeam(team):
    return bool(Team(team))
