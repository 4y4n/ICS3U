#Author: Ayan Noorani
#Date: Otober 31st 2021
#purpose: Convert star pattern code into functions and include GUI

from tkinter import*
from tkinter import messagebox

root = Tk()
mode = StringVar("")
fnt = IntVar(0)
fnt.set(value="null")
attr = IntVar(0)
attr.set(value="null")
doublePatternSize = DoubleVar(0)



def displaySquare(size=1, fill=True):
    if fill == True:
        displaySolidSquare(size)
    else:
        displayHollowSquare(size)

def displayTriangle(size=1, fill=True):
    if fill==True:
        displaySolidTriangle(size)
    else:
        displayHollowTriangle(size)

def displayDiamond(size=1, fill=True):
    if fill==True:
        displaySolidDiamond(size)
    else:
        displayHollowDiamond(size)

def displaySolidSquare(patternSize=1):
    y = 1
    s = ""
    while y<=patternSize:
        s += "\n"
        y += 1
        x = 1
        while x<=patternSize:
            s += " * "
            x += 1
    output.set(value=s)

def displayHollowSquare(patternSize=1):
    y = 1
    s= ""
    while y<=patternSize:
        s += "\n"
        y += 1
        x = 1
        while x<=patternSize:
            if y<=2 or y>patternSize or x<=1 or x>=patternSize:
                s += " * "
                x += 1
            else:
                s += "    "
                x += 1
    output.set(value=s)


def displaySolidTriangle(patternSize=1):
    tempPatternSize = 1
    y = 1
    s = ""
    while y<=patternSize:
        s += "\n"
        y +=1
        x = 1
        while x<=tempPatternSize:
            s += " * "
            x += 1
        if tempPatternSize != patternSize:
            tempPatternSize += 1
    output.set(value=s)


def displayHollowTriangle(patternSize=1):
    y=1
    s=""
    tempPatternSize = 1
    while y<=patternSize:
        s += "\n"
        y +=1
        x = 1
        while x<=tempPatternSize:
            if y<=2 or y>patternSize:
                s += " * "
                x += 1
            else:
                if x<=1 or x>=tempPatternSize:
                    s+= " * "
                    x += 1
                else:
                    s += "    "
                    x += 1
        if tempPatternSize != patternSize:
            tempPatternSize += 1
    output.set(value=s)

def displaySolidDiamond(patternSize=1):
    y = 1
    s = ""
    if patternSize % 2 == 0:
        raise ValueError("Number is even")
    center = patternSize//2 + 1
    a = center
    b = center
    while y <= center:        
        x = 1
        while x <= patternSize: 
            if x >= a and x <= b:
                s += " * "
            else:
                s += "    "
            x += 1
        s += "\n"
        y += 1
        a -= 1
        b += 1
    y = center + 1   
    a = 2
    b = patternSize -1
    while y <= patternSize:   
        x = 1
        while x <= patternSize:  
            if x >= a and x <= b:
                s += " * "
            else:
                s += "    "
            x += 1
        s += "\n"
        y += 1
        a += 1
        b -= 1
    output.set(value=s)

def displayHollowDiamond(patternSize=1):
    y = 1
    s = ""
    while patternSize % 2 == 0:
        raise ValueError("Even Number")
    center = patternSize//2 + 1
    a = center
    b = center
    while y <= center:        
        x = 1
        while x <= patternSize: 
            if x == a or x == b:
                s += " * "
            else:
                s += "    "
            x += 1
        s += "\n"
        y += 1
        a -= 1
        b += 1
    y = center + 1   
    a = 2
    b = patternSize -1
    while y <= patternSize:   
        x = 1
        while x <= patternSize:  
            if x == a or x == b:
                s += " * "
            else:
                s += "    "
            x += 1
        s += "\n"
        y += 1
        a += 1
        b -= 1
    output.set(value=s)

def draw():
    output.set(value= "")
    patternSize = int(doublePatternSize.get())
    if fnt.get() == 0:
        displaySquare(patternSize, attr.get())
    if fnt.get() == 1:
        displayTriangle(patternSize, attr.get()) 
    if fnt.get() == 2:
        try:
            displayDiamond(patternSize, attr.get())
        except:
            var = messagebox.showerror("Error", "Even Number")

output=StringVar("")
m=StringVar()
m.set (value = "Star Patterns")

def deleteALL():
    output.set(value="")
    doublePatternSize.set(value=1)
    fnt.set(value="null")
    attr.set(value="null")

    
    
message = Label(root, textvariable = m,font = ("Times New Roman", 15, "normal"))
message.grid(row = 0, column = 0, columnspan = 2)
fontGroup = LabelFrame(root, text="Shape",padx=5, pady=5)
fontGroup.grid(row=1, column = 0)
attrGroup = LabelFrame(root, text="Fill",padx=5, pady=5)
attrGroup.grid(row=1, column = 1)
outputLabel = Label(root, textvariable = output, anchor=W, justify=LEFT)
outputLabel.grid(row=7, column = 0, columnspan=5)



Radiobutton (fontGroup,text = "Square", variable = fnt, value = 0) \
    .grid(row = 0, sticky = W)
Radiobutton (fontGroup, text = "Triangle", variable = fnt, value = 1) \
    .grid(row = 1, sticky = W)
Radiobutton (fontGroup, text = "Diamond", variable = fnt, value = 2) \
    .grid(row = 2, sticky = W)
Radiobutton (attrGroup, text = "Solid", variable = attr,value = True) \
    .grid(row = 0, sticky = W)
Radiobutton (attrGroup, text = "Hollow", variable = attr,value = False) \
    .grid(row = 1, sticky = W)

widget = Scale (root, from_ = 1, to = 20,resolution = 1,orient = HORIZONTAL, variable = doublePatternSize) \
    .grid(row = 3, column=0, columnspan = 2)


Draw = Button (root, text = "Draw", width=6, command = lambda:draw())
Draw.grid(row = 4, column = 0, sticky = W)
Clear = Button (root, text = "Clear", width=6, command = lambda: deleteALL()) \
          .grid(row = 4, column = 0, columnspan=2)
Exit = Button (root, text = "Exit", width=6, command = lambda: exit()) \
       .grid(row=4, column=1, sticky=E)



mainloop()
