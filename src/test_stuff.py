from tkinter import * #For python 3 use: from Tkinter import *

root = Tk()
root.title("Fee Fie Foe Fum")
frame=Frame(root, width=300, height=200)
frame.pack()
button1 = Button(frame, text="Mercy!")
button1.place(x=10, y=10, height=30, width=100)
button2 = Button(frame, text="Justice!")
button2.place(x=10, y=50, height=30, width=100)
text1 = Label(text="Verdict:")
text1.place(x=10, y=90)
tbox1 = Text(frame)
tbox1.place(x=10, y=115, height=30, width=200)

root.mainloop()