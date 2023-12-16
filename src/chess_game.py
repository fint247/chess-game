
from tkinter import *
import tkinter as tk                                                       
from PIL import Image, ImageTk
import time
import threading

from chess_classes import *


r = tk.Tk() 
r.title('Chess') 
r.geometry('800x600-0+0')
r.config(bg = 'white')

# r.state('zoomed')

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


# a = [b_rook1, b_knigt1, b_bishop1, b_queen, b_king, b_bishop2, b_knigt2, b_rook2]
# b = [b_pawn1, b_pawn2, b_pawn3, b_pawn4, b_pawn5, b_pawn6, b_pawn7, b_pawn8]
# c = [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square]
# d = [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square]
# e = [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square]
# f = [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square]
# g = [w_pawn1, w_pawn2, w_pawn3, w_pawn4, w_pawn5, w_pawn6, w_pawn7, w_pawn8]
# h = [w_rook1, w_knigt1, w_bishop1, w_queen, w_king, w_bishop2, w_knigt2, w_rook2]

a = [b_rook1, b_knigt1, b_bishop1, b_queen, b_king, b_bishop2, b_knigt2, b_rook2]
b = [b_pawn1, b_pawn2, b_pawn3, b_pawn4, b_pawn5, b_pawn6, b_pawn7, b_pawn8]
c = [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square]
d = [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square]
e = [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square]
f = [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square]
g = [w_pawn1, w_pawn2, w_pawn3, w_pawn4, w_pawn5, w_pawn6, w_pawn7, w_pawn8]
h = [w_rook1, w_knigt1, w_bishop1, w_queen, w_king, w_bishop2, w_knigt2, w_rook2]

board = [a,b,c,d,e,f,g,h]

def exit_settings(r,s):
    # update_buttons(button_setting, button_stop)
    
    s.destroy()
    r.state('zoomed')
    r.state('normal')

def open_settings(r, from_rgb, exit_settings):
    settings.open_settings_window(r, from_rgb, exit_settings)

def update_buttons(settings, *args):
        print(f"HERE{settings.size}")
        for arg in args:
            arg.config(width=int(.25*1.3*int(settings.size)), height=int(.1*1.3*int(settings.size)),font=('Helvatical bold',int(.2*int(settings.size))), bg = 'teal', fg = 'black')
            arg.config(width=int(.25*1.3*int(settings.size)), height=int(.1*1.3*int(settings.size)),font=('Helvatical bold',int(.2*int(settings.size))), bg = 'teal', fg = 'black')
            
        for x in range(1,9):
            for y in range(1,9):
                exec(f"button_{x}_{y}.config(image = board[x-1][y-1].image)")

def check_if_promoting():
    if board[position_end[0]][position_end[1]].name == 'white_pawn' or board[position_end[0]][position_end[1]].name == 'black_pawn':
                if board[position_end[0]][position_end[1]].promoted == True:
                    if settings.auto_queen == True:
                        board[position_end[0]][position_end[1]] = Queen(board[position_end[0]][position_end[1]].color)
                    else:
                        #open promotion window Here
                        pass

def check_if_castling():
        if position_start[1] > position_end[1]:
            for i in range(0, position_end[1]):
                if board[position_start[0]][i].name == 'black_rook' and board[position_start[0]][position_start[1]].name == 'black_king' or board[position_start[0]][i].name == 'white_rook' and board[position_start[0]][position_start[1]].name == 'white_king':
                    print('here')
                    break

            board[position_end[0]][position_end[1]+1] = board[position_start[0]][i]
            board[position_start[0]][i] = empty_square

        elif position_start[1] < position_end[1]:
            for i in range(7, position_end[1], -1):
                if board[position_start[0]][i].name == 'black_rook' and board[position_start[0]][position_start[1]].name == 'black_king' or board[position_start[0]][i].name == 'white_rook' and board[position_start[0]][position_start[1]].name == 'white_king':
                    break
                
            board[position_end[0]][position_end[1]-1] = board[position_start[0]][i]
            board[position_start[0]][i] = empty_square

def update_ampasant():
    for x in range(8):
        # print('')
        for y in range(8):
        #     if board[x][y].ampasant == False:
        #         print(0,end = '')
        #     else:
        #         print(1,end='')
        
        
            if board[x][y].color == 'white' and whites_turn[0] == True:
                board[x][y].ampasant = False
                
            elif board[x][y].color == 'black' and whites_turn[0] == False:
                board[x][y].ampasant = False
                
    # print('\n')

def update_board():
    for x in range(1,9):
        for y in range(1,9):
            exec(f"button_{x}_{y}.config(image = board[x-1][y-1].image)")

def update_turn():
    if whites_turn[0] == True:
        whites_turn[0] = False
    elif whites_turn[0] == False:
        whites_turn[0] = True

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

        #print(board[position_start[0]][position_start[1]].name)

        valid_move[0] = board[position_start[0]][position_start[1]].is_legal(valid_move, whites_turn, board, position_start, position_end)
        if valid_move[0] == True:
            check_if_promoting()
            # check_if_castling()

        if valid_move[0] == True:
            board[position_end[0]][position_end[1]] = board[position_start[0]][position_start[1]]
            board[position_start[0]][position_start[1]] = empty_square
            
            board[position_end[0]][position_end[1]].has_moved = True
            

            update_board()
            update_ampasant()
            update_turn()

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

button_stop = Button(r, text='Stop', width=int(.25*1.3*settings.size), height=int(.1*1.3*settings.size),font=('Helvatical bold',int(.2*settings.size)), bg = 'teal', fg = 'black', command=r.destroy) 
button_stop.grid(row = 0, column = 0) 

button_setting = Button(r, text='Settings', width=int(.25*1.3*settings.size), height=int(.1*1.3*settings.size),font=('Helvatical bold',int(.2*settings.size)), bg = 'teal', fg = 'black', command= lambda: open_settings(r, from_rgb, exit_settings)) 
button_setting.grid(row = 0, column = 9) 

# filler_corner_1 = Label(r, bg = 'teal', border=2, relief='ridge') 
# filler_corner_1.grid(row = 9, column = 0, sticky='nse') 

# filler_corner_2 = tk.Button(r, bg = 'teal', border=2, relief='ridge') 
# filler_corner_2.grid(row = 9, column = 9, sticky='nsw') 

filler_1 = Label(r, bg = 'grey', borderwidth=2, relief='ridge')
filler_1.grid(row = 0, column = 1, columnspan = 8 ,sticky='nsew') 

# filler_2 = Label(r, bg = 'grey', borderwidth=2, relief='ridge')
# filler_2.grid(row = 1, column = 0, rowspan = 8 ,sticky='nsew') 

# filler_3 = Label(r, bg = 'grey', borderwidth=2, relief='ridge')
# filler_3.grid(row = 1, column = 9, rowspan = 8 ,sticky='nsew') 

# filler_4 = Label(r, bg = 'grey', borderwidth=2, relief='ridge')
# filler_4.grid(row = 9, column = 1, columnspan = 8 ,sticky='nsew') 

for x in range(1,9):
    for y in range(1,9):
        if x%2 == 0 and y%2 == 0 or x%2 != 0 and y%2 != 0:
            bg_color = from_rgb((238,238,210))
        else:
            bg_color = from_rgb((118,150,86))
        exec(f"button_{x}_{y} = tk.Button(r,image = board[x-1][y-1].image, bg = bg_color, width = settings.size, height = settings.size, border=0, command= lambda: pressed(button_{x}_{y},{x},{y},position_start,position_end, board))")
        exec(f"button_{x}_{y}.grid(row=x,column=y)")

highlight_img = Image.open(f"black_50.png")
highlight_img = ImageTk.PhotoImage(highlight_img.resize((settings.size,settings.size)))
highlight = Label(r,image = highlight_img, width = settings.size, height = settings.size, border=0)



r.mainloop() 

