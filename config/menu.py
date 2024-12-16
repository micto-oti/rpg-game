class main_menu:
    def m_n():
        print('1. Начать игру')
        print('2. Продолжить игру')
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
        print('2. Способность')
        print('3. Предмет')
        print('4. Защита')
        opt = int(input('> '))
        
        while opt < 1 or opt > 4:
            print('Выберите одну из опций')
            opt = int(input('> '))

        match opt:
            case 1:
                return opt
            case 2:
                return opt
            case 3:
                return opt
            
class character_menu:
    def char_menu():
        print('1. Вернуться')
        print('2. Использовать предмет')
        print('3. Посмотреть характеристики')
        print('4. Выйти из игры')
        opt = int(input('> '))
        
        while opt < 1 or opt > 4:
            print('Выберите одну из опций')
            opt = int(input('> '))

        match opt:
            case 1:
                return opt
            case 2:
                return opt
            case 3:
                return opt
            case 4:
                quit()