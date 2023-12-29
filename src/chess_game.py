"""
ideas to add:
flip board (home page)
play computer(home page)
play online (home page)
play local (home page)

auto flip (settings - local games)

"""

#activebackground='blue'


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

# r.overrideredirect(True)
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


a = [empty_square, empty_square, empty_square, b_queen, b_king, b_bishop2, b_knigt2, b_rook2]
b = [empty_square, empty_square, empty_square, b_pawn4, b_pawn5, b_pawn6, b_pawn7, b_pawn8]
c = [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square]
d = [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square]
e = [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square]
f = [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square]
g = [empty_square, empty_square, empty_square, w_pawn4, w_pawn5, w_pawn6, w_pawn7, w_pawn8]
h = [empty_square, empty_square, empty_square, w_queen, w_king, w_bishop2, w_knigt2, w_rook2]

# a = [b_rook1, b_knigt1, b_bishop1, b_queen, b_king, b_bishop2, b_knigt2, b_rook2]
# b = [b_pawn1, b_pawn2, b_pawn3, b_pawn4, b_pawn5, b_pawn6, b_pawn7, b_pawn8]
# c = [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square]
# d = [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square]
# e = [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square]
# f = [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square]
# g = [w_pawn1, w_pawn2, w_pawn3, w_pawn4, w_pawn5, w_pawn6, w_pawn7, w_pawn8]
# h = [w_rook1, w_knigt1, w_bishop1, w_queen, w_king, w_bishop2, w_knigt2, w_rook2]

board = [a,b,c,d,e,f,g,h]


class WindowTracker():
    """ windows resize event tracker """

    def __init__(self, root):
        self.root = root
        self.width, self.height = root.winfo_width(), root.winfo_height()
        self._func_id = None

    def bind_config(self, board):
        self._func_id = self.root.bind("<Configure>", lambda event: self.resize(event, board))

    def unbind_config(self):  # Untested.
        if self._func_id: 
            self.root.unbind("<Configure>", self._func_id)
            self._func_id = None

    def resize(self, event, board):
        if(event.widget == self.root and
           (self.width != event.width or self.height != event.height)):
            # print(f'{event.height}, {event.width}')
            self.width, self.height = event.width, event.height

            # scale = min(self.width, self.height)
            if self.width*(8/12) >= self.height*(8/12):
                chess_board_width = self.height * (10/12)
                side_bar_width = (self.width-chess_board_width)/2
                settings.size = int(chess_board_width*(1/10))


            elif self.width*(8/12) < self.height*(8/12):
                chess_board_width = self.width * (10/12)
                side_bar_width = (self.width-chess_board_width)/2
                settings.size = int(chess_board_width*(1/10))

            else:
                print('something else')

            rescale_game(board,int(side_bar_width), int(chess_board_width))

      

def rescale_game(board,side_bar_width,chess_board_width):
    left_frame.place(x=0, y=0, width=side_bar_width, height=tracker.height)
    right_frame.place(x=side_bar_width+chess_board_width, y=0, width=side_bar_width+3, height=tracker.height)
    center_frame.place(x=side_bar_width, y=0, width=chess_board_width, height=tracker.height)

    button_stop.config(width=side_bar_width)
    button_setting.config(width=side_bar_width)
    
    resized_empty_square = 0
    for x in range(8):
        for y in range(8):
            if board[x][y].name == 'empty_square':
                resized_empty_square += 1
            if board[x][y].name != 'empty_square' or resized_empty_square == 1:
                exec(f"button_{x}_{y}.config(width=int(chess_board_width*(1/8))-1, height=int(chess_board_width*(1/8)), image=board[x][y].rescale_img())")
            else:
                exec(f"button_{x}_{y}.config(width=int(chess_board_width*(1/8))-1, height=int(chess_board_width*(1/8)), image=board[x][y].new_scaled_image)")

    # print(f"{tracker.width=}")

def enter(event, button): # function to be called when mouse enters in a frame
    button.config(bg=from_rgb((0, 100, 100)))
	# print('Button-2 pressed at x = % d, y = % d'%(event.x, event.y))

def exit_(event, button): # function to be called when mouse exits the frame
    button.config(bg=from_rgb((0, 128, 128)))
	# print('Button-3 pressed at x = % d, y = % d'%(event.x, event.y))  

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
            
        for x in range(8):
            for y in range(8):
                exec(f"button_{x}_{y}.config(image = board[x-1][y-1].new_scaled_image)")
                
def check_if_promoting():
    if board[position_end[0]][position_end[1]].name == 'white_pawn' or board[position_end[0]][position_end[1]].name == 'black_pawn':
                if board[position_end[0]][position_end[1]].promoted == True:
                    if settings.auto_queen == True:
                        board[position_end[0]][position_end[1]] = Queen(board[position_end[0]][position_end[1]].color)
                    else:
                        #open promotion window Here
                        pass

def check_if_castling():
        if board[position_start[0]][position_start[1]].name == 'white_king' or board[position_start[0]][position_start[1]].name == 'black_king':
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
        
        
            if board[x][y].color == 'white' and whites_turn[0] == False:
                board[x][y].ampasant = False
                
            elif board[x][y].color == 'black' and whites_turn[0] == True:
                board[x][y].ampasant = False
                
    # print('\n')

def update_board():
    for x in range(8):
        for y in range(8):
            exec(f"button_{x}_{y}.config(image = board[x][y].new_scaled_image)")

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
    for x in range(8):
        for y in range(8):
            if x%2 == 0 and y%2 == 0 or x%2 != 0 and y%2 != 0:
                 bg_color = from_rgb((238,238,210))
            else:
                 bg_color = from_rgb((118,150,86))
            exec(f"button_{x}_{y}.config(bg = bg_color)")
            exec(f"button_{x}_{y}.config(bg = bg_color)")

    if len(position_start) == 0:
        # print('position_start before = ', position_start)
        position_start.append(a)
        position_start.append(b)
        # print('position start after = ',position_start)
        
    elif len(position_start) == 2:
        position_end.append(a)
        position_end.append(b)

        #print(board[position_start[0]][position_start[1]].name)
        
        valid_move[0] = board[position_start[0]][position_start[1]].is_legal(valid_move, whites_turn, board, position_start, position_end)
        
        if valid_move[0] == True:
            check_if_promoting()
            check_if_castling()
            update_ampasant()

            board[position_end[0]][position_end[1]] = board[position_start[0]][position_start[1]]
            board[position_start[0]][position_start[1]] = empty_square
            
            board[position_end[0]][position_end[1]].has_moved = True
            

            update_board()
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


#used to make buttons with text resize according to pixels not text
pixel = PhotoImage(width=1, height=1)

#game is made of 3 main frames: left, right, and center
left_frame = Frame(r, bg = from_rgb((0, 128, 128)))
left_frame.place(x=0, y=0, width=100, height=600)

right_frame = Frame(r, bg = from_rgb((0, 128, 128)))
right_frame.place(x=500, y=0, width=100, height=600)

center_frame = Frame(r, bg = 'grey25')
center_frame.place(x=100, y=0, width=400, height=600)

#stuff inside center frame: chess board, opponents username, and users name
center_frame.rowconfigure(0, weight=1)
top_bar = Label(center_frame, bg = 'grey25')
top_bar.grid(column=0, row=0, columnspan=8, sticky=NSEW)

for x in range(8):
    for y in range(8):
        if x%2 == 0 and y%2 == 0 or x%2 != 0 and y%2 != 0:
            bg_color = from_rgb((238,238,210))
        else:
            bg_color = from_rgb((118,150,86))
        exec(f"button_{x}_{y} = tk.Button(center_frame,image = board[x][y].new_scaled_image, bg = bg_color, width = (400/8)-2, height = (400/8)-2, border=0, command= lambda: pressed(button_{x}_{y},{x},{y},position_start,position_end, board))")
        exec(f"button_{x}_{y}.grid(row=x+1,column=y)")

center_frame.rowconfigure(9, weight=1)
bottom_bar = Label(center_frame, bg = 'grey25')
bottom_bar.grid(column=0, row=9, columnspan=8, sticky=NSEW)

#stuff inside left side bar: exit game, setting, and ...
button_stop = Button(left_frame, text='Exit',width=100-2,padx=0, pady=10, border=0, font=('Helvatical bold',int(10)), bg = from_rgb((0, 128, 128)), fg = 'black', image=pixel, compound="c", command=r.destroy) 
button_stop.grid(row=0, column=0, sticky="nsew") 
button_stop.bind('<Enter>', lambda event: enter(event, button_stop))             
button_stop.bind('<Leave>', lambda event: exit_(event, button_stop))

button_setting = Button(left_frame, text='Settings', width=100-2,padx=0, pady=10, border=0, font=('Helvatical bold',int(10)), bg = from_rgb((0, 128, 128)), fg = 'black', image=pixel, compound="c", command= lambda: open_settings(r, from_rgb, exit_settings)) 
button_setting.grid(row=1, column=0, sticky="nsew") 
button_setting.bind('<Enter>', lambda event: enter(event, button_setting))             
button_setting.bind('<Leave>', lambda event: exit_(event, button_setting))


#tracks the screen size
tracker = WindowTracker(r)
tracker.bind_config(board)




r.mainloop() 

