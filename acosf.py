from math import *
def arc_cos(display,deg,a,c):
    try:
        if a > 0:
            display = a
            a = 0
        else:
            pass
        if deg==True:
            display=float(display)
            if display<=1 and display>=-1:
                display=acos(display)
                display=degrees(display)
            else:
                text_input.set('ERROR')
        elif deg == False:
            display = float(display)
            if display <= 1 and display >= -1:
                display = acos(display)
                display = radians(display)

            else:
                text_input.set('ERROR')
    except:
        pass
    c = 5
    return display,deg,a,c
