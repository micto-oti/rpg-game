import random as r

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = int(r.randint(10, 30))
        self.res = int(r.randint(0, 10))
        self.dmg = int(r.randint(5, 20))

class agent:
    def __init__(self, name):
        self.name = name
        self.hp = int(r.randint(10, 30))
        self.res = int(r.randint(0, 10))
        self.dmg = int(r.randint(5, 20))