def green_print(text):
    GREEN = '\033[1;32;48m'
    END = '\033[1;37;0m'
    print('{}{}{}'.format(GREEN, text, END))

def red_print(text):
    RED = '\033[1;31;48m'
    END = '\033[1;37;0m'
    print('{}{}{}'.format(RED, text, END))

