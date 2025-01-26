""" import sys
sys.path.append(r'E:\projects\github\rpg-game\assets')
import items
 """
class main_menu:
    def m_n():
        print('1. Начать игру')
        print('2. Продолжить игру | (пока не реализовано)')
        print('3. Выход')
        opt = int(input('> '))

        
        while opt < 1 or opt > 3:
            print('Выберите одну из опций')
            opt = int(input('> '))

        if opt == 3:
            quit()
        else:
            return opt

class battle_menu:
    def b_m():
        print('1. Физ. атака')
        print('2. Способность | (пока что не реализовано))')
        print('3. Предмет')
        print('4. Защита')
        opt = (input('> '))

        """ 
        while opt < '1' or opt > '4':
            print('Выберите одну из опций')
            opt = (input('> '))
 """
        match opt:
            case '1':
                return opt
            case '2':
                return opt
            case '3':
                return opt
            case '4':
                return opt
            
class character_menu:
    def char_menu(inventory):
        print('1. Вернуться к игре')
        print('2. Использовать предмет')
        print('3. Посмотреть характеристики')
        print('4. Выйти из игры')
        opt = (input('> '))
        
        while opt < '1' or opt > '4':
            print('Выберите одну из опций')
            opt = (input('> '))

        match int(opt):
            case 1:
                return opt

            case 2:
                print(f'1. Использовать лекарство ({inventory[0]})')
                print(f'2. Использовать таблетку ({inventory[1]})')
                print(f'3. Вернуться в меню')
                choose = (input('> '))
        
                while choose < '1' or choose > '3':
                    print('Выберите одну из опций')
                    choose = (input('> '))
                
                match choose:
                    case '1':
                        choose = int(choose) + 6
                    case '2':
                        choose = int(choose) + 7
                    case '3':
                        choose == 999

                return choose
                
            case 3:
                return opt
            case 4:
                quit()
