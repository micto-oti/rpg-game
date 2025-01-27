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
import items as itms

инвентарь = itms.display_items()


######################## отчищаем экран

########################
print("\033[H\033[J", end="")
mn.main_menu.m_n()

########################

print("\033[H\033[J", end="")
player = ch.S_P.распределение_очков()
выбор = player[0]

while выбор.lower() != 'yes':
    if выбор.lower() == 'no':
        player = ch.S_P.распределение_очков()
        выбор = player[0]
    else:
        print("\033[H\033[J", end="")
        print(
            f'имя: {player[4]}'
            f'\nздоровье: {player[1]}',
            f'\nурон: {player[2]}',
            f'\nсопротивление: {player[3]}'
        )
        выбор = input('Вас устраивают эти характеристики? (YES/NO)\n> ')


########################

char_hp = player[1]
char_dmg = player[2]
char_res = player[3]
p = player[5]

########################

p.hp = char_hp
p.dmg = char_dmg
p.res = char_res

########################

enkefalin = 0
cred = 0
хилка = 0
мана = 0

ch_hp = char_hp
while ch_hp > 0 or enkefalin < 300:
    игра_не_пройдена = False
    ch_hp = p.hp
    enkefalin1 = 0
    Skill_points = 0
    while enkefalin1 < 15 and ch_hp > 0:
        print("\033[H\033[J", end="")
        print(f'Количество энкефалина: {enkefalin1} | общее количество энкефалина {enkefalin}')
        print(f'\nВаше здоровье: {ch_hp}\n')
        print("Куда пойти?")
        result = loc.game_loc(ch_hp, p)
        ch_hp = int(result[1])
        enkefalin1 = p.enk
        
        if p.enk == 15:
            enkefalin += 15
            p.enk = 0
        
        if p.exp >= 15:
            p.lvl += 1
            p.exp = p.exp - 15
            Skill_points += 1

            print("\033[H\033[J", end="")
            print('у вас есть 1 очко характеристик')
            print(
                f'имя: {p.name}',
                f'\nуровень: {p.lvl}   /   опыт: {p.exp}',
                f'\nздоровье: {p.hp}',
                f'\nэнергия: {p.mana}/{p.g_mana}',
                f'\nурон: {p.dmg}',
                f'\nсопротивление: {p.res}'
            )

            print('\nВыберите один из параметров')
            print('1. Здоровье      | +3',
                '\n2. Энергия       | +5',
                '\n3. Урон          | +1',
                '\n4. Сопротивление | +1'
                )        

            i = input('> ')

            match i:
                case '1': 
                    p.hp += 3
                    ch_hp = p.hp
                    Skill_points -= 1

                case '2':
                    p.g_mana += 5
                    p.mana = p.g_mana
                    Skill_points -= 1
                case '3':
                    p.dmg += 1
                    Skill_points -= 1
                case '3':
                    p.res += 1
                    Skill_points -= 1
                case _:
                    pass



    if result[0] == False:
        print("\033[H\033[J", end="")
        print('УМЕР')
        sys.stdin.readline()
        игра_не_пройдена = True
        break
    else:
        pass

if игра_не_пройдена == False:
    print('Вы прошли игру')