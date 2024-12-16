import sys
sys.path.append(r'E:\projects\github\rpg-game\assets')
sys.path.append(r'E:\projects\github\rpg-game\config')
from menu import battle_menu
import main 
import class_enemy
import events as evs

class btl:
    def bt():
        b = battle_menu.b_m()
        match b:
            case 1:
                main.hp -= 1
                evs.ag_hp -= main.dmg
                
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case _:
                pass