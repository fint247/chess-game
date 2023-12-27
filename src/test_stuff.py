# Import all files from
# tkinter and overwrite
# all the tkinter files
# by tkinter.ttk
from tkinter import *
import tkinter as tk   
# from PIL import Image,ImageDraw as D


# creates tkinter window or root window
root = Tk()
root.geometry('400x200')

img = PhotoImage(file='black_king.png')
# img = img.zoom(2,2)
img = img.subsample(4,4)
thing = Button(root,height= 200, width=200, image = img, command=root.destroy)
thing.grid(row=0, column=2)

button_stop = Button(root, text='Exit',width=20,padx=0, pady=10, border=0, font=('Helvatical bold',int(10)), bg = 'green', fg = 'black', command=root.destroy) 
button_stop.grid(row=0, column=1) 

mainloop()
