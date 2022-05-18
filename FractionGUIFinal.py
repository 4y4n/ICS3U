#Name: Ayan Noorani
#Purpose: Create a GUI to your fraction calculation game
#Date: December 15 2021

import random
from tkinter import *
from tkinter import messagebox

#Purpose: to create a game for the user to test their ability to perform fraction calculations
#Data Elements:
#   intNumerator
#   intDenominator
#Methods:
#   __init__
#   calcGCD
#   verify
#   reduce
#   setValue
#   randomize
#   __str__
#   calcInverse
#   __eq__
#   __add__
#   __sub__
#   __mul__
#   __truediv__

class Fraction():

    #Purpose: initializes the fields to given values, uses 1/1 as default values and calls reduce
    #Parameters: intNumerator, intDenominator
    #Return/Output: N/A
    def __init__(self, intNumerator=1, intDenominator=1): #formally a constructor
        self.intNumerator = intNumerator
        self.intDenominator = intDenominator

    #Purpose: returns the GCD of 2 given integers
    #Parameters: x, y
    #Return/Output: GCD in the form of an integer
    def calcGCD(self, x, y):
        a = x % y
        while a != 0:
            x = y
            y = a
            a = x % y
        return y

    #Purpose: Checks to see whether the fraction is a valid fraction
    #Parameters: N/A
    #Return/Output: N/A
    def verify(self):
        if self.intDenominator == 0 or self.intNumerator == 0:
            self.intNumerator = 1
            self.intDenominator = 1

    #Purpose: reduce the current fraction to lowest terms with the negative sign (if there is one) on the top.
    #Parameters: N/A
    #Return/Output: N/A
    def reduce(self):
        self.verify()
        gcd = self.calcGCD(self.intNumerator, self.intDenominator)
        self.intNumerator = int(self.intNumerator/gcd)
        self.intDenominator = int(self.intDenominator/gcd)
        if self.intNumerator < 0 and self.intDenominator < 0:
            self.intNumerator = abs(self.intNumerator)
            self.intDenominator = abs(self.intDenominator)
        elif self.intDenominator < 0:
            self.intDenominator = abs(self.intDenominator)
            self.intNumerator = self.intNumerator - (2*self.intNumerator)

    #Purpose: sets the current fraction with a numerator and denominator obtained via parameters
    #Parameters: num, den
    #Return/Output: N/A
    def setValue(self, num, den):
        self.__init__(num, den)
        self.reduce()

    #Purpose: sets the current fraction with a numerator and denominator in the range -10 to 10
    #Parameters: minInt, maxInt
    #Return/Output: N/A
    def randomize(self, minInt=-10, maxInt=10):
        self.intNumerator = random.randint(minInt, maxInt)
        self.intDenominator = random.randint(minInt, maxInt)
        return self.reduce()

    #Purpose: Returns the fraction in proper mixed number form
    #Parameters: N/A
    #Return/Output: fraction in the form of a string
    def __str__(self):
        mix = ''
        self.verify()
        num = self.intNumerator
        den = self.intDenominator
        if abs(num) >= den and num != 0:
            mix = abs(num) // den
            if num < 0:
                mix = '-' + str(mix)
            num = abs(num) % den
            fraction = str(mix) + ' ' + str(num) + '/' + str(den)
        if num == 0:
            if mix == '':
                mix = 0
            fraction = str(mix)
        else:
            fraction = str(mix) + ' ' + str(num) + '/' + str(den)
        if num < 0 and den < 0 and mix < 0:
            num = abs(num)
            den = abs(den)
            fraction = str(mix) + ' ' + str(num) + '/' + str(den)
        return fraction

    #Purpose: calculates the inverse fraction of the current fraction.
    #Parameters: N/A
    #Return/Output: N/A
    def calcInverse(self):
        self.intNumerator, self.intDenominator = self.intDenominator, self.intNumerator

    #Purpose: Checks if a given fraction equals the current fraction
    #Parameters: x
    #Return/Output: Boolean True or False
    def __eq__(self, x):
        equal = False
        if self.intNumerator == x.intNumerator and self.intDenominator == x.intDenominator:
            equal = True
        return equal

    #Purpose: Adds the current fraction to the given fraction
    #Parameters: x
    #Return/Output: integers
    def __add__(self, x):
        num1 = self.intNumerator
        den1 = self.intDenominator
        num2 = x.intNumerator
        den2 = x.intDenominator
        self.intDenominator = den1 * den2
        self.intNumerator = (num1*den2) + (num2*den1)
        self.reduce()

    #Purpose: subtracts the current fraction by the given fraction
    #Parameters: x
    #Return/Output: integers
    def __sub__(self, x):
        num1 = self.intNumerator
        den1 = self.intDenominator
        num2 = x.intNumerator
        den2 = x.intDenominator
        self.intDenominator = den1 * den2
        self.intNumerator = (num1*den2) - abs((num2*den1))
        self.reduce()

    #Purpose: multiplies the current fraction by the given fraction
    #Parameters: x
    #Return/Output: integers
    def __mul__(self, x):
        num1 = self.intNumerator
        den1 = self.intDenominator
        num2 = x.intNumerator
        den2 = x.intDenominator
        self.intNumerator = num1 * num2
        self.intDenominator = den1 * den2
        self.reduce()

    #Purpose: divides the current fraction by the given fraction
    #Parameters: x
    #Return/Output: integer
    def __truediv__(self, x):
            self.calcInverse()
            self.__mul__(x)

root = Tk()
root.title('Fractions')
root.geometry('250x150')

firstFraction = StringVar()
scoring = StringVar()
global guess
global score
score = 0
global outOf
outOf = 0
Continue = 'y'
def generate():
    fraction1 = Fraction()
    fraction1.randomize()
    fraction2 = Fraction()
    fraction2.randomize()
    operation = random.randint(1, 4)
    if operation == 1:
        operation = '   +   '
    elif operation == 2:
        operation = '   -   '
    elif operation == 3:
        operation = '   *   '
    else:
        operation = '   /   '
        
    global guess
    guess = random.randint(1, 2)
    
    ok = fraction1.__str__()
    if operation == '   +   ':
        fraction1 + fraction2
        if guess == 2:
            fraction1.__str__()
            fraction1.calcInverse()
    elif operation == '   -   ':
        fraction1 - fraction2
        if guess == 2:
            fraction1.__str__()
            fraction1.calcInverse()
    elif operation == '   *   ':
        fraction1 * fraction2
        if guess == 2:
            fraction1.__str__()
            fraction1.calcInverse()
    else:
        fraction1 / fraction2
        if guess == 2:
            fraction1.__str__()
            fraction1.calcInverse()

    firstFraction.set(ok + operation + fraction2.__str__() + ' = ' + fraction1.__str__())
    
        
def right():
    global guess
    global score
    global outOf
    if guess == 1:
        score += 1
    outOf += 1
    scoring.set("Your score is " + str(score) + '/' + str(outOf))

def wrong():
    global guess
    global score
    global outOf
    if guess == 2:
        score += 1
    outOf += 1
    scoring.set("Your score is " + str(score) + '/' + str(outOf))


def reset():
    global score
    global outOf
    score = 0
    outOf = 0
    scoring.set('')
    firstFraction.set('')

generatebtn = Button(root, text='Create new calculation', command=generate, width=20).place(x=50, y=0)#grid(columnspan=2)
fraction1lbl = Label(root, textvariable=firstFraction, font=("Arial", "14", "bold")).place(x=50, y=30)#grid(column=0, row=1)
righttbn = Button(root, text='Right', command=right, width=10).place(x=35, y=60)#grid(column=1, row=2)
scorelbl = Label(root, textvariable=scoring, font = ("Arial", "12")).place(x=65, y=100)#grid(column=1, row=1)
wrongtbn = Button(root, text='Wrong', command=wrong, width=10).place(x=140, y=60)#grid(column=2, row=2)
resetbtn = Button(root, text='Reset Score', command=reset, width=10).place(x=90, y=120)

mainloop()
