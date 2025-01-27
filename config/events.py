import sys
sys.path.append(r'E:\projects\github\rpg-game')
sys.path.append(r'E:\projects\github\rpg-game\config')
import battle_status as btl_sts
import random as r
import class_enemy as cl_en

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