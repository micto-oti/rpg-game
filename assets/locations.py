
class locations:
    def game_loc():
        print('1. Отдел контроля')
        print('2. Отдел исследования')
        print('3. Отдел подавления')
        opt = int(input('> '))
        
        match opt:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case _:
                print('выберите 1 из локаций')