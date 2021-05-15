import sys


class TextColors:
    HEADER = '\033[95m'
    OK_BLUE = '\033[94m'
    OK_GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    EN_DC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def printUsage():
    print(TextColors.OK_GREEN + 'USAGE:\n >>> python3 main.py [flag] "polynomial equation"\n' + TextColors.EN_DC)
    print("FLAGS:")
    print(' -h\tdisplay help and exit')
    print(' -p\tshow equation information')
    print(' -P\tshow graph')


def exit_with_error(error):
    printHelp = False
    if error == -1:
        message = 'No polynomial equation is given :C\n'
        printHelp = True
    elif error == -2:
        message = 'Wrong parameters are given :C\n'
        printHelp = True
    elif error == -5:
        message = 'Lexical error in the equation :C\n'
    elif error == -4:
        message = "The '=' symbol is missing !!\n"
    elif error == -6:
        message = 'The polynomial degree is strictly greater than 2, I can\'t solve.\n'
    elif error == -3:
        message = "Syntax error, the '=' should appear only once !!\n"
    else:
        message = TextColors.WARNING + 'Are you sure to know how to call this function ? (Error code: ' + str(
            error) + ')'

    print(TextColors.FAIL + '\nERROR: ' + message + TextColors.EN_DC)

    if printHelp:
        printUsage()
    sys.exit(2)

