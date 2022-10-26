from datetime import datetime

FILE_NAME = "calc_log.csv"


def write_log(num1, num2, operation, result):
    with open(FILE_NAME, "a") as f:
        f.write(f"\n{datetime.now().strftime('%d.%m.%Y. %H:%M')}.\
         Введены числа: {num1}, {num2}. Операция {operation}. Результат {result}")


def read_log():
    with open(FILE_NAME, "r") as f:
        print(f.read())