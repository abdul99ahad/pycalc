def addition(a,b,c,display):  # After pressing "+" button this function will be called
    try:
        if a == 0 and b == 0:  # For the first time,the first input will go to "a",because a = b = 0
            a = float(display)
            if a % 2 == 1 or a % 2 == 0:  # If the input is whole number then ".0" will be removed
                a = int(display)
            display = ''


        elif a != 0 and b == 0:  # Now after pressing any operator for the second time,the second input will go to "b",because a != 0 and b == 0
            if c == 1:  # For previously pressed addition
                b = float(display)
                a = a + b
                if a % 2 == 1 or a % 2 == 0:
                    a = int(a)
                b = 0
                display = ''
            if c == 2:  # For previously pressed subtraction
                b = float(display)
                a = a - b
                if a % 2 == 1 or a % 2 == 0:
                    a = int(a)
                b = 0
                display = ''
            if c == 3:  # For previously pressed multiplication
                b = float(display)
                a = a * b
                if a % 2 == 1 or a % 2 == 0:
                    a = int(a)
                b = 0
                display = ''
            if c == 4:  # For previously pressed division
                b = float(display)
                if b == 0:  # If denominator is 0
                    text_input.set('∞')
                    a = b = 0
                    c = 5
                    display = ''
                if b != 0:  # If denominator is not 0
                    a = a / b
                    if a % 2 == 1 or a % 2 == 0:
                        a = int(a)
                    b = 0
                    display = ''
    except:
        pass

    c = 1  # The fingerprint of addition. It will be checked every time when a new function is executed

    return a,b,c,display
