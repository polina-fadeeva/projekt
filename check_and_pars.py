import re
import sys

from error import exit_with_error, printUsage


def check(eq):
    s = re.sub('[^0-9X. \-+*^=]', '', eq)
    if s != eq:
        exit_with_error(-2)

    eq = re.sub(' ', '', eq)
    if eq.count('=') > 1:
        exit_with_error(-3)
    elif eq.count('=') == 0:
        exit_with_error(-4)

    if len(eq) < 3:
        exit_with_error(-5)

    if not eq[-1].isdigit():
        exit_with_error(-5)


def check_correct_part(eq):
    for i in range(len(eq) - 1):
        if eq[i] == '-' or eq[i] == '+':
            if not (eq[i + 1][0].isdigit() or eq[i + 1][0] == 'X'):
                exit_with_error(-5)

        elif eq[i] == '*':
            if eq[i + 1][0] != 'X':
                exit_with_error(-5)

        elif eq[i][0].isdigit():
            if eq[i].count('.') > 1:
                exit_with_error(-5)
            for n in eq[i]:
                if not (n.isdigit() or n == '.'):
                    exit_with_error(-5)

        elif eq[i][0] == 'X':
            if eq[i].count('X') > 1 or eq[i].count('^') > 1:
                exit_with_error(-5)

            if len(eq[i]) > 1:
                if eq[i][1] != '^':
                    exit_with_error(-5)
                else:
                    eq_str = re.sub('X', '', eq[i])
                    eq_str = re.sub('\^', '', eq_str)
                    for n in eq_str:
                        if not n.isdigit():
                            exit_with_error(-5)
            if not (eq[i + 1] == '+' or eq[i + 1] == '-' or eq[i + 1] == '='):
                exit_with_error(-5)

        elif eq[i] == '=':
            if not (eq[i + 1][0].isdigit() or eq[i + 1][0] == 'X' or eq[i + 1] == '-'):
                exit_with_error(-5)
        else:
            exit_with_error(-5)

    if not (eq[0][0].isdigit() or eq[0][0] == 'X' or eq[0][0] == '-'):
        exit_with_error(-5)

    if not (eq[-1][-1].isdigit() or eq[-1][-1] == 'X'):
        print(eq[0][0])
        print(eq)
        exit_with_error(-4)


def parse_argv(argv):
    flag_1 = 0
    flag_2 = 0
    equation = ""
    argc = len(argv)
    # вывод ошибки при отстутствии аргументов
    if argc == 1:
        exit_with_error(-1)
    elif sys.argv[1] == "-h":
        printUsage()
        sys.exit(2)
    elif sys.argv[1] == "-p" or sys.argv[1] == "-P":
        if argc == 2:
            exit_with_error(-1)
        elif argc > 3:
            exit_with_error(-2)

        # бонусы
        if sys.argv[1] == "-p":
            flag_1 = 1
        else:
            flag_2 = 1
        equation = sys.argv[2]
    elif argc == 2:
        equation = sys.argv[1]
    else:
        exit_with_error(-2)

    return equation, flag_1, flag_2


def get_number_factors(eq, fac):
    is_n = 0
    i = 1
    n = 0
    z = 1
    pow_ = 0

    for j, ch in enumerate(eq):

        if ch == '-' or ch == '+' or ch == '=' or j == len(eq) - 1:
            if ch[0] == 'X':
                if ch == 'X':
                    pow_ = 1
                else:
                    ch = ch.replace('X', '').replace('^', '')
                    pow_ = int(ch)
                n = 1 if is_n == 0 else n
            elif ch[0].isdigit():
                is_n = 1
                n = float(ch)

                n = 1 if is_n == 0 else n

            if pow_ in fac.pow_num_dict.keys():
                fac.pow_num_dict[pow_] += i * z * n
            else:
                fac.pow_num_dict[pow_] = i * z * n

            n = 0
            z = 1
            pow_ = 0
            is_n = 0

            if ch == '-':
                z = -1
            elif ch == '+':
                z = 1
            else:
                i = -1

        elif ch[0].isdigit():
            is_n = 1
            n = float(ch)

        elif ch[0] == 'X':
            if ch == 'X':
                pow_ = 1
                n = 1 if is_n == 0 else n
            else:
                ch = ch.replace('X', '').replace('^', '')
                pow_ = int(ch)

            n = 1 if is_n == 0 else n


def get_max_degree(fac):
    if fac.a != 0:
        fac.max_degree = 2
    elif fac.b != 0:
        fac.max_degree = 1
    
    for key in fac.pow_num_dict.keys():
        if key > fac.max_degree and fac.pow_num_dict[key] != 0:
            fac.max_degree = key
