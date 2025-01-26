import sys
sys.path.append(r'E:\projects\github\rpg-game\config')
sys.path.append(r'E:\projects\github\rpg-game')
sys.path.append(r'E:\projects\github\rpg-game\assets')
import class_enemy as cl_en
import events_1 as evs1
import menu
import items as its

###### импорт предметов

инвентарь = [0, 0, 0, 0]

###### импорт врагов

старая_леди = cl_en.старая_леди()
тот_кто_ждёт = cl_en.тот_кто_ждёт()
тысячя_лиц = cl_en.тысяча_лиц()

######

def game_loc(ch_hp, char_dmg, char_res, char_hp):
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
            result = evs1.Evs.бой(ch_hp, char_dmg, char_res, старая_леди)
            return result

        case 2:
            result = evs1.Evs.бой(ch_hp, char_dmg, char_res, тот_кто_ждёт)
            return result
        
        case 3:
            result = evs1.Evs.бой(ch_hp, char_dmg, char_res, тысячя_лиц)
            return result
        
        case 4:
            opt = menu.character_menu.char_menu(инвентарь)
            if opt == 7:
                if инвентарь[0] > 0:
                    ch_hp + 5
                
                else:
                    pass

                return True, ch_hp, False
            
            elif opt == 8:
                return True, ch_hp, False
            
            elif opt == 999:
                
                return True, ch_hp, False