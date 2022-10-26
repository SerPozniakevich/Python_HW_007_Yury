from calculation import calculation
from calc_loggining import read_log


def menu():
    flag = True
    while flag:
        print('Калькулятор приветствует вас')
        while True:
            print('Выберете действие:')
            print('1 - Выполнить вычесление')
            print('2 - Показать записи')
            print('3 - Выход')
            choice = input()
            if choice not in ['1', '2', '3']:
                print('Повторите ввод действия')
                continue
            if choice == '1':
                calculation()
                break
            elif choice == '2':
                read_log()
                break
            else:
                flag = False
                break


if __name__ == "__main__": # __name__ - функция, запускающая функцию "напрямую" из данного файла, а не по импорту
    menu()
