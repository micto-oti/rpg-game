import sys
sys.path.append(r'E:\projects\github\rpg-game\assets')
sys.path.append(r'E:\projects\github\rpg-game\config')
import config as con
import class_char as ch
import class_enemy as ce
import random as rd
import menu as mn
import locations as loc
import events_1 as evs1


########################
mn.main_menu.m_n()

p_name = input('введите имя:\n> ')
p = ch.Player(p_name)

########################
""" print(
    f'имя: {p.name}',
    f'\nздоровье: {p.hp}',
    f'\nурон: {p.dmg}',
    f'\nсопротивление: {p.res}'
)
 """

def распределение_очков():
    main_hp = p.hp
    dmg = p.dmg
    res = p.res
    c = 7
    while c != 0:
        print(f'\n[имеются {c} нераспределённых очков характеристик]')
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
                print('нельзя ввести меньше 1 и больше 3')
    print(
            f'\nздоровье: {main_hp}',
            f'\nурон: {dmg}',
            f'\nсопротивление: {res}'
        )
    в_о = input('вас устраивают эти характеристики? (YES/NO)\n> ')
    return в_о, main_hp, dmg, res

в_о = распределение_очков()

while в_о[0].lower() != 'yes':
    if в_о[0].lower() == 'no':
        в_о = распределение_очков()

char_hp = в_о[1]
char_dmg = в_о[2]
char_res = в_о[3]

########################


enkefalin = 0
cred = 0

ch_hp = char_hp
while ch_hp > 0:
    ch_hp = char_hp
    while enkefalin < 30 or ch_hp > 0:
        print("\nкуда пойти?")
        loc.game_loc(ch_hp, char_dmg, char_res)
        
        print(ch_hp)

print('УМЕР')
