#Author: Ayan Noorani
#Date: 27 November 2021
#Purpose: Creates ahand of dominos
#============================================

import random
from tkinter import *
from tkinter import messagebox

#Purpose: A Domino
#Data Elements:
#   Value
#   Size
#   Diameter
#   Gap
#   Orientation
#   Faceup Status
#Methods:
#   __init__
#   __str__
#   getValue
#   setValue
#   flip
#   setOrientation
#   setSize
#   setface
#   randomize
#   draw
#====================================================================================================================================================================
class Domino:
    #Purpose: Initializes the data elements and sets diameter and gap accordingly. Validate and use default values if necessary.
    #Parameters: value, size, orientation, faceDown
    #Return/Output: N/A
    def __init__(self, value=1, size = 60, orientation = 'H', faceDown=False): #formally a constructor
        if value <= 0 or value > 66 or value//10 > 6 or value%10 > 6:
            self.randomize()
        else:
            self.value = value
            
        if size >= 30 and size <= 100:
            self.size = size
        else:
            self.size = 60

        if str(orientation) == "H" or str(orientation) == "V":
            self.orientation = orientation
        else:
            self.orientation = "H"
        self.faceDown=faceDown

        self.diameter = self.size // 5
        self.gap = self.diameter // 2

    #Purpose: returns the value of the domino as a formatted string
    #Parameters: N/A
    #Return/Output: string conversion
    def __str__(self):
        strDomino = "The value is: " + str(self.value) + '\nThe size is: ' + str(self.size) + '\nThe Orientation is: ' + str(self.orientation)
        return strDomino

    #Purpose: gets the value of the domino from the user (edit for valid values like getPositiveInteger)
    #Parameters: low, high, prompt
    #Return/Output: value, face, size and orientation
    def getValue (self, low, high, prompt):
        inputprompt = "Please enter the " + prompt + " in the range (" + str(low) + " - " + str(high) + "): "
        if prompt == 'orientation':
            r = ""
            while r != 'h' and r != 'H' and r != 'v' and r != 'V':
                r = str(input(inputprompt))
                return r
        elif prompt == 'face':
            f = ''
            while f != 'up' and f != 'down':
                f = str(input(inputprompt))
            return f
        elif prompt == 'value':
            v = 0
            while v < 1 or v < low or v > high:
                v = int(input(inputprompt))
            digit2 = str(v)[1]
            intv = int(digit2)
            while intv > 6:
                v = int(input(inputprompt))
                digit2 = str(v)[1]
                intv = int(digit2)
            return v
        else:
            n = 0
            while n < 1 or n < low or n > high:
                n = int(input(inputprompt))
            return n

    #Purpose: sets the value of the domino to a valid value obtained via parameter (otherwise 0 on error)
    #Parameters: N/A
    #Return/Output: N/A
    def setValue(self):
        self.value = self.getValue(0, 66, 'value')

    #Purpose: changes the value of the domino from XY to YX
    #Parameters: N/A
    #Return/Output: flipped string
    def flip(self):
        strValue = str(self.value)[::-1]
        return strValue

    #Purpose: sets the value of the domino’s orientation
    #Parameters: N/A
    #Return/Output: N/A
    def setOrientation(self):
        self.orientation = self.getValue('H', 'V', 'orientation')

    #Purpose: sets the value of the domino’s size to a valid value
    #Parameters: N/A
    #Return/Output: N/A
    def setSize(self):
        self.size = self.getValue(30, 100, 'size')

    #Purpose: sets the value of the domino’s faceup status
    #Parameters: N/A
    #Return/Output: N/A
    def setFace(self):
        self.faceDown = self.getValue('up', 'down', 'face')

    #Purpose: randomly sets the value of the domino to a new valid value, no parameters required
    #Parameters: N/A
    #Return/Output: random integer
    def randomize(self):
        self.value = random.randint(0, 66)
        return self.value

    #Purpose: draws the domino
    #Parameters: c, x, y, flip
    #Return/Output: The domino
    
    def draw(self, c, x = 0, y = 0, flip = False):
        if flip == True:
            value = int(self.flip())
        else:
            value = self.value
        self.drawHalf(c, x, y, value//10)
        if self.orientation == 'h' or self.orientation == 'H':
            self.drawHalf(c, x + self.size, y,  value%10)
        else:
            self.drawHalf(c, x, y +self.size, value % 10)

    #Purpose: Draws half the domino
    #Parameters: c, x, y, value
    #Return/Output: Half the domino
    def drawHalf(self, c, x, y, value):
        if self.faceDown == False:
            c.create_rectangle(x, y, x + self.size, y + self.size, width = 3, outline="black", fill="white")
            if value == 1:
                c.create_oval(x + 4*self.gap, y + 4*self.gap, x + 4*self.gap + self.diameter, y + 4*self.gap + self.diameter, fill ="black")
            elif value == 2:
                c.create_oval(x + self.gap, y + self.gap, x + self.gap + self.diameter, y + self.gap + self.diameter, fill ="black")
                c.create_oval(x + 7*self.gap, y + 7*self.gap, x + 7*self.gap + self.diameter, y + 7*self.gap + self.diameter, fill ="black")
            elif value == 3:
                c.create_oval(x + 4*self.gap, y + 4*self.gap, x + 4*self.gap + self.diameter, y + 4*self.gap + self.diameter, fill ="black")
                c.create_oval(x + self.gap, y + self.gap, x + self.gap + self.diameter, y + self.gap + self.diameter, fill ="black")
                c.create_oval(x + 7*self.gap, y + 7*self.gap, x + 7*self.gap + self.diameter, y + 7*self.gap + self.diameter, fill ="black")
            elif value == 4:
                c.create_oval(x + self.gap, y + self.gap, x + self.gap + self.diameter, y + self.gap + self.diameter, fill ="black")
                c.create_oval(x + 7*self.gap, y + self.gap, x + 7*self.gap + self.diameter, y + self.gap + self.diameter, fill ="black")
                c.create_oval(x + self.gap, y + 7*self.gap, x + self.gap + self.diameter, y + 7*self.gap + self.diameter, fill ="black")
                c.create_oval(x + 7*self.gap, y + 7*self.gap, x + 7*self.gap + self.diameter, y + 7*self.gap + self.diameter, fill ="black")
            elif value == 5:
                c.create_oval(x + self.gap, y + self.gap, x + self.gap + self.diameter, y + self.gap + self.diameter, fill ="black")
                c.create_oval(x + 7*self.gap, y + self.gap, x + 7*self.gap + self.diameter, y + self.gap + self.diameter, fill ="black")
                c.create_oval(x + self.gap, y + 7*self.gap, x + self.gap + self.diameter, y + 7*self.gap + self.diameter, fill ="black")
                c.create_oval(x + 7*self.gap, y + 7*self.gap, x + 7*self.gap + self.diameter, y + 7*self.gap + self.diameter, fill ="black")
                c.create_oval(x + 4*self.gap, y + 4*self.gap, x + 4*self.gap + self.diameter, y + 4*self.gap + self.diameter, fill ="black")
            elif value == 6:
                c.create_oval(x + self.gap, y + self.gap, x + self.gap + self.diameter, y + self.gap + self.diameter, fill ="black")
                c.create_oval(x + 7*self.gap, y + self.gap, x + 7*self.gap + self.diameter, y + self.gap + self.diameter, fill ="black")
                c.create_oval(x + self.gap, y + 7*self.gap, x + self.gap + self.diameter, y + 7*self.gap + self.diameter, fill ="black")
                c.create_oval(x + 7*self.gap, y + 7*self.gap, x + 7*self.gap + self.diameter, y + 7*self.gap + self.diameter, fill ="black")
                c.create_oval(x + self.gap, y + 4*self.gap, x + self.gap + self.diameter, y + 4*self.gap + self.diameter, fill ="black")
                c.create_oval(x + 7*self.gap, y + 4*self.gap, x + 7*self.gap + self.diameter, y + 4*self.gap + self.diameter, fill = "black")
            else:
                c.create_rectangle(x, y, x+self.size, y+self.size, width=1, outline='black', fill='white')
        else:
            c.create_rectangle(x, y, x + self.size, y + self.size, width = 3, outline="black", fill="grey")

#Purpose: A hand of dominos
#Data Elements:
#   firstDomino
#   secondDomino
#   thirdDomino
#   size
#Methods:
#   __init__
#   __str__
#   gsetSize
#   sort
#   roll
#   draw
#   getRun
#====================================================================================================================================================================
class HandOfDominos:
    
    #Purpose: creates the three domino object data elements and sets their size from a parameter. Validate input and use default values if necessary.
    #Parameters: size
    #Return/Output: N/A
    def __init__(self, size=60): #formally a constructor
        if size >= 30 or size <=100:
            self.size = size
        else:
            size = 60
        self.firstDomino = Domino(size = size)
        self.secondDomino = Domino(size = size)
        self.thirdDomino = Domino(size = size)

    #Purpose: returns the value of the hand object as a string the three values obtained from each of the three domino data elements.
    #Parameters: N/A
    #Return/Output: String conversion
    def __str__(self):
        strReturnDom1 = str(self.firstDomino.__str__())
        strReturnDom2 = str(self.secondDomino.__str__())
        strReturnDom3 = str(self.thirdDomino.__str__())
        return 'Domino 1\n' + strReturnDom1 + '\n\nDomino 2\n' + strReturnDom2 + '\n\nDomino 3\n' + strReturnDom3

    #Purpose: sets the value of the dominos’ sizes within the hand to a valid value
    #Parameters: size
    #Return/Output: Valid size
    def setSize(self, size):
        if size >= 30 or size <=100:
            self.size = size
        else:
            size = 60
        self.firstDomino = Domino(size = size)
        self.secondDomino = Domino(size = size)
        self.thirdDomino = Domino(size = size)

    #Purpose: compares 2 given domino values
    #Parameters: x, y
    #Return/Output: equal, greater or less
    def compare(self, x, y):
        if x.value == y.value:
            return 'equal'
        elif int(x.flip()) == y.value:
            return 'equal'
        elif x.value > y.value:
            return 'greater'
        else:
            return 'less'

    #Purpose: rearranges the three dominos so that the first is the smallest and third is the largest by calling the compare method three times
    #Parameters: N/A
    #Return/Output: domino values in a sorted order
    def sort(self):
        if self.compare(self.firstDomino, self.secondDomino) == 'greater':
            self.firstDomino,self.secondDomino = self.secondDomino,self.firstDomino
        if self.compare(self.firstDomino, self.thirdDomino) == 'greater':
            self.firstDomino,self.thirdDomino = self.thirdDomino,self.firstDomino
        if self.compare(self.secondDomino, self.thirdDomino) == 'greater':
            self.secondDomino,self.thirdDomino = self.thirdDomino,self.secondDomino

    #Purpose: randomizes each of the hand’s three dominos, becoming a new valid set of values
    #Parameters: N/A
    #Return/Output: three random domino values
    def roll(self):
        self.firstDomino.randomize()
        self.secondDomino.randomize()
        self.thirdDomino.randomize()

    #Purpose: draws the three dominos in a line
    #Parameters: c, x, y
    #Return/Output: three dominoes drawn on a canvas
    def draw(self, c, x, y):
        self.firstDomino.draw(c,x,y)
        self.secondDomino.draw(c,x*4+self.size, y)
        self.thirdDomino.draw(c, x*8+self.size*2,y)

    #Purpose: obtains the individual digits of each of the values for the three dominos
    #Parameters: domino, digit
    #Return/Output: first and second digits
    def getDigit(self, domino, digit=1):
        firstDigit = int(domino.value//10)
        secondDigit = int(domino.value%10)
        if digit == 1:
            return firstDigit
        else:
            return secondDigit
        
    #Purpose: checks to see if all of the values have a common digit using listsh
    #Parameters:  N/A
    #Return/Output: Boolean variable
    def run1(self):
        value = False
        dominostr = ""
        x=0
        y=0
        dominostr = str(self.firstDomino.value) + str(self.secondDomino.value) + str(self.thirdDomino.value)
        dominolist = []
        dominolist.append(str(self.firstDomino.value))
        dominolist.append(str(self.secondDomino.value))
        dominolist.append(str(self.thirdDomino.value))
        for c in dominostr:
            for e in dominolist:
                if c in e:
                    x += 1
            if x == 3:
                value = True
                y += 1
            if y > 4:
                value = False
            x = 0
        return value

    #Purpose: checks to see if two values have a common digit using lists
    #Parameters: N/A
    #Return/Output: Boolean variable
    def run2(self):
        value = False
        dominostr = ""
        x=0
        y=0
        dominostr = str(self.firstDomino.value) + str(self.secondDomino.value) + str(self.thirdDomino.value)
        dominolist = []
        dominolist.append(str(self.firstDomino.value))
        dominolist.append(str(self.secondDomino.value))
        dominolist.append(str(self.thirdDomino.value))
        for c in dominostr:
            for e in dominolist:
                if c in e:
                    x += 1
            if x == 2:
                value = True
                y += 1
            if y > 1:
                value = False
        return value

    #Purpose: determines the largest ‘Run’ of the hand
    #Parameters: N/A
    #Return/Output: run of 0, 2 or 3
    def getRun(self):
        v1d1 = self.getDigit(self.firstDomino, 1)
        v1d2 = self.getDigit(self.firstDomino, 2)
        v2d1 = self.getDigit(self.secondDomino, 1)
        v2d2 = self.getDigit(self.secondDomino, 2)
        v3d1 = self.getDigit(self.thirdDomino, 1)
        v3d2 = self.getDigit(self.thirdDomino, 2)
        if v1d1 != v2d1 and v1d1 != v2d2 and v1d1 != v3d1 and v1d1 != v3d2 and v1d2 != v2d1 and v1d2 != v2d2 and v1d2 != v3d1 and v1d2 != v3d2 and v2d1 != v3d1 and v2d2 != v3d1 and v2d1 != v3d2 and v2d2 != v3d2:
            return 0
        elif (self.firstDomino.value != self.secondDomino.value != self.thirdDomino.value) and (self.run2() == True or self.run1() == True): #((v1d1 == v2d1 == v3d1 or v1d1 == v2d1 == v3d2 or v1d1 == v2d2 == v3d1 or v1d1 == v2d2 == v3d2 or v1d2 == v2d1 == v3d1 or v1d2 == v2d1 == v3d2 or v1d2 == v2d2 == v3d1 or v1d2 == v2d2 == v3d2) or (self.run2() == True)):
            return 2
        else:
            return 3



#main=============================================================================================
handOfDomino = HandOfDominos(size=random.randint(30, 100))

def clear():
    canvas.delete('all')
    dominoRun.set('')

def about():
    x = 0
    print("""Copyright (c) 2001-2018 Python Software Foundation.\nAll Rights Reserved.\nCopyright (c) 2000 BeOpen.com.\n\nCopyright (c) 1995-2001 Corporation for National Research Initiatives.\nAll Rights Reserved.\n\nCopyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.\nAll Rights Reserved.\n\n\nA. HISTORY OF THE SOFTWARE\n==========================\n\nPython was created in the early 1990s by Guido van Rossum at Stichting Mathematisch Centrum (CWI, see http://www.cwi.nl) in the Netherlands as a successor of a language called ABC.  Guido remains Python'sprincipal author, although it includes many contributions from others.\n\nIn 1995, Guido continued his work on Python at the Corporation for\nNational Research Initiatives (CNRI, see http://www.cnri.reston.va.us)\nin Reston, Virginia where he released several versions of the software.\n\nIn May 2000, Guido and the Python core development team moved to BeOpen.com to form the BeOpen PythonLabs team.  In October of the same year, the PythonLabs team moved to Digital Creations, which became Zope Corporation.  In 2001, the Python Software Foundation (PSF, see https://www.python.org/psf/) was formed, a non-profit organization created specifically to own Python-related Intellectual Property.\nZope Corporation was a sponsoring member of the PSF.\n\nAll Python releases are Open Source (see http://www.opensource.org for the Open Source Definition).  Historically, most, but not all, Python""")
    return x

def newHand():
    handOfDomino.setSize(doubleDominoSize.get())
    handOfDomino.roll()
    canvas.delete('all')
    handOfDomino.draw(canvas, 50, 10)
    handOfDomino.sort()
    handOfDomino.draw(canvas, 50, 200)
    dominoRun.set('Run is: ' + str(handOfDomino.getRun()))


def simulation():
    runZero = 0
    runTwo = 0
    runThree = 0
    for i in range(1,10001):
        handOfDominos = HandOfDominos()
        handOfDominos.roll()
        run = handOfDominos.getRun()
        if run == 0:
            runZero += 1
        elif run == 2:
            runTwo += 1
        elif run == 3:
            runThree += 1
        zero.set(str(runZero) + ' - ' + str(round(runZero/10000*100, 2)) + '%')
        two.set(str(runTwo) + ' - ' + str(round(runTwo/10000*100, 2)) + '%')
        three.set(str(runThree) + ' - ' + str(round(runThree/10000*100, 2)) + '%')
    



def keyPressed(event):
    pass

root = Tk()
root.title('Dominos')
root.config(bg='cyan')
doubleDominoSize = DoubleVar(0)
# display the menu
newHandbtn = Button(root, text = 'New Hand', command = lambda:newHand())
newHandbtn.grid(column=1, row = 0)
sizeScale = Scale(root, from_=30, to=100, resolution=1, orient=HORIZONTAL, variable = doubleDominoSize)
sizeScale.grid(column=2, row=0)
clearbtn = Button(root, text='Clear Canvas', command = lambda:clear())
clearbtn.grid(column=3, row=0)
canvas = Canvas(width = 800, height = 300)
canvas.bind('<Key>', keyPressed)
canvas.config(background = 'cyan')
dominoRun = StringVar()
zero = StringVar()
two = StringVar()
three = StringVar()
zerolabel = Label(root, text = 'Amount of run=0', bg = 'cyan', font = ("Arial", "12", "bold"))
twolabel = Label(root, text = 'Amount of run=2', bg = 'cyan', font = ("Arial", "12", "bold"))
threelabel = Label(root, text = 'Amount of run=3', bg = 'cyan', font = ("Arial", "12", "bold"))
runlbl = Label(root, textvariable=dominoRun, bg = 'cyan', font = ("Arial", "12", "bold"))
zerolbl = Label(root, textvariable=zero, bg = 'cyan', font = ("Arial", "12", "bold"))
twolbl = Label(root, textvariable=two, bg = 'cyan', font = ("Arial", "12", "bold"))
threelbl = Label(root, textvariable=three, bg = 'cyan', font = ("Arial", "12", "bold"))
canvas.grid(column=1, row = 1, columnspan=3, rowspan=3)
simulationbtn = Button(root, text='New Simulation', command = lambda:simulation())
simulationbtn.grid(column=2, row=4)


menubar = Menu(root)
root.config(menu=menubar)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New Hand", command=newHand)
filemenu.add_command(label='New Simulation', command=lambda:simulation())
filemenu.add_separator()
filemenu.add_command(label="Exit",command=lambda:root.destroy())
menubar.add_cascade(label="File", menu=filemenu)
# create more pulldown menus
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

runlbl.grid(column=2, row=2)
zerolabel.grid(column=1, row=5)
twolabel.grid(column=2, row=5)
threelabel.grid(column=3, row=5)
zerolbl.grid(column=1, row=6)
twolbl.grid(column=2, row=6)
threelbl.grid(column=3, row=6)
canvas.focus_set()
mainloop()
