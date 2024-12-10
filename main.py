import sys
sys.path.append(r'E:\projects\github\rpg-game\assets')  # Замените на ваш путь
import config as con
import class_char as ch
import class_enemy as ce
import random as rd
import menu as mn
import battle
import locations as loc



########################
mn.main_menu.m_n()

p_name = input('введите имя: ')
p = ch.Player(p_name)

main_hp = p.hp
dmg = p.dmg
res = p.res

########################
""" print(
    f'имя: {p.name}',
    f'\nздоровье: {p.hp}',
    f'\nурон: {p.dmg}',
    f'\nсопротивление: {p.res}'
)
 """
c = 7
while c != 0:
    print(f'\nимеются нераспределённых очков прокачки {c}')
    print(
        f'здоровье: {p.hp}',
        f'\nурон: {p.dmg}',
        f'\nсопротивление: {p.res}'
    )
    
    i = int(input('> '))
    match i:
        case 1: 
            p.hp += 1
            c -= 1
        case 2:
            p.dmg += 1
            c -= 1
        case 3:
            p.res += 1
            c -= 1
        case _:
            print('нельзя ввести меньше 1 и больше 3')

########################
main_hp = p.hp
dmg = p.dmg
res = p.res

enkefalin = 0
hp = main_hp

while hp != 0:
    hp = main_hp
    while enkefalin != 30 or hp != 0:
        print("куда пойти?")
        loc.locations.game_loc()