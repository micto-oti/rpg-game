import sys
sys.path.append(r'E:\projects\github\rpg-game')
sys.path.append(r'E:\projects\github\rpg-game\config')
import battle_status as btl_sts
import random as r
import class_enemy as cl_en

###### импорт аномалий

т_к_ж = cl_en.тот_кто_ждёт()
ст_лд = cl_en.старая_леди()
т_л = cl_en.тысяча_лиц()

###### импорт характеристик аномалий

# характеристики аномалий
т_к_ж_hp = т_к_ж.hp

ст_лд_hp = ст_лд.hp

т_л_hp = т_л.hp

######

class Evs:
    def бой(hp_ch, char_dmg, char_res):
        global т_к_ж_hp, ст_лд_hp, т_л_hp
        rand = r.randint(1,3)

        match rand:
            case 1:
                print(f'\nВы пришли в отдел контроля')
                print('\nВы столкнулись с аномалией Старая леди')
                print(f'Ваше здоровье: {hp_ch} | Здоровье аномалии: {ст_лд_hp}')
                res = btl_sts.btl.old_lady(hp_ch, char_dmg, char_res, ст_лд_hp)

                return res 
            
            case 2:
                print('Вы пришли в отдел контроля и получили предмет')
                return True, hp_ch
            case 3:
                print('Вы пришли в отдел контроля.\nа нахуя вы сюда пришли?')
                return True, hp_ch