#change this to be a text file so it remembers you settings
#add users so the settings can be save to users
#maybe add passwords and look into encryption
#add verification when person enters email,phone number, or disord


from tkinter import *
import tkinter as tk                                                       
from PIL import Image, ImageTk


size = 50

#state = 'normal', 'iconic', 'withdrawn', or 'zoomed'

def exit_settings(r,s):
    s.destroy()
    r.state('zoomed')
    r.state('normal')

def open_settings(r):
    r.state('withdrawn')
    
    s = tk.Tk() 
    s.title('Settings') 
    s.geometry('700x600-0+0')
    #s.tk.call('tk','scaling', 3.0)

    exit_button = Button(s, text='Exit',pady = 10, width=7, height=3,font=('Helvatical bold',20), bg = 'teal', fg = 'black', command= lambda: exit_settings(r,s)) 
    exit_button.pack() 

    size_lbl = Label(s, text = 'Size', width=7, height=3,font=('Helvatical bold',20), bg = 'teal', fg = 'black', pady = 10)
    size_lbl.pack(fill=X,)

    size_1 = Button(s, text = 'Size 1', width=7, height=3,font=('Helvatical bold',20), bg = 'teal', fg = 'black', pady = 10)
    size_1.place(relwidth=0.5, relheight=0.5, relx=0.5, rely=0.5, anchor=CENTER)
    # size_1.pack(fill = X, padx = 50)

    size_2 = Button(s, text = 'Size 2', width=7, height=3,font=('Helvatical bold',20), bg = 'teal', fg = 'black', pady = 10)
    # size_2.place(relwidth=0.5, relheight=0.5, relx=0.5, rely=0.5, anchor=CENTER)
    size_2.pack(fill = X)

    size_3 = Button(s, text = 'Size 3', width=7, height=3,font=('Helvatical bold',20), bg = 'teal', fg = 'black', pady = 10)
    # size_3.place(relwidth=0.5, relheight=0.5, relx=0.5, rely=0.5, anchor=CENTER)
    size_3.pack(fill = X)

    border_lbl = Label(s, text = 'border Thickness', width=7, height=3,font=('Helvatical bold',20), bg = 'teal', fg = 'black', pady = 30, padx = 10)
    border_lbl.pack(side = BOTTOM, fill=X,)



