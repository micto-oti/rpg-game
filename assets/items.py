import sys
sys.path.append(r'E:\projects\github\rpg-game')

items = ['лекарство','энкевалин','таблетка','кредиты']

def heal(ch_hp, char_hp):
    if ch_hp+5 < char_hp:
        ch_hp += 5
        print('heal')
        print(ch_hp)
    elif ch_hp+5 > char_hp:
        ch_hp = char_hp

def enk(enkefalin):
    enkefalin += 1

def credits(cred):
    cred += 2