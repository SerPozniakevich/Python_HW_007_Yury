

def input_number():
    while True:
        a = input('Введите число: ')
        try:
            return float(a)
        except:
            try:
                x = float(a.strip('j')) # strip - обрезает указанный символ (j)
                while True:
                    y = input('Введите реальную часть комплексного числа: ')
                    try:
                        return complex(float(y), x)
                    except:
                        print('Ошибка ввода. Попробуйте снова: ')
            except:
                print('Ошибка ввода. Попробуйте снова: ')



def input_operation():
    while True:
        print('Введите номер операции: ')
        print('1 - Сложение (+)')
        print('2 - Вычитание (-)')
        print('3 - Умножение (*)')
        print('4 - Деление (/)')
        op = input()
        if op not in ['1', '2', '3', '4']:
            print('Введите ещё раз желаемую операцию: ')
            continue
        return op
