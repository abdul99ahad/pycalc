from math import *
def fact(a,b,c,display):
    if a == 0 and b == 0:
        if display == '':
            text_input.set('ERROR')
            a = b = 0
            c = 5
            display = ''
        if display != '':
            a = int(display)
            if a < 0:
                text_input.set('ERROR')
                a = b = 0
                c = 5
                display = ''
            if a >= 0:
                a = factorial(a)
                display = str(a)
                a = 0

    if a != 0 and b == 0:
        if display == '':
            text_input.set('ERROR')
            a = b = 0
            c = 5
            display = ''
        if display != '':
            b = int(display)
            if b < 0:
                text_input.set('ERROR')
                a = b = 0
                c = 5
                display = ''
            if b >= 0:
                if c == 1:
                    b = float(display)
                    b = factorial(b)
                    a = a + b
                    display = str(a)
                    a = b = 0

                if c == 2:
                    b = float(display)
                    b = factorial(b)
                    a = a - b
                    display = str(a)
                    a = b = 0

                if c == 3:
                    b = float(display)
                    b = factorial(b)
                    a = a * b
                    display = str(a)
                    a = b = 0

                if c == 4:
                    b = float(display)
                    b = factorial(b)
                    a = a / b
                    display = str(a)
                    a = b = 0

    return a,b,c,display
