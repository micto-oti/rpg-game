import sys
sys.path.append(r'E:\projects\github\rpg-game')
sys.path.append(r'E:\projects\github\rpg-game\assets')
sys.path.append(r'E:\projects\github\rpg-game\config')
import class_enemy as cl_en
import menu
import items as its
import random

###### импорт предметов

инвентарь = its.display_items()

######

class btl:
    def old_lady(hp_ch, p, enemy):
        cold = 0
        burning = 0
        enemy_hp = enemy.hp

        while hp_ch > 0:
            print("\033[H\033[J", end="")
            print(f'Вы пришли в отдел контроля')
            print(f'Вы столкнулись с аномалией {enemy.name} \n')
            print(f'Ваше здоровье: {hp_ch} | Здоровье аномалии: {enemy_hp}')
            print(f'Ваша энергия: {p.mana}\n')
            choose = menu.battle_menu.b_m()

            match choose:
                case '1':    
                    if burning > 0:
                        burning -= 1
                        
                        print("\033[H\033[J", end="")
                        урон = (p.dmg / (enemy.res)) + 5
                        print(f'Вы наносите аномалии урон: {урон}')
                        enemy_hp -= урон
                        cont_game = input('> ')
                    
                    else:
                        print("\033[H\033[J", end="")
                        урон = p.dmg / (enemy.res)
                        print(f'Вы наносите аномалии урон: {урон}')
                        enemy_hp -= урон
                        cont_game = input('> ')

                    
                    if enemy_hp > 0:
                        
                        if cold > 0:
                            cold -= 1
                            pass

                        else:

                            hp_ch -= enemy.dmg / (p.res / 3)
                            print(f'урон от аномалии: {enemy.dmg / (p.res / 3)}\n')
                            print(f'Ваше здоровье: {hp_ch} | Здоровье аномалии: {enemy_hp}\n')
                            cont_game = input('> ')

                    else:
                        p.enk += 1
                        p.exp += enemy.exp
                        its.add_item('деньги', 50)
                        return True, hp_ch

                case '2':
                    print("\033[H\033[J", end="")
                    print(f'Ваше здоровье: {hp_ch} | Здоровье аномалии: {enemy_hp}')
                    print(f'Ваша энергия {p.mana}\n')
                    print('Выберите 1 из способностей')
                    print('1. Поджёг     (7)          | каждый последующий ход (2) наносит +5 урона\n'
                          '2. Заморозка  (17)         | аномалия пропускает 2 хода\n'
                          '3. Побег      (15)         | пропуск боя, можно получить предмет'
                          )
                    
                    i = input('> ')

                    match i:
                        case '1':
                            if p.mana >= 7:
                                burning = 2
                                p.mana -= 7
                                hp_ch -= enemy.dmg / (p.res / 3)
                                print(f'урон от аномалии: {enemy.dmg / (p.res / 3)}\n')
                                print(f'Ваше здоровье: {hp_ch} | Здоровье аномалии: {enemy_hp}\n')
                                cont_game = input('> ')
                            
                            else:
                                print('У вас не хватает энергии')
                                cont_game = input('> ')

                        case '2':
                            if p.mana >= 17:
                                cold = 2
                                p.mana -= 17
                            
                            else:
                                print('У вас не хватает энергии')
                                cont_game = input('> ')

                        case '3':
                            if p.mana >= 15:
                                item = random.choice(['таблетка','лекарство','деньги'])
                                p.mana -= 15
                                if item == 'деньги':
                                    money = random.randint(5,50)
                                    its.add_item('деньги', money)

                                    print('Вы сбежали, найдя по дороге ' + item + f'({money})')
                                    cont_game = input('> ')
    
                                    return True, hp_ch

                                else:
                                    if item == 'таблетка':
                                        it_id = 'Капсула энкефалина'
                                    elif item == 'лекарство':
                                        it_id == 'Аптечка'

                                    its.add_item(item, 1)
                                    print('Вы сбежали, найдя по дороге ' + it_id + ' (1)')
                                    cont_game = input('> ')
                            
                            else:
                                print('У вас не хватает энергии')  
                                cont_game = input('> ') 

                    
                case '3':
                    print("\033[H\033[J", end="")
                    print(f'Ваше здоровье: {hp_ch}/{p.hp} | Ваша энергия: {p.mana}/{p.g_mana}\n')
                    its.display_items()
                    print('1. Восстаносить здоровье ' + str(инвентарь['лекарство']))
                    print('2. Восстановить энергию ' + str(инвентарь['таблетка']))
                    opt = (input('> '))
                    

                    while opt < '1' or opt > '2':
                        print('Выберите одну из опций')
                        opt = (input('> '))

                    match opt:
                        case '1': # здоровье
                            if инвентарь['лекарство'] > 0 and hp_ch < (p.hp-5):
                                hp_ch += 5
                                its.remove_item('лекарство', 1)
                                print(f'Ваше здоровье: {hp_ch}/{p.hp} | Здоровье аномалии: {enemy_hp}\n')
                                cont_game = input('> ')
                            
                            elif инвентарь['лекарство'] > 0 and hp_ch == (p.hp-5):
                                hp_ch = p.hp
                                its.remove_item('лекарство', 1)
                                print(f'Ваше здоровье: {hp_ch}/{p.hp} | Здоровье аномалии: {enemy_hp}\n')
                                cont_game = input('> ')
                            
                            elif инвентарь['лекарство'] == 0:
                                print('Вы не можете восстановить здоровье (нет Аптечек)')
                                cont_game = input('> ')

                        case '2': # мана
                            if инвентарь['таблетка'] > 0 and p.mana < (p.g_mana-5):
                                p.mana += 5
                                its.remove_item('таблетка', 1)
                                print(f'Ваша энергия: {p.mana}/{p.g_mana} | Здоровье аномалии: {enemy_hp}\n')
                                cont_game = input('> ')
                            
                            elif инвентарь['таблетка'] > 0 and p.mana == (p.g_mana-5):
                                p.mana = p.g_mana
                                its.remove_item('таблетка', 1)
                                print(f'Ваша энергия: {p.mana}/{p.g_mana} | Здоровье аномалии: {enemy_hp}\n')
                                cont_game = input('> ')
                            
                            elif инвентарь['таблетка'] == 0:
                                print('Вы не можете восстановить здоровье (нет Капсул энкефалина)')
                                cont_game = input('> ')
                            

                case '4':
                    hp_ch -= enemy.dmg / (p.res)
                    enemy_hp -= (enemy.dmg - 2) / enemy.res
                    print(f'урон от аномалии: {enemy.dmg / (p.res)}')
                    print(f'аномалия получила отражённый урон: {(enemy.dmg - 2) / enemy.res}')
                    cont_game = input('> ')

                    if enemy_hp > 0:
                        pass
                    else:
                        p.enk += 1
                        p.exp += enemy.exp
                        return True, hp_ch

                case _:
                    print('Выберите одну из опций\n')
                    print(f'Ваше здоровье: {hp_ch} | Здоровье аномалии: {enemy_hp}\n')
        
        if hp_ch <= 0:
            print('\nИгра окончена')
            quit()

        return False, hp_ch, None

