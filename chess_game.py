
from tkinter import *
import tkinter as tk                                                       
from PIL import Image, ImageTk

from chess_classes import *


r = tk.Tk() 
r.title('Chess') 
r.geometry('600x600')
size = 50 

valid_move = [True]
position_start = []
position_end = []
whites_turn= [True]





#maybe add a name variable to the instences that specifies what pawn/rook/bishop/knight it is rather than making 24 unique instances 

empty_square = EmptySquare()

b_rook1 = Rook('black')
b_knigt1 = Knight('black')
b_bishop1 = Bishop('black')
b_queen = Queen('black')
b_king = King('black')
b_bishop2 = Bishop('black')
b_knigt2 = Knight('black')
b_rook2 = Rook('black')
b_pawn1 = Pawn('black')
b_pawn2 = Pawn('black')
b_pawn3 = Pawn('black')
b_pawn4 = Pawn('black')
b_pawn5 = Pawn('black')
b_pawn6 = Pawn('black')
b_pawn7 = Pawn('black')
b_pawn8 = Pawn('black')
w_rook1 = Rook('white')

w_knigt1 = Knight('white')
w_bishop1 = Bishop('white')
w_queen = Queen('white')
w_king = King('white')
w_bishop2 = Bishop('white')
w_knigt2 = Knight('white')
w_rook2 = Rook('white')
w_pawn1 = Pawn('white')
w_pawn2 = Pawn('white')
w_pawn3 = Pawn('white')
w_pawn4 = Pawn('white')
w_pawn5 = Pawn('white')
w_pawn6 = Pawn('white')
w_pawn7 = Pawn('white')
w_pawn8 = Pawn('white')


a = [b_rook1, b_knigt1, b_bishop1, b_queen, b_king, b_bishop2, b_knigt2, b_rook2]
b = [b_pawn1, b_pawn2, b_pawn3, b_pawn4, b_pawn5, b_pawn6, b_pawn7, b_pawn8]
c = [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square]
d = [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square]
e = [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square]
f = [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square]
g = [w_pawn1, w_pawn2, w_pawn3, w_pawn4, w_pawn5, w_pawn6, w_pawn7, w_pawn8]
h = [w_rook1, w_knigt1, w_bishop1, w_queen, w_king, w_bishop2, w_knigt2, w_rook2]

board = [a,b,c,d,e,f,g,h]



def update_buttons():
    for x in range(1,9):
        for y in range(1,9):
            exec(f"button_{x}_{y}.config(image = board[x-1][y-1].image)")

def from_rgb(rgb):
    """
    translates an rgb tuple of int to a tkinter friendly color code
    """
    r, g, b = rgb
    return f'#{r:02x}{g:02x}{b:02x}'

def pressed(button,a,b,position_start,position_end, board):
    for x in range(1,9):
        for y in range(1,9):
            if x%2 == 0 and y%2 == 0 or x%2 != 0 and y%2 != 0:
                exec(f"button_{x}_{y}.config(bg = from_rgb((238,238,210)))")
            else:
                exec(f"button_{x}_{y}.config(bg = from_rgb((118,150,86)))")

    if len(position_start) == 0:
        # print('position_start before = ', position_start)
        position_start.append(a-1)
        position_start.append(b-1)
        # print('position start after = ',position_start)
        
    elif len(position_start) == 2:
        position_end.append(a-1)
        position_end.append(b-1)

        print(board[position_start[0]][position_start[1]].name)

        valid_move[0], whites_turn[0] = board[position_start[0]][position_start[1]].is_legal(valid_move, whites_turn)
        if valid_move[0] == True:
            print(f"position start: {position_start} --> position end: {position_end}\n")
            board[position_end[0]][position_end[1]] = board[position_start[0]][position_start[1]]
            board[position_start[0]][position_start[1]] = empty_square
            update_buttons()
        else:
            #resets valid move to be true but doesnt move the piece
            valid_move[0] = True
            
            
        for i in range(len(position_start)):
            position_start.pop(0)
        for j in range(len(position_end)):
            position_end.pop(0)
    
    else:
        raise Exception(f"position start({position_start}) is not a valid legth")
        

    button.config(bg = from_rgb((238-50,238-50,210-50)))
    # print(f"row = {a}, col = {b}")
    # highlight.grid(row=a, column=b)

button = tk.Button(r, text='Stop', width=7, height=3,font=('Helvatical bold',20), bg = 'teal', fg = 'black', command=r.destroy) 
button.grid(row = 0, column = 0) 



for x in range(1,9):
    for y in range(1,9):
        if x%2 == 0 and y%2 == 0 or x%2 != 0 and y%2 != 0:
            bg_color = from_rgb((238,238,210))
        else:
            bg_color = from_rgb((118,150,86))
        exec(f"button_{x}_{y} = tk.Button(r,image = board[x-1][y-1].image, bg = bg_color, width = size, height = size, border=0, command= lambda: pressed(button_{x}_{y},{x},{y},position_start,position_end, board))")
        exec(f"button_{x}_{y}.grid(row=x,column=y)")

highlight_img = Image.open(f"black_50.png")
highlight_img = ImageTk.PhotoImage(highlight_img.resize((size,size)))
highlight = Label(r,image = highlight_img, width = size, height = size, border=0)



r.mainloop() 
