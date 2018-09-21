import random

def createDie(seed, n):
    class Die(object):
        # def __init__(self, seed, n):
        #     self.seed = seed
        #     self.n = n
        
        def __new__(self, seed, n):
            random.seed(seed)
            return int(random.random() * n) + 1.

    class Game(object):
        die = Die(seed, n)

    return Game.die
