import random as r

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = int(r.randint(15, 30))
        self.res = int(r.randint(1, 10))
        self.dmg = int(r.randint(5, 15))
        self.exp = 0
        self.lvl = 0
        if self.exp == 10:
            self.exp = 0
            return self.lvl + 1
        
class agent:
    def __init__(self, name):
        self.name = name
        self.hp = int(r.randint(10, 30))
        self.res = int(r.randint(1, 10))
        self.dmg = int(r.randint(5, 20))