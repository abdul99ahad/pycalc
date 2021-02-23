from math import *
def expofunc(a,b,c,display):

    if a == 0 and b == 0:
        if display == '':
            a = e
        if display != '':
            a = float(display)
            a = a * e
        display = str(a)
        a = b = 0
    if a != 0 and b == 0:
        if c == 1:
            if display == '':
                b = e
            if display != '':
                b = float(display)
                b = b * e
            a = a + b
            b = 0
            display = ''

        if c == 2:
            if display == '':
                b = e
            if display != '':
                b = float(display)
                b = b * e
            a = a - b
            b = 0
            display = ''

        if c == 3:
            if display == '':
                b = e
            if display != '':
                b = float(display)
                b = b * e
            a = a * b
            b = 0
            display = ''

        if c == 4:
            if display == '':
                b = e
            if display != '':
                b = float(display)
                b = b * e
            a = a / b
            b = 0
            display = ''

    return a,b,c,display
