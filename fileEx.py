# Drop-dows - change to feed
customers = [
    'customer 1',
    'customer 2',
    'customer 3..',]   

users = [
    'User 1',
    'User 2']               


from tkinter import *
import datetime
import time


# Window
root = Tk()                    
root.title("Time Tracker")
root.geometry("376x101")
root.configure(background="gray40")
root.resizable(False,False)
root.attributes('-topmost', True)   #always on top
root.update()                       # refresh for always on top

labelFont = ('calibri', 10, 'bold')

# Drop downs
u = StringVar(root)
u.set(users[0])

u1 = OptionMenu(root, u, *users)
u1.config(bg="GRAY34", fg="grey90", highlightthickness=0, activebackground="grey44", activeforeground="white")
u1.grid(row=0, column=1, columnspan=2, sticky=N+S+E+W)

dDC = StringVar(root)
dDC.set(customers[0])

dDC1 = OptionMenu(root, dDC, *customers)
dDC1.config(bg="GRAY34", fg="grey90", highlightthickness=0, activebackground="grey44", activeforeground="white")
dDC1.grid(row=1, column=1, columnspan=2, sticky=N+S+E+W)


# Globals
timeStamp = datetime.datetime.now()
startTime = 0
stopTime = 0


# Functions                 to be expanded upon
def startTimer(event):
    global startTime
    startTime = time.time()

def stopTimer(event):
    global stopTime
    stopTime = time.time()

def resetTimer(event):
    global startTime
    global stopTime
    startTime = 0
    stopTime = 0

def submitTimer(event):
    pass    # yet to be done


# Buttons
startButton = Button(root, text="Start", bg="black", fg="white", activebackground="grey25", activeforeground="grey90", width=12, borderwidth=2, relief="ridge")
startButton.bind("<Button-1>", startTimer)
startButton.grid(row=3, column=0, sticky=N+S+E+W)

stopButton = Button(root, text="Stop", bg="black", fg="white", activebackground="grey25", activeforeground="grey90", width=12, borderwidth=2, relief="ridge")
stopButton.bind("<Button-1>", stopTimer)
stopButton.grid(row=3, column=1, sticky=N+S+E+W)

resetButton = Button(root, text="Reset", bg="firebrick4", activebackground="firebrick3", activeforeground="grey90", fg="grey90", width=12, borderwidth=2, relief="ridge")
resetButton.bind("<Button-1>", resetTimer)
resetButton.grid(row=3, column=2, sticky=N+S+E+W)

submitButton = Button(root, text="Submit", bg="springgreen4", fg="white", activebackground="springgreen3", activeforeground="grey90", width=12, borderwidth=2, relief="ridge")
submitButton.bind("<Button-1>", resetTimer)
submitButton.grid(row=3, column=3, sticky=N+S+E+W)

noteInput = Entry(root, bg="grey90", borderwidth=2, relief="ridge")
noteInput.grid(row=2, column=1, columnspan=3, sticky=N+S+E+W)


# Labels
labelUser = Label(root, text="User:", bg="grey40", fg="grey90", font=labelFont)
labelUser.grid(row=0, column=0, sticky=E)

labelCustomers = Label(root, text="Customer:", bg="grey40", fg="grey90", font=labelFont)
labelCustomers.grid(row=1, column=0, sticky=E)

notes = Label(root, text="Notes:", bg="grey40", fg="grey90", font=labelFont)
notes.grid(row=2, column=0, sticky=E)

startLabel = Label(root, text=startTime, bg="grey40", fg="grey90")
startLabel.grid(column=3, row=0, sticky=N+S+E+W)

stopLabel = Label(root, text=stopTime, bg="grey40", fg="grey90")
stopLabel.grid(column=3, row=1, sticky=N+S+E+W)


# stops window from closing
root.mainloop()                 