def sign_converter(a,display):

    if a == 0:
        display = float(display)
        if display > 0:
            display = str(display)
            display = '-' + display
            display = float(display)
            if display % 2 == 0 or display % 2 == 1:
                display = int(display)
            display = str(display)

        elif display < 0:
            display = str(display)
            display = display[1:]
            display = float(display)
            if display % 2 == 0 or display % 2 == 1:
                display = int(display)
            display = str(display)


    if display == '':
        a = float(a)
        if a > 0:
            a = str(a)
            a = '-' + a
            a = float(a)
            if a % 2 == 0 or a % 2 == 1:
                a = int(a)
                a = str(a)

        elif a < 0:
            a = str(a)
            a = a[1:]
            a = float(a)
            if a % 2 == 0 or a % 2 == 1:
                a = int(a)
                a = str(a)
    return a,display
