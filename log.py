from math import *
def logarithm(a,b,c,display):

    if a == 0 and b == 0:
        if display == '':
            text_input.set('ERROR')
            a = b = 0
            c = 5
        if display != '':
            display = float(display)
            display = log(display)

            c = 5

    if a != 0 and b == 0:
        if display == '':
            text_input.set('ERROR')
            a = b = 0
            c = 5
        if display != '':
            if c == 1:
                b = float(display)
                b = log(b)
                a = a + b
                display = ''
                b = 0

            if c == 2:
                b = float(display)
                b = log(b)
                a = a - b
                display = ''
                b = 0

            if c == 3:
                b = float(display)
                b = log(b)
                a = a * b
                display = ''
                b = 0

            if c == 4:
                b = float(display)
                b = log(b)
                a = a / b
                display = ''
                b = 0

    return a,b,c,display
