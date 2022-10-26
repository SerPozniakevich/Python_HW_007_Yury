from input_data import input_number, input_operation
from calc_op import calc_sum, calc_mult, calc_sub, calc_div
from calc_loggining import write_log


def calculation():
    a = input_number()
    b = input_number()
    op = input_operation()
    if op == '1':
        res = calc_sum(a, b)
        op_pr = '+'
    elif op =='2':
        res = calc_sub(a, b)
        op_pr = '-'
    elif op == '3':
        res = calc_mult(a, b)
        op_pr = '*'
    elif op == '4':
        res = calc_div(a, b)
        op_pr = '/'
    print(f'{a} {op_pr} {b} = {res}')
    write_log(a, b, op_pr, res)
