from math import *
def tanh_fun(display,a):
    if a>0:
        display = a
    display = float(display)
    display = tanh(display)
    return display,a
