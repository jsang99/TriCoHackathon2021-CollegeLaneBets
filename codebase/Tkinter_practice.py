from tkinter import *
#create window
root = Tk()

#create text labels
theLabel = Label(root,text = "collegelanebets ftw")
theLabel.pack()

#frames to put stuffs in
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

#buttons
button1 = Button(topFrame, text="Button1", fg="red")
button2 = Button(topFrame, text="Button2", fg="blue")
button3 = Button(bottomFrame, text="Button3", fg="green")

button1.pack(side=LEFT)
button2.pack(side=RIGHT)
button3.pack()

#label background and foreground, and filling sides
one = Label(root, text="One",bg = "red",fg="white")
one.pack()
two = Label(root, text="Two",bg = "black",fg="green")
two.pack(fill=X)
three = Label(root, text="Three",bg = "yellow",fg="green")
three.pack(side=LEFT,fill=Y)

#function binding to button
def printSmth():
    print("smth lmao")

button4 = Button(root,text="print something", command=printSmth)
button4.pack(side=BOTTOM)

#keep window running
root.mainloop()