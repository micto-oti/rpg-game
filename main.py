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


######################## отчищаем экран

########################
print("\033[H\033[J", end="")
mn.main_menu.m_n()

print("\033[H\033[J", end="")
p_name = input('введите имя:\n> ')
p = ch.Player(p_name)

########################

def распределение_очков():
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
    return в_о, main_hp, dmg, res

в_о = распределение_очков()
выбор = в_о[0]

while выбор.lower() != 'yes':
    if выбор.lower() == 'no':
        в_о = распределение_очков()
        выбор = в_о[0]
    else:
        print("\033[H\033[J", end="")
        print(
            f'имя: {p.name}'
            f'\nздоровье: {в_о[1]}',
            f'\nурон: {в_о[2]}',
            f'\nсопротивление: {в_о[3]}'
        )
        выбор = input('Вас устраивают эти характеристики? (YES/NO)\n> ')

char_hp = в_о[1]
char_dmg = в_о[2]
char_res = в_о[3]

########################



########################

enkefalin = 0
cred = 0
хилка = 0
мана = 0

ch_hp = char_hp
while ch_hp > 0 or enkefalin < 300:
    игра_не_пройдена = False
    ch_hp = char_hp
    enkefalin1 = 0
    
    while enkefalin1 < 10 and ch_hp > 0:
        print("\033[H\033[J", end="")
        print(f'Количество энкефалина: {enkefalin1} | общее количество энкефалина {enkefalin}')
        print(f'\nВаше здоровье: {ch_hp}\n')
        print("Куда пойти?")
        res = loc.game_loc(ch_hp, char_dmg, char_res, char_hp)
        ch_hp = int(res[1])
        enk = res[2]
        
        if enk == True:
            enkefalin1 += 1
            enkefalin += 1
    
    if res[0] == False:
        print("\033[H\033[J", end="")
        print('УМЕР')
        sys.stdin.readline()
        игра_не_пройдена = True
        break
    else:
        pass

if игра_не_пройдена == False:
    print('Вы прошли игру')