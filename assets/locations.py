import sys
sys.path.append(r'E:\projects\github\rpg-game\config')
sys.path.append(r'E:\projects\github\rpg-game')
sys.path.append(r'E:\projects\github\rpg-game\assets')
import class_enemy as cl_en
import events_1 as evs1

######

def game_loc(ch_hp, char_dmg, char_res):
    print('1. Отдел контроля')
    print('2. Отдел исследования')
    print('3. Отдел подавления')
    print('4. Меню')
    opt = int(input('> '))

    while opt < 1 or opt > 4:
        print('Выберите одну из опций')
        opt = int(input('> '))

    match opt:
        case 1:
            result = evs1.Evs.бой(ch_hp, char_dmg, char_res)
            return result

        case 2:
            return opt
        case 3:
            return opt
        case 4:
            return opt