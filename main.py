from tkinter import *
from math import *
import sum
import subtraction
import multiply
import divide
import equalsto
import squareroot
import square
import factorial
import constantpie
import exponential
import sinf
import converter
import log
import signconvert
import decimal
import cosf
import tanf
import asinf
import acosf
import atanf
import sinhf
import coshf
import tanhf
import cube
display = ''  # For screen display
a = 0  # First Input
b = 0  # Second Input
c = 0  # Conditional Operation [1 = "+" , 2 = "-" , 3 = "*" , 4 = "/" , 5 = "To clear the memory on pressing any number after calculating with (=)"]
deg = False #By Default for radian only
# ---------------------------NUMBER CLICK----------------------------


def click(number):
    global a
    global b
    global c
    global display
    if c == 5:  # This value of "c" occurs after pressing "=". If this happens then fresh calculation will be started
        a = 0
        b = 0
        c = 0
        display = ''
        text_input.set(display)
    display = display + str(number)  # This is because string just add after itself instead of normal addition
    text_input.set(display)


# ---------------------BASIC ARITHMETIC FUNCTIONS---------------------

def importadd():
    global a
    global b
    global c
    global display

    a,b,c,display = sum.addition(a,b,c,display)
    text_input.set(a)


def importsubt():
    global a
    global b
    global c
    global display

    a,b,c,display= subtraction.subtraction(a,b,c,display)
    text_input.set(a)


def importmultiply():
    global a
    global b
    global c
    global display

    a,b,c,display=multiply.multiplication(a,b,c,display)
    text_input.set(a)


def importdivide():
    global a
    global b
    global c
    global display
    a,b,c,d=divide.division(a,b,c,display)
    text_input.set(a)

# ----------------DECIMAL AND SIGN CONVERTER-----------------------


def importsignconverter():
    global a
    global display
    a, display = signconvert.sign_converter(a,display)
    if a==0:
        text_input.set(display)
    elif display == '':
         text_input.set(a)

def importdec():
    global display
    display = decimal.decimal(display)
    text_input.set(display)


# ----------------------------EQUALS-------------------------------

def importequals():
    global a
    global b
    global c
    global display

    a,b,c,display = equalsto.equals(a,b,c,display)
    text_input.set(display)


# -----------------------Square root/ Power/ Cube Root

def importunderroot():
    global a
    global b
    global c
    global display

    a,b,c,display = squareroot.square_root(a,b,c,display)
    text_input.set(display)


def importsquare():
    global a
    global display
    a,display = square.square(a,display)
    text_input.set(display)

def importfact():
    global a
    global b
    global c
    global display

    a,b,c,display = factorial.fact(a,b,c,display)
    text_input.set(display)

# ------------------------CLEARING AND DELETING-----------------------


def allclear():
    global display
    global a
    global b
    global c
    display = ''
    a = 0
    b = 0
    c = 0
    text_input.set(display)


def clear():
    global display
    try:
        display = display[:-1]
        text_input.set(display)
    except:
        text_input.set('')


# ----------------------CONSTANTS-------------------------------------

def importpie():
    global a
    global b
    global c
    global display

    a,b,c,display = constantpie.pie(a,b,c,display)
    if a != 0 and b == 0:
        text_input.set(a)
    else:
        text_input.set(display)

def importexpo():
    global a
    global b
    global c
    global display

    a,b,c,display=exponential.expofunc(a,b,c,display)

    if a != 0 and b == 0:
        text_input.set(a)
    else:
        text_input.set(display)




# ----------------------RADIAN TO DEGREE-------------------------------------


def convert():
    global display
    global deg
    #a=radians(constant)
    print('Initial',deg)
    if deg==False:
        deg=True
        button_deg.configure(fg='purple',text='DEG')
    elif deg==True:
        deg=False
        button_deg.configure(text="RAD" , fg='DodgerBlue3')

def importconv():
    global display
    global deg

    display,deg = converter.convert(display,deg)
    if deg == True:
        button_deg.configure(fg='purple',text='DEG')
    elif deg == False:
        button_deg.configure(text="RAD" , fg='DodgerBlue3')



# -----------------TRIGONOMETRIC FUNCTIONS-------------------------------

def importsin():
    global a
    global display
    global deg
    global c

    a,display,c,deg = sinf.sin_fun(a,display,c,deg)
    text_input.set(display)


def importcos():
    global display
    global a
    global c
    global deg

    display,deg,a,c = cosf.cos_fun(display,deg,a,c)
    text_input.set(display)


def importtan():
    global display
    global a
    global c
    global deg

    display,deg,a,c = tanf.tan_fun(display,deg,a,c)
    if display == 90:
        text_input.set('∞')
    else:
        text_input.set(display)



# ------------------------------INVERSE TRIGONOMETRIC FUNCTIONS----------------


def importasin():
    global display
    global deg
    global a
    global c

    display,deg,a,c = asinf.arc_sin(display,deg,a,c)
    if display<=1 and display>=-1:
        text_input.set(display)
    else:
        text_input.set('ERROR')



def importacos():
    global display
    global deg
    global a
    global c

    display,deg,a,c = acosf.arc_cos(display,deg,a,c)
    if display<=1 and display>=-1:
        text_input.set(display)
    else:
        text_input.set('ERROR')


def importatan():
    global display
    global deg
    global a
    global c

    display,deg,a,c = atanf.arc_tan(display,deg,a,c)
    if display<=1 and display>=-1:
        text_input.set(display)
    else:
        text_input.set('ERROR')


# ----------------------------Hyp Trignometric Functions

def importsinh():
    global display
    global a

    display,a = sinhf.sinh_fun(display,a)
    text_input.set(display)

def importcosh():
    global display
    global a

    display,a = coshf.cosh_fun(display,a)
    text_input.set(display)

def importtanh():
    global display
    global a

    display,a = tanhf.tanh_fun(display,a)
    text_input.set(display)




# -----------------------------LOG-----------------------------------

def importlog():
    global a
    global b
    global c
    global display

    a,b,c,display = log.logarithm(a,b,c,display)
    if a == 0 and b == 0:
        text_input.set(display)
    else:
        text_input.set(a)

def importcube():
    global a
    global display
    a,display = cube.cube(a,display)
    text_input.set(display)

root = Tk()
# ---------------------GUI---------------------------------#

# Button1
button1 = Button(root, font=("Calibri",20,'bold'), text="1", command=lambda: click(1), activeforeground='RoyalBlue1',height=1,width=2,bg='gray87')
button1.grid(row=7, column=1)

# Button2
button2 = Button(root, font=("Calibri",20,'bold'), text="2", command=lambda: click(2), activeforeground='RoyalBlue1',height=1,width=2,bg='gray87')
button2.grid(row=7, column=2)

# Button3
button3 = Button(root, font=("Calibri",20,'bold'), text="3", command=lambda: click(3), activeforeground='RoyalBlue1',height=1,width=2,bg='gray87')
button3.grid(row=7, column=3)

# Button4
button4 = Button(root, font=("Calibri",20,'bold'), text="4", command=lambda: click(4), activeforeground='RoyalBlue1',height=1,width=2,bg='gray87')
button4.grid(row=6, column=1)

# Button5
button5 = Button(root, font=("Calibri",20,'bold'), text="5", command=lambda: click(5), activeforeground='RoyalBlue1',height=1,width=2,bg='gray87')
button5.grid(row=6, column=2)

# Button6
button6 = Button(root, font=("Calibri",20,'bold'), text="6", command=lambda: click(6), activeforeground='RoyalBlue1',height=1,width=2,bg='gray87')
button6.grid(row=6, column=3)

# Button7
button7 = Button(root, font=("Calibri",20,'bold'), text="7", command=lambda: click(7), activeforeground='RoyalBlue1',height=1,width=2,bg='gray87')
button7.grid(row=5, column=1)

# Button8
button8 = Button(root, font=("Calibri",20,'bold'), text="8", command=lambda: click(8), activeforeground='RoyalBlue1',height=1,width=2,bg='gray87')
button8.grid(row=5, column=2)

# Button9
button9 = Button(root, font=("Calibri",20,'bold'), text="9", command=lambda: click(9), activeforeground='RoyalBlue1',height=1,width=2,bg='gray87')
button9.grid(row=5, column=3)

# Button0
button0 = Button(root, font=("Calibri",20,'bold'), text="0", command=lambda: click(0), activeforeground='RoyalBlue1',height=1,width=2,bg='gray87')
button0.grid(row=8, column=2)

# Buttondecimal
buttondeci = Button(root, font=("Calibri",20,'bold'), text=" . ", command=lambda: importdec(),relief='flat',activeforeground='RoyalBlue1',height=1,width=2,bg='gray87')
buttondeci.grid(row=6, column=0)

#Button sin inverse
button0 = Button(root, font=("Calibri", 18), text="asin", command=lambda: importasin(),height=1,width=3,relief='flat',fg='purple',activeforeground='plum1')
button0.grid(row=4, column=0)

#Button cos inverse
button0 = Button(root, font=("Calibri", 18), text="acos", command=lambda: importacos(),height=1,width=3,relief='flat',fg='purple',activeforeground='plum1')
button0.grid(row=4, column=1)

#Button tan inverse
button0 = Button(root, font=("Calibri", 18), text="atan", command=lambda: importatan(),height=1,width=3,relief='flat',fg='purple',activeforeground='plum1')
button0.grid(row=4, column=2)

# Button_sin
button0 = Button(root, font=("Calibri", 19), text="sin", command=lambda: importsin(),height=1,width=3,relief='flat',fg='purple',activeforeground='plum1')
button0.grid(row=2, column=0)

# Button_cos
button0 = Button(root, font=("Calibri", 20), text="cos", command=lambda: importcos(),height=1,width=3,relief='flat',fg='purple',activeforeground='plum1')
button0.grid(row=2, column=1)

# Button_tan
button0 = Button(root, font=("Calibri", 20), text="tan", command=lambda: importtan(),height=1,width=3,relief='flat',fg='purple',activeforeground='plum1')
button0.grid(row=2, column=2)

#Button sinh
button0 = Button(root, font=("Calibri", 18), text="sinh", command=lambda: importsinh(),height=1,width=3,relief='flat',fg='purple',activeforeground='plum1')
button0.grid(row=3, column=0)

#Button cosh
button0 = Button(root, font=("Calibri", 18), text="cosh", command=lambda: importcosh(),height=1,width=3,relief='flat',fg='purple',activeforeground='plum1')
button0.grid(row=3, column=1)

#Button tanh
button0 = Button(root, font=("Calibri", 18), text="tanh", command=lambda: importtanh(),height=1,width=3,relief='flat',fg='purple',activeforeground='plum1')
button0.grid(row=3, column=2)

# Button_pie
button0 = Button(root, font=("arial", 20), text="π", command=lambda: importpie(),relief='flat', activeforeground='purple',bg='thistle',activebackground='seashell2')
button0.grid(row=8, column=1)

# Button_exponential
button0 = Button(root, font=("arial", 20), text="e", command=lambda: importexpo(),relief='flat', activeforeground='purple',bg='thistle',activebackground='seashell2')
button0.grid(row=8, column=3)

#Square Root
button1 = Button(root, font=("arial", 20), text="√", command=lambda: importunderroot(),relief='flat',activeforeground='gold',bg='LightSkyBlue1',activebackground='LightSteelBlue1',height=1,width=3)
button1.grid(row=2, column=4)

#Square
button1 = Button(root, font=("arial", 16), text=" x²", command=lambda: importsquare(),relief='flat', activeforeground='gold',bg='LightSkyBlue1',activebackground='LightSteelBlue1',height=1,width=3)
button1.grid(row=2, column=3,ipady=10)

#Factorial
button1 = Button(root, font=("Calibri", 18), text="!", command=lambda: importfact(),relief='flat', activeforeground='gold',bg='LightSkyBlue1',activebackground='LightSteelBlue1',height=1,width=3)
button1.grid(row=3, column=3)

#log
button1 = Button(root, font=("Calibri", 16), text="log", command=lambda:importlog(),relief='flat', activeforeground='gold',bg='LightSkyBlue1',activebackground='LightSteelBlue1',height=1,width=3)
button1.grid(row=3, column=4)

# Entry Box
text_input = StringVar()
entrybox = Entry(root, textvariable=text_input, justify="right", font=("arial", 20))
entrybox.grid(row=0,columnspan=7)

# All Clear
buttonclear = Button(root, font=("Calibri", 16), text="AC", command=lambda: allclear(),relief='flat',activeforeground='RoyalBlue1',height=1,width=2,bg='gray87')
buttonclear.grid(row=7, column=0, ipadx=1, ipady=4)

# Clear
buttonclear = Button(root, font=("Calibri", 18,'bold'), text="C", command=lambda: clear(),relief='flat',activeforeground='RoyalBlue1',height=1,width=2,bg='gray87')
buttonclear.grid(row=8, column=0, ipadx=1, ipady=4)

#Cube
buttonplus = Button(root, font=("Calibri",18), text="x^3", command=lambda:importcube(),relief='flat', activeforeground='gold',bg='LightSkyBlue1',activebackground='LightSteelBlue1',height=1,width=3)
buttonplus.grid(row=4, column=3,ipady=3)

# Equals
buttonequals = Button(root, font=("arial", 20), text="=", command=lambda: importequals(),relief='flat', activeforeground='gold',bg='LightSkyBlue1',activebackground='LightSteelBlue1')
buttonequals.grid(row=8, column=4)

# Addition
buttonplus = Button(root, font=("arial",20), text="+", command=lambda: importadd(),relief='flat', activeforeground='gold',bg='LightSkyBlue1',activebackground='LightSteelBlue1')
buttonplus.grid(row=7, column=4)

# Subtraction
buttonminus = Button(root, font=("arial", 20), text="-", command=lambda: importsubt(),relief='flat', activeforeground='gold',bg='LightSkyBlue1',activebackground='LightSteelBlue1')
buttonminus.grid(row=6, column=4)

# Multiplication
buttonmultily = Button(root, font=("arial", 20), text="x", command=lambda: importmultiply(),relief='flat', activeforeground='gold',bg='LightSkyBlue1',activebackground='LightSteelBlue1')
buttonmultily.grid(row=5, column=4)

# Division
buttondivide = Button(root, font=("arial", 20), text="÷", command=lambda: importdivide(),relief='flat', activeforeground='gold',bg='LightSkyBlue1',activebackground='LightSteelBlue1')
buttondivide.grid(row=4, column=4)

# Plus Minus Converter
button_plus_minus = Button(root, font=("arial", 20), text="±", command=lambda: importsignconverter(), relief='flat',activeforeground='gold')
button_plus_minus.grid(row=5, column=0)

button_deg = Button(root, font=("Calibri", 16,'bold'), text="RAD", command=lambda: convert(), relief='flat',activeforeground='coral',fg='DodgerBlue2')
button_deg.grid(row=1, column=0)

root.mainloop()
