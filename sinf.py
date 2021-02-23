from math import *
def sin_fun(a,display,c,deg):

    try:
        if a > 0:
            display = a
            a = 0
        else:
            pass

        if deg==True:
            display=float(display)
            display=sin(radians(display))

        elif deg==False:
            display=float(display)
            display=sin(display)
        text_input.set(display)
    except:
        pass
    c = 5
    return a,display,c,deg
