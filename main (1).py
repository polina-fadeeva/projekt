import sys

from check_and_pars import check, parse_argv, get_number_factors, check_correct_part, get_max_degree
from create_solution import solve


class MyPolynomialPars:
    a = 0
    b = 0
    c = 0
    max_degree = 0
    pow_num_dict = {}
    reduced_form = ''
    if_p = 0
    if_i = 0


def print_reduced_form(fac):
    list_keys = sorted(list(fac.pow_num_dict.keys()), reverse=True)
    z = 0

    for i in list_keys:
        l = 0

        if fac.pow_num_dict[i] != 0:
            if z == 0:
                z = 1
            else:
                fac.reduced_form += ' + '
            if fac.pow_num_dict[i] < 0:
                l = 1
            if l == 1:
                fac.reduced_form += '('
            fac.reduced_form += str(fac.pow_num_dict[i])
            if l == 1:
                fac.reduced_form += ')'
            if i != 0:
                fac.reduced_form += ' * X^' + str(i)

    if fac.reduced_form == "":
        fac.reduced_form = "0"
    fac.reduced_form += ' = 0'

    print('\nReduced form:', fac.reduced_form)
    print('Polynomial degree:', fac.max_degree)

    return 0


def get_abc(fac):
    if 0 in fac.pow_num_dict.keys():
        fac.c = fac.pow_num_dict[0]
    if 1 in fac.pow_num_dict.keys():
        fac.b = fac.pow_num_dict[1]
    if 2 in fac.pow_num_dict.keys():
        fac.a = fac.pow_num_dict[2]


def main(argv):
    fac = MyPolynomialPars
    equation, fac.if_i, fac.if_p = parse_argv(argv)
    check(equation)
    equation = equation.split()
    check_correct_part(equation)
    get_number_factors(equation, fac)
    get_max_degree(fac)
    get_abc(fac)
    print_reduced_form(fac)
    solve(fac)

    return 0


main(sys.argv)
