import tkinter as tk

root = tk.Tk()
root.geometry('500x200')
root.config(bg = 'blue')
pixel = tk.PhotoImage(width=1, height=1)
button = tk.Button(root, text="hello",bg = 'yellow', image=pixel,border =0, padx = 0, pady = 0, width=200, height=100, compound="c")
button2 = tk.Button(root, text="hello", bg = 'red', image=pixel,border=0,padx = 0, pady = 0, width=200, height=100, compound="c")
button.grid(column=0)
button2.grid(column=1)

button.grid(column=0, sticky="nsew")
button2.grid(column=1, sticky="nsew")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

root.mainloop()
# import tkinter as tk


# class Tracker:
#     """ Toplevel windows resize event tracker. """

#     def __init__(self, root):
#         self.root = root
#         self.width, self.height = root.winfo_width(), root.winfo_height()
#         self._func_id = None

#     def bind_config(self):
#         self._func_id = self.root.bind("<Configure>", self.resize)

#     def unbind_config(self):  # Untested.
#         if self._func_id: 
#             self.root.unbind("<Configure>", self._func_id)
#             self._func_id = None

#     def resize(self, event):
#         if(event.widget == self.root and
#            (self.width != event.width or self.height != event.height)):
#             print(f'{event.widget=}: {event.height=}, {event.width=}\n')
#             self.width, self.height = event.width, event.height


# root = tk.Tk()

# tracker = Tracker(root)
# tracker.bind_config()

# root.mainloop()









# # Import module 
# from tkinter import *
 
# # Create object 
# root = Tk()
 
# # Adjust size 
# root.geometry("500x500")
 
# # # Specify Grid
# # Grid.rowconfigure(root,0,weight=1)
# # Grid.columnconfigure(root,0,weight=1)
 
# # Grid.rowconfigure(root,1,weight=1)

# # Create Buttons
# button_1 = Button(root,text="Button 1",bg = 'teal')
# button_2 = Button(root,text="Button 2",bg = 'teal')
 
# button_1.grid(row=0,column=0,sticky="NSEW")
# button_2.grid(row=0,column=2,sticky="NSEW")

# Grid.rowconfigure(root,0,weight=1)
# Grid.columnconfigure(root,0,weight=1)

# Grid.columnconfigure(root,1,weight=1)
# Grid.columnconfigure(root,2,weight=1)

# main_frame = Frame(root,bg = 'teal',bd = 10)
# main_frame.grid(row=1,column=1)

# for x in range(8):
#     Grid.rowconfigure(main_frame,x,weight=1)
#     Grid.columnconfigure(main_frame,x,weight=1)
#     for y in range(8):
#         button = Button(main_frame, text=f'{x+y}')
#         button.grid(row=x,column=y,sticky="NSEW")
        

 
# # Execute tkinter
# root.mainloop()











# class Pawn():
#     def __init__(self,name,color):
#         self.name = name
#         self.color = color


# pawn1 = Pawn('pawn1','black')
# pawn2 = pawn1.copy()

# pawn2.name = pawn2

# print(pawn1.name)
# print(pawn2.name)
  

    





# from chess_classes import *

# r = tk.Tk() 
# r.title('Chess') 
# r.geometry('800x600-0+0')
# r.config(bg = 'white')

# # r.state('zoomed')

# valid_move = [True]
# position_start = []
# position_end = []
# whites_turn= [True]



# #maybe add a name variable to the instences that specifies what pawn/rook/bishop/knight it is rather than making 24 unique instances 

# empty_square = EmptySquare()

# b_rook1 = Rook('black')
# b_knigt1 = Knight('black')
# b_bishop1 = Bishop('black')
# b_queen = Queen('black')
# b_king = King('black')
# b_bishop2 = Bishop('black')
# b_knigt2 = Knight('black')
# b_rook2 = Rook('black')
# b_pawn1 = Pawn('black')
# b_pawn2 = Pawn('black')
# b_pawn3 = Pawn('black')
# b_pawn4 = Pawn('black')
# b_pawn5 = Pawn('black')
# b_pawn6 = Pawn('black')
# b_pawn7 = Pawn('black')
# b_pawn8 = Pawn('black')
# w_rook1 = Rook('white')

# w_knigt1 = Knight('white')
# w_bishop1 = Bishop('white')
# w_queen = Queen('white')
# w_king = King('white')
# w_bishop2 = Bishop('white')
# w_knigt2 = Knight('white')
# w_rook2 = Rook('white')
# w_pawn1 = Pawn('white')
# w_pawn2 = Pawn('white')
# w_pawn3 = Pawn('white')
# w_pawn4 = Pawn('white')
# w_pawn5 = Pawn('white')
# w_pawn6 = Pawn('white')
# w_pawn7 = Pawn('white')
# w_pawn8 = Pawn('white')


# a = [b_rook1, b_knigt1, b_bishop1, b_queen, b_king, b_bishop2, b_knigt2, b_rook2]
# b = [b_pawn1, b_pawn2, b_pawn3, b_pawn4, b_pawn5, b_pawn6, b_pawn7, b_pawn8]
# c = [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square]
# d = [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square]
# e = [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square]
# f = [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square]
# g = [w_pawn1, w_pawn2, w_pawn3, w_pawn4, w_pawn5, w_pawn6, w_pawn7, w_pawn8]
# h = [w_rook1, w_knigt1, w_bishop1, w_queen, w_king, w_bishop2, w_knigt2, w_rook2]

# # a = [b_rook1, b_king, empty_square, empty_square, empty_square, empty_square, empty_square, b_rook2]
# # b = [b_pawn1, b_pawn2, b_pawn3, b_pawn4, b_pawn5, b_pawn6, b_pawn7, b_pawn8]
# # c = [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square]
# # d = [empty_square, empty_square, empty_square, w_king, empty_square, empty_square, empty_square, empty_square]
# # e = [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square]
# # f = [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square]
# # g = [w_pawn1, w_pawn2, w_pawn3, w_pawn4, w_pawn5, w_pawn6, w_pawn7, w_pawn8]
# # h = [w_rook1, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, w_rook2]

# board = [a,b,c,d,e,f,g,h]

# temp_board = [ row.copy() for row in board]
# temp_empty_square = EmptySquare()

# for a in range(8):
#    for b in range(8):
#       print(temp_board[a][b].name,end=' - ')
#    print('')

# print('\n')

# for a in range(8):
#    for b in range(8):
#       print(board[a][b].name,end=' - ')
#    print('')

# temp_board[1][1] = temp_board[0][1]
# temp_board[0][1] = temp_empty_square

# print('\n')

# for a in range(8):
#    for b in range(8):
#       print(temp_board[a][b].name,end=' - ')
#    print('')

# print('\n')

# for a in range(8):
#    for b in range(8):
#       print(board[a][b].name,end=' - ')
#    print('')