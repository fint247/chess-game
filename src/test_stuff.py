from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry('400x400')

class ImageClass():
    def __init__(self):
        self.image= (Image.open(f"black_knight.png"))
        self.scaled_image= ImageTk.PhotoImage(self.image.resize((100,100)))


    def rescale_img(self):
        self.scaled_image= ImageTk.PhotoImage(self.image.resize((int(self.scaled_image.width())+10,int(self.scaled_image.height())+10)))
        return self.scaled_image
    

img = ImageClass()

def resize(img):
    button.config(image=img.rescale_img(), width=int(button['width'])+10, height=int(button['height'])+10)

def change_bg(button):
    if button['bg'] == 'green':
        button.config(bg = 'blue')
    else:
        button.config(bg = 'green')

button = Button(root, height=100, width=100, bg='green', image=img.scaled_image, command=lambda: resize(img))
button.grid(row=0, column=2)


button2 = Button(root, height=10, width=20, bg='grey',text='change\nbg color', command=lambda: change_bg(button))
button2.grid(row=0, column=1)

root.mainloop()