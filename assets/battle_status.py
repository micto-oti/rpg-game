import sys
sys.path.append(r'E:\projects\github\rpg-game')
sys.path.append(r'E:\projects\github\rpg-game\assets')
sys.path.append(r'E:\projects\github\rpg-game\config')
import class_enemy as cl_en
import menu
import items as its

###### импорт предметов

###### импорт аномалий

т_к_ж = cl_en.тот_кто_ждёт()
ст_лд = cl_en.старая_леди()
т_л = cl_en.тысяча_лиц()

###### импорт характеристик аномалий

# характеристики аномалий
т_к_ж_dmg, т_к_ж_res = т_к_ж.dmg, т_к_ж.res

ст_лд_dmg, ст_лд_res = ст_лд.dmg, ст_лд.res

т_л_dmg, т_л_res = т_л.dmg, т_л.res

######

class btl:
    def old_lady(hp_ch, char_dmg, char_res, enemy_hp):
        global ст_лд_dmg, ст_лд_res

        while hp_ch > 0:
            choose = menu.battle_menu.b_m()
            print("\033[H\033[J", end="")
#            print(f'Ваше здоровье: {hp_ch} | Здоровье аномалии: {ст_лд_hp}')

            match choose:
                case '1':
                    урон = char_dmg / (ст_лд_res * 0.2)
                    print(f'Вы наносите аномалии урон: {урон}')
                    enemy_hp -= урон

                    
                    if enemy_hp > 0:
                        hp_ch -= ст_лд_dmg / (char_res / 3)
                        print(f'урон от аномалии: {ст_лд_dmg / (char_res / 3)}\n')
                        print(f'Ваше здоровье: {hp_ch} | Здоровье аномалии: {enemy_hp}\n')
                    else:
                        return True, hp_ch, True

                case '2':
                    pass
                case '3':
                    pass
                case '4':
                    pass
                case _:
                    print('Выберите одну из опций\n')
                    print(f'Ваше здоровье: {hp_ch} | Здоровье аномалии: {enemy_hp}\n')
            
        return False, hp_ch, None

