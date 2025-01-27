""" import sys
sys.path.append(r'E:\projects\github\rpg-game\assets')
import items
 """
class main_menu:
    def m_n():
        print('1. Начать игру')
#        print('2. Продолжить игру | (пока не реализовано)')
        print('2. Выход')
        opt = int(input('> '))

        
        while opt < 1 or opt > 2:
            print('Выберите одну из опций')
            opt = int(input('> '))

        if opt == 2:
            quit()
        else:
            return opt

class battle_menu:
    def b_m():
        print('1. Физ. атака  | обычная атака')
        print('2. Способность | (пока что не реализовано))')
        print('3. Предмет     | используйте полученные предметы')
        print('4. Защита      | следующая атака аномалии нанесёт меньше урона, а также отразит часть в неё')
        opt = (input('> '))

        while opt < '1' or opt > '4':
            print('Выберите одну из опций')
            opt = (input('> '))

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
    def char_menu():
        print("\033[H\033[J", end="")
        print('1. Вернуться к игре')
        print('2. Использовать предмет')
        print('3. Посмотреть характеристики')
        print('4. Магазин')
        print('5. Выйти из игры')
        opt = (input('> '))
        
        while opt < '1' or opt > '5':
            print('Выберите одну из опций')
            opt = (input('> '))

        opt = int(opt)

        if opt == 5:
            quit()
        
        else:
            return opt
