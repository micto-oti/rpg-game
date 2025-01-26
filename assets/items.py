import sys
sys.path.append(r'E:\projects\github\rpg-game')

class invent:
    def __init__(self):
        self.inventory = [0, 0, 0, 0] # 1 - хилка, 2 - таблетка, 3 - экефалин, 4 - деньги

    def add_items(f):
        if f == 'add_heal':
            return 1
        elif f == 'add_mana':
            return 2
        elif f == 'add_enk':
            return 3
        elif f == 'add_money':
            return 4