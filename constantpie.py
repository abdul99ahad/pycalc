from math import *
def pie(a,b,c,display):

    if a == 0 and b == 0:
        if display == '':
            a = pi
        if display != '':
            a = float(display)
            a = a * pi
        display = str(a)
        a = b = 0

    if a != 0 and b == 0:
        if c == 1:
            if display == '':
                b = pi
            if display != '':
                b = float(display)
                b = b * pi
            a = a + b
            b = 0
            display = ''

        if c == 2:
            if display == '':
                b = pi
            if display != '':
                b = float(display)
                b = b * pi
            a = a - b
            b = 0
            display = ''

        if c == 3:
            if display == '':
                b = pi
            if display != '':
                b = float(display)
                b = b * pi
            a = a * b
            b = 0
            display = ''

        if c == 4:
            if display == '':
                b = pi
            if display != '':
                b = float(display)
                b = b * pi
            a = a / b
            b = 0
            display = ''

    return a,b,c,display
