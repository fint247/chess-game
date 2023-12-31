from tkinter import *
from PIL import Image, ImageTk


from PIL import Image, ImageDraw

# Open the image
image_path = "white_knight.png"  # Replace with the actual path to your image
original_image = Image.open(image_path)

# Create a new image with RGBA mode
new_image = Image.new("RGBA", original_image.size, (0, 0, 0, 0))

# Paste the original image onto the new image
new_image.paste(original_image, (0, 0))

# Create a drawing object for the new image
draw = ImageDraw.Draw(new_image)

# Define the circle parameters
center = (25, 25)  # Replace with the desired center coordinates
radius = 10  # Replace with the desired radius
color = (0, 0, 255, 50)  # RGB color with alpha (transparency) value

# Draw the circle on the new image
draw.ellipse([(center[0] - radius, center[1] - radius), (center[0] + radius, center[1] + radius)], fill=color, outline=None)

# Save or display the modified image
new_image.show()





# import copy

# class MyClass():
#     pass
# # Create an instance
# my_instance = MyClass()

# # Check the class using type()
# instance_class = type(my_instance)
# print(instance_class)

# is_instance = isinstance(my_instance, MyClass)
# print(is_instance)


# img1 = Image.open(f"black_knight.png")
# img2 = Image.open(f"black_circle_75.png")

# img3 = img1.resize((100,100))
# img4 = img2.resize((100,100))

# result = Image.blend(img3, img4, alpha=0.5)

# result.show()


# root = Tk()
# root.geometry('400x400')

# class ImageClass():
#     def __init__(self):
#         self.image= (Image.open(f"black_knight.png"))
#         self.scaled_image= ImageTk.PhotoImage(self.image.resize((100,100)))


#     def rescale_img(self):
#         self.scaled_image= ImageTk.PhotoImage(self.image.resize((int(self.scaled_image.width())+10,int(self.scaled_image.height())+10)))
#         return self.scaled_image
    

# img = ImageClass()

# def resize(img):
#     button_1_3.config(image=img.rescale_img(), width=int(button_1_3['width'])+10, height=int(button_1_3['height'])+10)

# def change_bg(button_1_3):
#     for x in range(1,2):
#         for y in range(3,4):
            
#                 if button_1_3['bg'] == 'green':
#                     button_1_3.config(bg = 'blue')
#                 else:
#                     button_1_3.config(bg = 'green')

# button_1_3 = Button(root, height=100, width=100, bg='green', image=img.scaled_image, command=lambda: resize(img))
# button_1_3.grid(row=0, column=2)
# button_1_3.x_y = (1,3)
# print(button_1_3.x_y)


# button2 = Button(root, height=10, width=20, bg='grey',text='change\nbg color', command=lambda: change_bg(button_1_3))
# button2.grid(row=0, column=1)

# root.mainloop()