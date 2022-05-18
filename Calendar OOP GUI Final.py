#Author: Ayan Noorani
#Date: Nov 9 2021
#Purpose: Create a date class which will allow entry and output of a date and print a calendar for the month and year.

from tkinter import *
import math
from tkinter import messagebox

#Purpose: A Date
#Data Elements:
#   Day: 1-31
#   Month: 1-12
#   Year: 1600-2200
#Method:
#   init
#   returnMonthName
#   returnLeapYear
#   returnMaxDay
#   calcZeller
#   returnDayName
#   getPositiveInteger
#   getDate
#   str
#=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class Date:
    
    def __init__(self): #formally a constructor
        self.intDay = 1
        self.intMonth = 1
        self.intYear = 2019

    #Purpose: to convert the month number into the name
    #Parameters: N/A
    #Return/Output: string conversion
    def returnMonthName(self, intmonth):
        if intmonth == 1:
            mname = "January"
        elif intmonth == 2:
            mname = "Feburary"
        elif intmonth == 3:
            mname = "March"
        elif self.intMonth == 4:
            mname = "April"
        elif intmonth == 5:
            mname = "May"
        elif intmonth == 6:
            mname = "June"
        elif intmonth == 7:
            mname = "July"
        elif intmonth == 8:
            mname = "August"
        elif intmonth == 9:
            mname = "September"
        elif intmonth == 10:
            mname =  "October"
        elif intmonth == 11:
            mname = "November"
        else:
            mname = "December"
        return mname

    #Purpose: to check if the year is a leap year or not
    #Parameters: N/A
    #Return/Output: Boolean True or False
    def returnLeapYear(self):
        if self.intYear % 100 != 0:
            nonCenturyYear = self.intYear
            if self.intYear % 400 == 0 or nonCenturyYear % 4 == 0:
                leapYear = True
                return leapYear
            else:
                leapYear = False
                return leapYear

    #Purpose: calculates the number of days in the month
    #Parameters: N/A
    #Return/Output: integer between 1 and 31
    def returnMaxDay(self, month):
        maxDay = 0
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            maxDay = 31
        elif month == 4 or month == 6 or month == 9 or month == 11:
            maxDay = 30
        else:
            if self.returnLeapYear() == True:
                maxDay = 29
            else:
                maxDay = 28
        return maxDay

    #Purpose: to calculate the zeller of the date
    #Parameters: N/A
    #Return/Output: integer between 0 and 6
    def calcZeller(self, day, month, year):
        m = month - 2
        y = year
        if m <= 0:
            m = m + 12
            y = y - 1
        p = y // 100
        r = y % 100
        return (day + (26 * m - 2) // 10 + r + r // 4 + p // 4 + 5 * p) % 7

    #Purpose: to convert the zeller number into the day name
    #Parameters: N/A
    #Return/Output: string conversion
    def returnDayName(self):
        switcher = {
            0: "Sunday",
            1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday",
        }
        return switcher.get(self.calcZeller(self.intDay, self.intMonth, self.intYear))

    #Purpose: check if the date inputted is valid
    #Parameters: N/A
    #Return/Output: Boolean True or False
    def calcValid(self):
        if self.intDay < 1 or self.intDay > self.returnMaxDay(self.intMonth):
            return False
            self.intDay = 1
            self.intMonth = 1
            self.intYear = 2019
        if self.intMonth < 1 or self.intMonth > 12:
            return False
            self.intDay = 1
            self.intMonth = 1
            self.intYear = 2019
        if self.intYear < 1600 or self.intYear > 2200:
            return False
            self.intDay = 1
            self.intMonth = 1
            self.intYear = 2019
        return True

    #Purpose: get a positive integer from the user
    #Parameters: low, high, prompt
    #Return/Output: a date in three outputs
    def getPositiveInteger (self, low, high, prompt):
        inputprompt = "Please enter the " + prompt + " in the range (" + str(low) + " - " + str(high) + "): "
        n = 0
        while n < 1 or n < low or n > high:
            n = int(input(inputprompt))
        return n

    #Purpose: calls getpositiveinteger and provides the range, then stores the numbers inputted into variables
    #Parameters: N/A
    #Return/Output: N/A
    def getDate(self):
        self.intDay = self.getPositiveInteger(1, 31, "day")
        self.intMonth = self.getPositiveInteger(1, 12, "month")
        self.intYear = self.getPositiveInteger(1600, 2200, "year")

    #Purpose: print the date in form “Thursday, March 30, 2020"
    #Parameters: N/A
    #Return/Output: the date
    def __str__(self):
        str1 = "\n" + self.returnDayName() + ", " + self.returnMonthName(self.intMonth) + " " + str(self.intDay) + ", " + str(self.intYear)
        return str1

    #Purpose: to display the calendar
    #Parameters: N/A
    #Return/Output: a calendar of the month with the month name and year on top
    def displayCalendar(self):
        disCal= ""
        zeller = self.calcZeller(1, self.intMonth, self.intYear)
        #print("\n      " + self.returnMonthName(), self.intYear)
        disCal = disCal + "\n           " + self.returnMonthName(self.intMonth) + '  ' + str(self.intYear) + '\n'
        space = ""
        space = space.rjust(4, " ")
        #print('Su', space, 'Mo', space, 'Tu', space, 'We', space, 'Th', space, 'Fr',space, 'Sa')
        disCal = disCal + 'Su' + space + 'Mo' + space + 'Tu' + space + 'We' + space + 'Th' + space + 'Fr' + space + 'Sa' + '\n'
        #print(self.calcZeller(1, self.intMonth, self.intYear))
        firstDay = 0
        space = space.rjust(5, " ")
        space1 = space.rjust(1, " ")
        space2 = space.rjust(9, " ")
        for i in range(7):
            if i<zeller:
                #print(space1, end="")
                disCal += space2
            else:
                firstDay += 1
                tmp = firstDay
                firstDay = "0" + str(firstDay)
                #print(firstDay, space, end="")
                disCal += firstDay + space1
                firstDay = tmp
        if self.returnLeapYear() == True and self.intMonth == 2:
            daysLeft = (self.returnMaxDay(self.intMonth)-firstDay)//7
        else:
            daysLeft = (self.returnMaxDay(self.intMonth)-firstDay)//7 +1
        for i in range(daysLeft):
            #print(" ")
            disCal += "\n"
            for j in range(7):
                firstDay += 1
                if firstDay<10:
                    tmp = firstDay
                    firstDay = "0" + str(firstDay)
                    #print(firstDay, space, end="")
                    disCal += firstDay + space
                    firstDay = tmp
                else:
                    #print(firstDay, space, end="")
                    disCal += str(firstDay) + space
                if firstDay == self.returnMaxDay(self.intMonth):
                    break
        return disCal

    def dayOfYear(self):
        monthCount = 1
        dayOfYear = 0
        while monthCount < self.intMonth:
            dayOfYear += self.returnMaxDay(monthCount)
            monthCount += 1
        dayOfYear += self.intDay
        imSoSickAndTiredOfMakingNewVariableNamesThereAreLikeAThousandVariablesInThisCodeImRunningOutOfIdeas = "\n \nThe day of the year is " + str(dayOfYear)
        return imSoSickAndTiredOfMakingNewVariableNamesThereAreLikeAThousandVariablesInThisCodeImRunningOutOfIdeas

                

#GUI===========================================================================================================================================================================

root = Tk()

date = Date()

century = StringVar()
decade = StringVar()
year = StringVar()
month = StringVar()
calendar = StringVar()
dayEnt = StringVar()
monthEnt = StringVar()
yearEnt = StringVar()
fullDate = StringVar()
dayOfYear = StringVar()

def getRoundedYears(yearVal, roundFactor):
    yearVal = yearVal/roundFactor
    yearVal = math.floor(yearVal)
    yearVal = yearVal * roundFactor
    return yearVal

def createDate():
    newDate= Date()
    newDate.intDay = int(dayEnt.get())
    newDate.intMonth = int(monthEnt.get())
    newDate.intYear = int(yearEnt.get())
    if newDate.calcValid() == False:
        var = messagebox.showerror("Error", "Invalid Input")
    else:
        date.intDay = int(dayEnt.get())
        date.intMonth = int(monthEnt.get())
        date.intYear = int(yearEnt.get())
        century.set(getRoundedYears(date.intYear, 100))
        decade.set(getRoundedYears(date.intYear, 10))
        year.set(date.intYear)
        month.set(date.returnMonthName(date.intMonth))
        calendar.set(date.displayCalendar())
        fullDate.set(date.__str__())
        dayOfYear.set(date.dayOfYear())

def centbtn(change):
    if change == 'up':
        date.intYear += 100
        decade.set(getRoundedYears(date.intYear, 10))
        year.set(date.intYear)
        if date.intYear > 2100:
            centupbtn['state'] = DISABLED
        if date.intYear >= 1700:
            centdwnbtn['state'] = NORMAL
        century.set(getRoundedYears(date.intYear, 100))
    else:
        date.intYear -= 100
        decade.set(getRoundedYears(date.intYear, 10))
        year.set(date.intYear)
        if date.intYear <= 2100:
            centupbtn['state'] = NORMAL
        if date.intYear < 1700:
            centdwnbtn['state'] = DISABLED
        century.set(getRoundedYears(date.intYear, 100))
    calendar.set(date.displayCalendar())
    yearEnt.set(date.intYear)
    dayOfYear.set(date.dayOfYear())
        
def decbtn(change):
    if change == 'up':
        date.intYear += 10
        if date.intYear > 2190:
            decupbtn['state'] = DISABLED
        if date.intYear >= 1610:
            decdwnbtn['state'] = NORMAL
        year.set(date.intYear)
        decade.set(getRoundedYears(date.intYear, 10))
    else:
        date.intYear -= 10
        if date.intYear < 2190:
            centupbtn['state'] = NORMAL
        if date.intYear < 1610:
            centdwnbtn['state'] = DISABLED
        year.set(date.intYear)
        decade.set(getRoundedYears(date.intYear, 10))
    calendar.set(date.displayCalendar())
    yearEnt.set(date.intYear)
    dayOfYear.set(date.dayOfYear())
        
def yearbtn(change):
    if change == 'up':
        date.intYear += 1
        if date.intYear == 2200:
            yearupbtn['state'] = DISABLED
        if date.intYear == 1601:
            yeardwnbtn['state'] = NORMAL
        year.set(date.intYear)
    else:
        date.intYear -= 1
        if date.intYear == 2199:
            yearupbtn['state'] = NORMAL
        if date.intYear == 1600:
            yeardwnbtn['state'] = DISABLED
        year.set(date.intYear)
    calendar.set(date.displayCalendar())
    yearEnt.set(date.intYear)
    dayOfYear.set(date.dayOfYear())
        
def monthbtn(change):
    if change == 'up':
        date.intMonth+=1
        if date.intMonth == 13:
            date.intMonth=1
        month.set(date.returnMonthName(date.intMonth))
    else:
        date.intMonth-=1
        if date.intMonth == 0:
            date.intMonth=12
        month.set(date.returnMonthName(date.intMonth))
    calendar.set(date.displayCalendar())
    monthEnt.set(date.intMonth)
    dayOfYear.set(date.dayOfYear())
    
#main======================================================================================================================
daylbl = Label(root, text="Please enter the day")
monthlbl = Label(root, text="Please enter the month")
yearlbl = Label(root, text="Please enter the year")
dayEntr = Entry(root,textvariable=dayEnt)
monthEntr = Entry(root,textvariable=monthEnt)
yearEntr = Entry(root,textvariable=yearEnt)


centdwnbtn = Button(root, text = '<', command=lambda:centbtn('down'))
centupbtn = Button(root, text= '>', command=lambda:centbtn('up'))
decdwnbtn = Button(root, text= '<', command=lambda:decbtn('down'))
decupbtn = Button(root, text= '>', command=lambda:decbtn('up'))
yeardwnbtn = Button(root, text= '<', command=lambda:yearbtn('down'))
yearupbtn = Button(root, text='>', command=lambda:yearbtn('up'))
monthdwnbtn = Button(root, text= '<', command=lambda:monthbtn('down'))
monthupbtn = Button(root, text='>', command=lambda:monthbtn('up'))

createbtn = Button(root, text = 'Display Date', command = lambda:createDate())

centurylbl = Label(root, textvariable = century)
decadelbl = Label(root, textvariable = decade)
yearlbl1 = Label(root, textvariable = year)
monthlbl1 = Label(root, textvariable = month)
fullDatelbl = Label(root, textvariable = fullDate)
calendarlbl = Label(root, textvariable = calendar, justify=LEFT)
dayOfYearlbl = Label(root, textvariable = dayOfYear)



daylbl.grid(row=1, sticky=W)
dayEntr.grid(column=1, row=1)
monthlbl.grid(row=2, sticky=W)
monthEntr.grid(column=1, row=2)
yearlbl.grid(row=3, sticky=W)
yearEntr.grid(column=1, row=3)

createbtn.grid(row=4, columnspan=2)
centurylbl.grid(row=5, columnspan=2)
decadelbl.grid(row=6, columnspan=2)
fullDatelbl.grid(row=10, columnspan=2)
calendarlbl.grid(row=11, columnspan=2)
dayOfYearlbl.grid(row=12, columnspan=2)
centdwnbtn.grid(row=5)
centupbtn.grid(column=1, row=5)
decdwnbtn.grid(row=6)
decupbtn.grid(column=1, row=6)
yeardwnbtn.grid(row=8)
yearupbtn.grid(column=1, row=8)
monthdwnbtn.grid(row=9)
monthupbtn.grid(column=1, row=9)
yearlbl1.grid(row=8, columnspan=2)
monthlbl1.grid(row=9, columnspan=2)

century.set(getRoundedYears(date.intYear, 100))
decade.set(getRoundedYears(date.intYear, 10))
year.set(date.intYear)
month.set(date.returnMonthName(date.intMonth))
fullDate.set(date.__str__())
calendar.set(date.displayCalendar())
dayOfYear.set(date.dayOfYear())



mainloop()
