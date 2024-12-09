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
    if i == 1:
        p.hp += 1
        c -= 1
    elif i == 2:
        p.dmg += 1
        c -= 1
    elif i == 3:
        p.res += 1
        c -= 1
    else:
        print('i не может быть меньше 1 и больше 3')