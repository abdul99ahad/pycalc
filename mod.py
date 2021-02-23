def mod(a,display,c):
    try:
        display = float(a)
        if a % 2 == 1 or a % 2 == 0:# If the input is whole number then ".0" will be removed
            a = int(display)
            display = ''
        c=6
    except:
        pass
    return a,display,c
