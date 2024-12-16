import sys
sys.path.append(r'E:\projects\github\rpg-game')
sys.path.append(r'E:\projects\github\rpg-game\config')
import battle_status as btl_sts
from main import hp_ch, dmg
import menu
######

class Events:
    def бой(dir):
        match dir:
            case 1:
                hp = hp_ch
                agro_hp = btl_sts.sys_game()
                print(agro_hp)
                """ while agro_hp >= 0 or hp >= 0:
                    b = menu.battle_menu.b_m()
                    bt_sts = btl_sts.btl.bt(b,hp,dmg,agro_hp)
                    hp = bt_sts[0]
                    agro_hp = bt_sts[1]
                    print(f'ваше здоровье: {hp}\nздоровье аномалии: {ag_hp}')
 """
                if agro_hp <= 0:
                    pass
                elif hp <= 0:
                    return hp
            
            case 2:
                pass
            case 3:
                pass
