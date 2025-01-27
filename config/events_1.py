import sys
sys.path.append(r'E:\projects\github\rpg-game')
sys.path.append(r'E:\projects\github\rpg-game\config')
import battle_status as btl_sts
import random as r
import class_enemy as cl_en
import items as itms

###### создаём инвентарь 

Tier1 = cl_en.Tier1_recall()
Tier2 = cl_en.Tier2_recall()
Tier3 = cl_en.Tier3_recall()

######



class Evs:
    def бой(hp_ch, p, enemy_tier):
        
##############################################
        
        print("\033[H\033[J", end="")

        tier = int(enemy_tier)

        if tier == 1:
            abnormally = r.choice(Tier1)
            rand = r.randint(1,3)
            money = 0

            match rand:
                case 1:
                    #print("\033[H\033[J", end="")
                    
                    res = btl_sts.btl.old_lady(hp_ch, p, abnormally)

                    return res
            
                case 2:

                    print('Вы пришли в отдел контроля и получили предмет:')
                    item = r.choice(['лекарство','деньги'])

                    if item == 'деньги':
                        money = r.randint(5,50)
                        itms.add_item('деньги', money)

                        print('Вы получили ' + item + f'({money})')

                    else:
                        itms.add_item('лекарство', 1)

                        print('Вы получили Аптечка (1)')
                    
                    cont_game = input('> ')

                    return None, hp_ch, None
                
                case 3:

                    res = btl_sts.btl.old_lady(hp_ch, p, abnormally)

                    return res
                
##############################################

        if tier == 2:
            abnormally = r.choice(Tier2)
            rand = r.randint(1,3)
            money = 0

            match rand:
                case 1:
                    #print("\033[H\033[J", end="")
                    
                    res = btl_sts.btl.old_lady(hp_ch, p, abnormally)

                    return res
            
                case 2:

                    print('Вы пришли в отдел исследований и получили предмет:')
                    item = r.choice(['деньги','энкефалин', 'таблетка'])

                    if item == 'деньги':
                        money = r.randint(5,50)
                        itms.add_item('деньги', money)

                        print('Вы получили ' + item + f'({money})')

                    elif item == 'энкефалин':
                        print('Вы получили ' + item + ' (1)')
                        cont_game = input('> ')

                        return True, hp_ch, None
                    
                    else:
                        itms.add_item('таблетка', 1)

                        print('Вы получили Капсула энкефалина (1)')

                    cont_game = input('> ')

                    return None, hp_ch, None
                
                case 3:

                    res = btl_sts.btl.old_lady(hp_ch, p, abnormally)

                    return res

##############################################

        if tier == 3:
            abnormally = r.choice(Tier3)
            rand = r.randint(1,3)
            money = 0

            match rand:
                case 1:
                    #print("\033[H\033[J", end="")
                    
                    res = btl_sts.btl.old_lady(hp_ch, p, abnormally)

                    return res
            
                case 2:

                    print('Вы пришли в отдел контроля и получили предмет:')
                    item = r.choice(['лекарство', 'таблетка','деньги'])

                    if item == 'деньги':
                        money = r.randint(5,50)
                        itms.add_item('деньги', money)

                        print('Вы получили ' + item + f'({money})')

                    elif item == 'лекарство':
                        itms.add_item('лекарство', 1)

                        print('Вы получили Аптечка (1)')
                    
                    else:
                        itms.add_item('таблетка', 1)

                        print('Вы получили Капсула энкефалина (1)')

                    
                    cont_game = input('> ')

                    return None, hp_ch, None
                
                case 3:

                    res = btl_sts.btl.old_lady(hp_ch, p, abnormally)

                    return res