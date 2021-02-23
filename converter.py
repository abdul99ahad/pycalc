deg = False
def convert(display,deg):
    #a=radians(constant)
    print('Initial',deg)
    deg = False
    if deg==False:
        deg=True
        #button_deg.configure(fg='purple',text='DEG')
    elif deg==True:
        deg=False
        #button_deg.configure(text="RAD" , fg='DodgerBlue3')

    return display,deg
