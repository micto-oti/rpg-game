class main_menu:
    def m_n(self):
        print('1. Начать игру')
        print('2. Продолжить игру')
        print('3. Выход')
        opt = int(input('> '))
        if opt == 3:
            quit()

class battle_menu:
    def b_m(self):
        print('1. Физ. атака')
        print('2. Способность')
        print('3. Предмет')
        opt = int(input('> '))