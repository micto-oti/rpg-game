import config as con
import class_char as ch
import class_enemy as ce
import random as rd
import menu as mn

########################
mn.main_menu.m_n(1)

p_name = input('введите имя: ')
p = ch.Player(p_name)
print(
    f'имя: {p.name}',
    f'\nздоровье: {p.hp}',
    f'\nурон: {p.dmg}',
    f'\nсопротивление: {p.res}'
)

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