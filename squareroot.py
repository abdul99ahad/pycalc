def square_root(a,b,c,display):


    if a == 0 and b == 0:
        a = float(display)
        a = a ** 0.5
        if a % 2 == 1 or a % 2 == 0:
            a = int(a)
        display = str(a)
        a = 0

    if a != 0 and b == 0:
        if c == 1:
            b = float(display)
            b = b ** 0.5
            if b % 2 == 1 or b % 2 == 0:
                b = int(b)
            a = a + b
            display = str(a)
            a = b = 0
        if c == 2:
            b = float(display)
            b = b ** 0.5
            if b % 2 == 1 or b % 2 == 0:
                b = int(b)
            a = a - b
            display = str(a)
            a = b = 0
        if c == 3:
            b = float(display)
            b = b ** 0.5
            if b % 2 == 1 or b % 2 == 0:
                b = int(b)
            a = a * b
            display = str(a)
            a = b = 0
        if c == 4:
            b = float(display)
            b = b ** 0.5
            if b % 2 == 1 or b % 2 == 0:
                b = int(b)
            if b == 0:
                text_input.set('ERROR')
                a = b = 0
                c = 5
                display = ''
            if b != 0:
                a = a / b
                display = str(a)
                a = b = 0
    return a,b,c,display
