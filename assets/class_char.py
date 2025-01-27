import random as r



class Player:
    def __init__(self, name):
        self.name = name
        self.hp = int(r.randint(15, 30))
        self.res = int(r.randint(1, 10))
        self.dmg = int(r.randint(5, 15))
        self.g_mana = 25
        self.mana = 25
        self.exp = 0
        self.lvl = 0
        self.enk = 0

class S_P:
    def распределение_очков():
        p_name = input('введите имя:\n> ')
        p = Player(p_name)
        main_hp = p.hp
        dmg = p.dmg
        res = p.res
        c = 7
        while c != 0:
            print("\033[H\033[J", end="")
            print(f'[имеются {c} нераспределённых очков характеристик]')
            print(
                f'здоровье: {main_hp}',
                f'\nурон: {dmg}',
                f'\nсопротивление: {res}'
            )
    
            i = input('> ')
            match i:
                case '1': 
                    main_hp += 1
                    c -= 1
                case '2':
                    dmg += 1
                    c -= 1
                case '3':
                    res += 1
                    c -= 1
                case _:
                #print('нельзя ввести меньше 1 и больше 3')
                    pass
 
        print("\033[H\033[J", end="")
        print(
                f'имя: {p.name}'
                f'\nздоровье: {main_hp}',
                f'\nурон: {dmg}',
                f'\nсопротивление: {res}'
        )
        в_о = input('Вас устраивают эти характеристики? (YES/NO)\n> ')
        return в_о, main_hp, dmg, res, p_name, p
    

""" 
class agent:
    def __init__(self, name):
        self.name = name
        self.hp = int(r.randint(10, 30))
        self.res = int(r.randint(1, 10))
        self.dmg = int(r.randint(5, 20)) """