"""
ideas to add:
flip board (home page)
play computer(home page)
play online (home page)
play local (home page)

full screen exclusive - windowed (settings)
auto queen (settings)
click show legal moves - hover show legal moves - dont show legal moves (settings)
auto flip (settings - local games only)
show/hide opponents colors/skins (maybe add to settings)

"""



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

# list_of_pieces_classes = [Rook, Knight, Bishop, Queen, King, Pawn, EmptySquare]

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
b = [b_pawn1, b_pawn2, b_pawn3, empty_square, empty_square, empty_square, empty_square, empty_square]
c = [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square]
d = [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square]
e = [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square]
f = [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square]
g = [w_pawn1, w_pawn2, w_pawn3, empty_square, empty_square, empty_square, empty_square, empty_square]
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
                board_of_buttons[x][y].config(width=int(chess_board_width*(1/8))-1, height=int(chess_board_width*(1/8)), image=board[x][y].rescale_img())
            else:
                board_of_buttons[x][y].config(width=int(chess_board_width*(1/8))-1, height=int(chess_board_width*(1/8)), image=board[x][y].new_image)

    # print(f"{tracker.width=}")

def enter(event, button): # function to be called when mouse enters in a frame
    button.config(bg=rgb_to_hex(settings.menu_button_highlight_color))
	# print('Button-2 pressed at x = % d, y = % d'%(event.x, event.y))

def exit_(event, button): # function to be called when mouse exits the frame
    button.config(bg=rgb_to_hex(settings.menu_button_color))
	# print('Button-3 pressed at x = % d, y = % d'%(event.x, event.y))  



# def show_legal_moves(board, position_start):
#     # for x in range(8):
#     #     for y in range(8):
#     #         temp_valid_move = True
#     #         temp_position_end = [x,y]
#     #         #make sure function (.is_legal) doesn't manipulate the global var valid_move
#     #         #its definitly changing valid move
#     #         if board[position_start[0]][position_start[1]].is_legal(temp_valid_move, whites_turn, board, position_start, temp_position_end) == True:
#     #             board_of_buttons[x][y].config(image=board[x][y].show_legal_move_img)
#     pass

def exit_settings(r,s):
    # update_buttons_from_settings(button_setting, button_stop)
    
    s.destroy()
    r.state('zoomed')
    r.state('normal')

def open_settings(r, rgb_to_hex, exit_settings):
    settings.open_settings_window(r, rgb_to_hex, exit_settings)

def update_buttons_from_settings(settings, *args):
        print(f"HERE{settings.size}")
        for arg in args:
            arg.config(width=int(.25*1.3*int(settings.size)), height=int(.1*1.3*int(settings.size)),font=('Helvatical bold',int(.2*int(settings.size))), bg = 'teal', fg = 'black')
            arg.config(width=int(.25*1.3*int(settings.size)), height=int(.1*1.3*int(settings.size)),font=('Helvatical bold',int(.2*int(settings.size))), bg = 'teal', fg = 'black')
            
        for x in range(8):
            for y in range(8):
                board_of_buttons[x][y].config(image = board[x-1][y-1].new_image)
                
def check_if_promoting():
    if board[position_start[0]][position_start[1]].name == 'white_pawn' or board[position_start[0]][position_start[1]].name == 'black_pawn':
        if board[position_start[0]][position_start[1]].promoted == True:
            if settings.auto_queen == True:
                board[position_start[0]][position_start[1]] = Queen(board[position_start[0]][position_start[1]].color)
            else:
                #open promotion window Here
                pass

def check_if_castling():
        #if your moving a king piece 2 square to either side
        if (board[position_start[0]][position_start[1]].name == 'white_king' and abs(position_start[1] - position_end[1]) == 2
            or board[position_start[0]][position_start[1]].name == 'black_king' and abs(position_start[1] - position_end[1]) == 2):

            #if you castling to the right
            if position_start[1] > position_end[1]:
                for i in range(0, position_end[1]):
                    #if the for loop finds a rook, break
                    if board[position_start[0]][i].name == 'black_rook' and board[position_start[0]][position_start[1]].name == 'black_king' or board[position_start[0]][i].name == 'white_rook' and board[position_start[0]][position_start[1]].name == 'white_king':
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
            board_of_buttons[x][y].config(image = board[x][y].new_image)

def update_turn():
    if whites_turn[0] == True:
        whites_turn[0] = False
    elif whites_turn[0] == False:
        whites_turn[0] = True

def rgb_to_hex(rgb):
    """
    translates an rgb tuple of int to hexadecimal: a tkinter friendly color code
    """
    r, g, b = rgb
    return f'#{r:02x}{g:02x}{b:02x}'

def hex_to_rgb(hex_string):
    # Remove the '#' if present in the input
    hex_string = hex_string.lstrip('#')

    # Convert the hexadecimal string to RGB integers
    return tuple(int(hex_string[i:i+2], 16) for i in (0, 2, 4)) 

def reset_board_bg(wipe=''):
    for x in range(8):
        # print('\n')
        for y in range(8):
            # print(x,y,board_of_buttons[x][y]['bg'] , rgb_to_hex(settings.primary_move_color) , rgb_to_hex(settings.secondary_move_color))

            #clears everything if wipe == 'wipe' 
            if wipe == 'wipe':
                if x%2 == 0 and y%2 == 0 or x%2 != 0 and y%2 != 0:
                    board_of_buttons[x][y].config(bg = rgb_to_hex(settings.dark_square_color))
                else:
                    board_of_buttons[x][y].config(bg = rgb_to_hex(settings.light_square_color))

            #doesnt clear yellow highlight from moving a piece if wipe != 'wipe 
            elif not (board_of_buttons[x][y]['bg'] == rgb_to_hex(settings.primary_move_color) or board_of_buttons[x][y]['bg'] == rgb_to_hex(settings.secondary_move_color)):
                if x%2 == 0 and y%2 == 0 or x%2 != 0 and y%2 != 0:
                    board_of_buttons[x][y].config(bg = rgb_to_hex(settings.dark_square_color))
                else:
                    board_of_buttons[x][y].config(bg = rgb_to_hex(settings.light_square_color))
            
def pressed(a, b, position_start, position_end, board):
    button = board_of_buttons[a][b]

    #resets the boards backgrounds to remove button click highlights
    reset_board_bg('clear button clicked highlights')

    #highlights the square you clicked on
    button.config(bg = rgb_to_hex(settings.highlight_square_color))

    if board[a][b].color == 'white' and whites_turn[0] == True or board[a][b].color == 'black' and whites_turn[0] == False:
        for i in range(len(position_start)):
            position_start.pop(0)

        if len(position_start) == 0:
            # print('position_start before = ', position_start)
            position_start.append(a)
            position_start.append(b)
            # print('position start after = ',position_start)

            show_legal_moves(board, position_start)
        
    elif len(position_start) == 2:
        position_end.append(a)
        position_end.append(b)
        # print('position end after = ',position_end)

        #print(board[position_start[0]][position_start[1]].name)
        valid_move[0] = board[position_start[0]][position_start[1]].is_legal(valid_move, whites_turn, board, position_start, position_end)
        
        if valid_move[0] == True:
            check_if_promoting()
            check_if_castling()
            update_ampasant()

            board[position_end[0]][position_end[1]] = board[position_start[0]][position_start[1]]
            board[position_start[0]][position_start[1]] = empty_square
            
            board[position_end[0]][position_end[1]].has_moved = True

            reset_board_bg('wipe')

            #highlights the square a piece moved from and to
            board_of_buttons[position_end[0]][position_end[1]].config(bg = rgb_to_hex(settings.primary_move_color))

            if (abs(position_start[0]-position_end[0]) == 1 and abs(position_start[1]-position_end[1]) == 0
                or abs(position_start[0]-position_end[0]) == 0 and abs(position_start[1]-position_end[1]) == 1):
                board_of_buttons[position_start[0]][position_start[1]].config(bg = rgb_to_hex(settings.secondary_move_color))

            else:
                board_of_buttons[position_start[0]][position_start[1]].config(bg = rgb_to_hex(settings.primary_move_color))

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
        # reset_board_bg()
        pass
        
    
    
    # print(f"row = {a}, col = {b}")


#tracks the screen size
tracker = WindowTracker(r)
tracker.bind_config(board)

#used to make buttons with text resize according to pixels not text
pixel = PhotoImage(width=1, height=1)

#game is made of 3 main frames: left, right, and center
left_frame = Frame(r, bg = rgb_to_hex(settings.left_side_bar_bg_color))
left_frame.place(x=0, y=0, width=100, height=600)

right_frame = Frame(r, bg = rgb_to_hex(settings.right_side_bar_bg_color))
right_frame.place(x=500, y=0, width=100, height=600)

center_frame = Frame(r)
center_frame.place(x=100, y=0, width=400, height=600)

#stuff inside center frame: chess board, opponents username, and users name
center_frame.rowconfigure(0, weight=1)
top_bar = Label(center_frame, bg = rgb_to_hex(settings.top_top_bar_bg_color))
top_bar.grid(column=0, row=0, columnspan=8, sticky=NSEW)




board_of_buttons = []

for x in range(8):
    lyst = []
    for y in range(8):
        if x%2 == 0 and y%2 == 0 or x%2 != 0 and y%2 != 0:
            bg_color = rgb_to_hex(settings.dark_square_color)
        else:
            bg_color = rgb_to_hex(settings.light_square_color)
        button_on_board = tk.Button(center_frame,image = board[x][y].new_image, bg = bg_color, activebackground=bg_color, width = (400/8)-2, height = (400/8)-2, border=0)
        button_on_board.x, button_on_board.y = int(x), int(y)
        button_on_board.grid(row=x+1,column=y)

        lyst.append(button_on_board)
    board_of_buttons.append(list(lyst))

for x in range(8):
    for y in range(8):
        # print(int(board_of_buttons[x][y].x), int(board_of_buttons[x][y].y))
        board_of_buttons[x][y].config(command= lambda x=x, y=y: pressed(x, y, position_start, position_end, board))





center_frame.rowconfigure(9, weight=1)
bottom_bar = Label(center_frame, bg = rgb_to_hex(settings.bottom_bottom_bar_bg_color))
bottom_bar.grid(column=0, row=9, columnspan=8, sticky=NSEW)

#stuff inside left side bar: exit game, setting, and ...
button_stop = Button(left_frame, text='Exit',width=100-2,padx=0, pady=10, border=0, font=('Helvatical bold',int(10)), bg = rgb_to_hex(settings.menu_button_color), fg = 'black', image=pixel, compound="c", command=r.destroy) 
button_stop.grid(row=0, column=0, sticky="nsew") 
button_stop.bind('<Enter>', lambda event: enter(event, button_stop))             
button_stop.bind('<Leave>', lambda event: exit_(event, button_stop))

button_setting = Button(left_frame, text='Settings', width=100-2,padx=0, pady=10, border=0, font=('Helvatical bold',int(10)), bg = rgb_to_hex(settings.menu_button_color), fg = 'black', image=pixel, compound="c", command= lambda: open_settings(r, rgb_to_hex, exit_settings)) 
button_setting.grid(row=1, column=0, sticky="nsew") 
button_setting.bind('<Enter>', lambda event: enter(event, button_setting))             
button_setting.bind('<Leave>', lambda event: exit_(event, button_setting))







r.mainloop() 

