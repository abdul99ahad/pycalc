from math import *
def tan_fun(display,deg,a,c):
    try:
        if a > 0:
            display = a
            a = 0
        else:
            pass
        if deg==True:
            display=float(display)
            if display !=90:
                display=tan(radians(display))
            else:
                pass
        elif deg==False:
            display=float(display)
            display=tan(display)
        if display == 90:
            text_input.set('∞')
    except:
        pass

    c = 5
    return display,deg,a,c
