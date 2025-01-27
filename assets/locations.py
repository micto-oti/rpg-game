import sys
sys.path.append(r'E:\projects\github\rpg-game\config')
sys.path.append(r'E:\projects\github\rpg-game')
sys.path.append(r'E:\projects\github\rpg-game\assets')
import class_enemy as cl_en
import events_1 as evs1
import menu
import items as itms


###### импорт предметов

инвентарь = itms.display_items()


###### импорт врагов

Tier1 = cl_en.Tier1_recall()
Tier2 = cl_en.Tier2_recall()
Tier3 = cl_en.Tier3_recall()

######

def game_loc(ch_hp, p):

    print('1. Отдел контроля')
    print('2. Отдел исследований')
    print('3. Отдел подавления')
    print('4. Меню')
    opt = (input('> '))

    while opt < '1' or opt > '4':
        print('Выберите одну из опций')
        opt = (input('> '))

    opt = int(opt)
    hp_ch = ch_hp

    match opt:
        case 1:
            result = evs1.Evs.бой(ch_hp, p, 1)
            return result

        ##############################

        case 2:
            result = evs1.Evs.бой(ch_hp, p, 2)
            return result
        
        ##############################

        case 3:
            result = evs1.Evs.бой(ch_hp, p, 3)
            return result
        
        ############################## работа с меню

        case 4:
            menu_option = menu.character_menu.char_menu()
            
            if menu_option == 1:
                return None, ch_hp

            elif menu_option == 2:
                print("\033[H\033[J", end="")
                print(f'Ваше здоровье: {hp_ch}/{p.hp} | Ваша энергия: {p.mana}/{p.g_mana}\n')
                itms.display_items()
                print('1. Восстаносить здоровье')
                print('2. Восстановить ману')
                opt = (input('> '))
                    

                while opt < '1' or opt > '2':
                    print('Выберите одну из опций')
                    opt = (input('> '))

                match opt:
                    case '1': # здоровье
                        if инвентарь['лекарство'] > 0 and hp_ch < (p.hp-5):
                            hp_ch += 5
                            itms.remove_item('лекарство', 1)
                            print(f'Ваше здоровье: {hp_ch}/{p.ph} | Здоровье аномалии: {enemy_hp}\n')
                            cont_game = input('> ')
                        
                        elif инвентарь['лекарство'] > 0 and hp_ch == (p.hp-5):
                            hp_ch = p.hp
                            itms.remove_item('лекарство', 1)
                            print(f'Ваше здоровье: {hp_ch}/{p.ph} | Здоровье аномалии: {enemy_hp}\n')
                            cont_game = input('> ')
                            
                        elif инвентарь['лекарство'] == 0:
                            print('Вы не можете восстановить здоровье (нет лекарств)')
                            cont_game = input('> ')

                    case '2': # мана
                        if инвентарь['таблетка'] > 0 and p.mana < (p.g_mana-5):
                            p.mana += 5
                            itms.remove_item('таблетка', 1)
                            print(f'Ваша энергия: {p.mana}/{p.g_mana} | Здоровье аномалии: {enemy_hp}\n')
                            cont_game = input('> ')
                            
                        elif инвентарь['таблетка'] > 0 and p.mana == (p.g_mana-5):
                            p.mana = p.g_mana
                            itms.remove_item('таблетка', 1)
                            print(f'Ваша энергия: {p.mana}/{p.g_mana} | Здоровье аномалии: {enemy_hp}\n')
                            cont_game = input('> ')
                            
                        elif инвентарь['таблетка'] == 0:
                            print('Вы не можете восстановить здоровье (нет таблеток)')
                            cont_game = input('> ')
                
                return None, ch_hp
            
            elif menu_option == 3:
                print("\033[H\033[J", end="")
                print(
                    f'имя: {p.name}',
                    f'\nуровень: {p.lvl}   /   опыт: {p.exp}',
                    f'\nздоровье: {p.hp}',
                    f'\nэнергия: {p.mana}/{p.g_mana}',
                    f'\nурон: {p.dmg}',
                    f'\nсопротивление: {p.res}'
                )
                cont_game = input('> ')

                return None, ch_hp
            
            elif menu_option == 4:
                print("\033[H\033[J", end="")
                print('1. Купить лекарство (75)')
                print('2. Купить таблетку  (50)\n')
                print('Выберите один из вариантов')

                i = input('> ')

                match i:
                    case '1':
                        if инвентарь['деньги'] >= 75:
                            itms.add_item('лекарство', 1)
                        
                        else:
                            print('Вам не хватает денег')
                            cont_game = input('> ')
                    
                    case '1':
                        if инвентарь['деньги'] >= 50:
                            itms.add_item('таблетка', 1)
                        
                        else:
                            print('Вам не хватает денег')
                            cont_game = input('> ')
                            
                return None, ch_hp