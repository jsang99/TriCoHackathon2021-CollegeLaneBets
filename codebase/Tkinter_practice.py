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

#keep window running
root.mainloop()