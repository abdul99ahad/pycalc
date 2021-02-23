from math import *
def cos_fun(display,deg,a,c):
    try:
        if a > 0:
            display = a
            a = 0
        else:
            pass
        if deg==True:
            display=float(display)
            display=cos(radians(display))

        elif deg==False:
            display=float(display)
            display=cos(display)

    except:
        pass

    c = 5
    return display,deg,a,c
