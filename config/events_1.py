import sys
sys.path.append(r'E:\projects\github\rpg-game')
sys.path.append(r'E:\projects\github\rpg-game\config')
import battle_status as btl_sts
import random as r
import class_enemy as cl_en

###### импорт аномалий
""" 
т_к_ж = cl_en.тот_кто_ждёт()
ст_лд = cl_en.старая_леди()
т_л = cl_en.тысяча_лиц()
 """
###### импорт характеристик аномалий

# характеристики аномалий
""" 
т_к_ж_hp = т_к_ж.hp

ст_лд_hp = ст_лд.hp

т_л_hp = т_л.hp
 """
######

class Evs:
    def бой(hp_ch, char_dmg, char_res, enemy):
        
        ######

        if enemy.name == 'старая леди':
            rand = r.randint(1,3)

            match rand:
                case 1:
                    print("\033[H\033[J", end="")
                    print(f'Вы пришли в отдел контроля')
                    print('Вы столкнулись с аномалией Старая леди')
                    print(f'\nВаше здоровье: {hp_ch} | Здоровье аномалии: {enemy.hp}')
                    res = btl_sts.btl.old_lady(hp_ch, char_dmg, char_res, enemy.hp)

                    return res 
            
                case 2:
                    print('Вы пришли в отдел контроля и получили предмет')
                    item = r.choice(['лекарство','таблетка','деньги'])
                    if item == 'деньги':
                        money = r.randint(5,50)
                    else:
                        money == 0
                    print('Вы получили' + item + f'({money})')
                    return True, hp_ch, None, item, money
                case 3:
                    print('Вы пришли в отдел контроля.\nа зачем вы сюда пришли?')
                    return True, hp_ch, None
        
        ######

        elif enemy.name == 'тот кто ждёт':

            rand = r.randint(1,3)

            match rand:
                case 1:
                    print("\033[H\033[J", end="")
                    print(f'Вы пришли в отдел исследований')
                    print('Вы столкнулись с аномалией Тот кто ждёт')
                    print(f'\nВаше здоровье: {hp_ch} | Здоровье аномалии: {enemy.hp}')
                    res = btl_sts.btl.old_lady(hp_ch, char_dmg, char_res, enemy.hp)

                    return res 
            
                case 2:
                    print('Вы пришли в отдел исследований и получили предмет')
                    item = r.choice(['лекарство','таблетка','энкефалин'])
                    if item == 'деньги':
                        money = r.randint(5,50)
                    else:
                        money == 0
                    print('Вы получили' + item + f'({money})')
                    return True, hp_ch, None, item, money
                case 3:
                    print('Вы пришли в отдел исследований.\nа зачем вы сюда пришли?')
                    return True, hp_ch, None
                
        ######

        elif enemy.name == 'тысяча лиц':
            rand = r.randint(1,3)

            match rand:
                case 1:
                    print("\033[H\033[J", end="")
                    print(f'Вы пришли в отдел подавления')
                    print('Вы столкнулись с аномалией Старая леди')
                    print(f'\nВаше здоровье: {hp_ch} | Здоровье аномалии: {enemy.hp}')
                    res = btl_sts.btl.old_lady(hp_ch, char_dmg, char_res, enemy.hp)

                    return res 
            
                case 2:
                    print('Вы пришли в отдел подавления и получили предмет')
                    return True, hp_ch, None
                case 3:
                    print('Вы пришли в отдел подавления.\nа зачем вы сюда пришли?')
                    return True, hp_ch, None