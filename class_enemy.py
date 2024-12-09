import random as r

class st_abnormaly:
    def __init__(self,name):
        self.name = name
        self.hp = int(r.randint(40, 100))
        self.res = int(r.randint(5, 20))
        self.dmg = int(r.randint(10, 25))
        