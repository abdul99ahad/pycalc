def cube(a,display):
    try:
        if a > 0:
                display = a
                a = 0
        else:
            pass
        display=float(display)
        display=display**3
        if display %2 ==0 or display % 2 == 1:
            display=int(display)
        else:
            pass
    except:
        pass
    return a,display
