"""
--HOME PAGE--
ideas to add:
flip board 
play computer
play online 
play local 

--SETTINGS PAGE--
full screen exclusive - windowed (settings)
auto queen (settings)
click show legal moves - hover show legal moves - dont show legal moves (settings)
auto flip (settings - local games only)
show/hide opponents colors/skins (maybe add to settings)

--STORE DATA--
username
password
email/phone number
all of their settings (color, display prefrence, etc)
game history


"""



# from tkinter import *
# from PIL import Image, ImageTk


from chess_pieces import *


root = tk.Tk() 
root.title('Chess') 
root.geometry('900x600-0+0')
root.config(bg = 'grey')

# root.overrideredirect(True)
# root.state('zoomed')

position_start = []
position_end = []


list_of_pieces_classes = [Rook, Knight, Bishop, Queen, King, Pawn, EmptySquare]

empty_square = EmptySquare()

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

class GameStateTracker():
    def create_new_board(self):
    
        self.board = [
        [Rook('black'), Knight('black'), Bishop('black'), Queen('black'), King('black'), Bishop('black'), Knight('black'), Rook('black')],
        [Pawn('black'), Pawn('black'), Pawn('black'), Pawn('black'), Pawn('black'), Pawn('black'), Pawn('black'), Pawn('black')],
        [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square],
        [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square],
        [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square],
        [empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square, empty_square],
        [Pawn('white'), Pawn('white'), Pawn('white'), Pawn('white'), Pawn('white'), Pawn('white'), Pawn('white'), Pawn('white')],
        [Rook('white'), Knight('white'), Bishop('white'), Queen('white'), King('white'), Bishop('white'), Knight('white'), Rook('white')]
            ]
        try:
            if board_of_buttons and text_widget:
                pass
        except:
            pass
        else:
                update_board(self.board)
                reset_board_bg('wipe')
                clear_text_widget(text_widget)

                
        

    def __init__(self):
        self.master_move_history = []
        self.move_count = 0
        self.current_displayed_move = 0
        self.whites_turn = True

        self.create_new_board()

        self.master_move_history.append([])
        for x in range(8):
            self.master_move_history[-1].append([])
            for y in range(8):
                self.master_move_history[-1][-1].append(self.board[x][y])
    
    def piece_was_moved(self):
        self.move_count += 1
        self.current_displayed_move = self.move_count
        update_board(self.board)
        
        if self.move_count % 2 == 0:
            self.whites_turn = True
        else:
            self.whites_turn = False

        #stores the current position of each piece into a list of positions
        self.master_move_history.append([])
        for x in range(8):
            self.master_move_history[-1].append([])
            for y in range(8):
                self.master_move_history[-1][-1].append(self.board[x][y])

        # count=0
        # print('-----------------------')
        # for z in self.master_move_history:
        #     print()
        #     for y in z:
        #         for x in y:
        #             count+=1
        #             print(x.char_name,end=' ')
        #             if count % 8 == 0:
        #                 print()
    
    def show_previous_move(self):
        if self.current_displayed_move > 0:
            self.current_displayed_move += -1
            update_board(self.master_move_history[self.current_displayed_move])
            print(self.current_displayed_move)
    
    def show_next_move(self):
        if self.current_displayed_move < self.move_count:
            self.current_displayed_move += 1
            update_board(self.master_move_history[self.current_displayed_move])
            print(self.current_displayed_move)

class WindowTracker():
    """ windows resize event tracker """

    def __init__(self, root):
        self.root = root
        self.width, self.height = root.winfo_width(), root.winfo_height()
        self._func_id = None

    def bind_config(self, game_state):
        self._func_id = self.root.bind("<Configure>", lambda event: self.resize(event, game_state))

    def unbind_config(self):  # Untested.
        if self._func_id: 
            self.root.unbind("<Configure>", self._func_id)
            self._func_id = None

    def resize(self, event, game_state):
        if( event.widget == self.root and
           (self.width != event.width or self.height != event.height)):
            # print(f'{event.height}, {event.width}')
            self.width, self.height = event.width, event.height
            

            # scale = min(self.width, self.height)
            if self.width*(8/12) >= self.height*(8/12):
                self.chess_board_width = self.height * (10/12)
                self.side_bar_width = (self.width-self.chess_board_width)/2
                settings.size = int(self.chess_board_width*(1/10))


            elif self.width*(8/12) < self.height*(8/12):
                self.chess_board_width = self.width * (10/12)
                self.side_bar_width = (self.width-self.chess_board_width)/2
                settings.size = int(self.chess_board_width*(1/10))

            else:
                print('something else')

            rescale_game(game_state,int(self.side_bar_width), int(self.chess_board_width))

def rescale_game(game_state,side_bar_width,chess_board_width):
    left_frame.place(x=0, y=0, width=side_bar_width, height=tracker.height)
    right_frame.place(x=side_bar_width+chess_board_width, y=0, width=side_bar_width+3, height=tracker.height)
    center_frame.place(x=side_bar_width, y=0, width=chess_board_width, height=tracker.height)

    button_stop.config(width=side_bar_width)
    button_setting.config(width=side_bar_width)
    
    resized_empty_square = 0
    for x in range(8):
        for y in range(8):
            if game_state.board[x][y].name == 'empty_square':
                resized_empty_square += 1
            if game_state.board[x][y].name != 'empty_square' or resized_empty_square == 1:
                board_of_buttons[x][y].config(width=int(chess_board_width*(1/8))-1, height=int(chess_board_width*(1/8)), image=game_state.board[x][y].rescale_img())
            else:
                board_of_buttons[x][y].config(width=int(chess_board_width*(1/8))-1, height=int(chess_board_width*(1/8)), image=game_state.board[x][y].image)
    
    # print(f"{tracker.width=}")

def enter(event, button): # function to be called when mouse enters in a frame
    button.config(bg=rgb_to_hex(settings.menu_button_highlight_color))
	# print('Button-2 pressed at x = % d, y = % d'%(event.x, event.y))

def exit_(event, button): # function to be called when mouse exits the frame
    button.config(bg=rgb_to_hex(settings.menu_button_color))
	# print('Button-3 pressed at x = % d, y = % d'%(event.x, event.y))  

def show_legal_moves(game_state, position_start):
    for x in range(8):
        for y in range(8):
            temp_position_end = [x,y]
            if game_state.board[position_start[0]][position_start[1]].is_legal(bool(game_state.whites_turn),game_state, position_start, temp_position_end) == True:
                if settings.show_legal_moves == True:
                    board_of_buttons[x][y].config(image=game_state.board[x][y].show_legal_move_img)
    
def exit_settings(r, s):
    root.overrideredirect(settings.display == 'full_screen')
    if settings.display == 'full_screen':
        root.state('zoomed')
    
    r.lift(s)

    for button in lyst_of_game_buttons:
        button.config(state=NORMAL)

    reset_board_bg()
    
def open_settings(r, s, lyst_of_game_buttons, button_stop):
    for button in lyst_of_game_buttons:    
        button.config(state=DISABLED)
    button_stop.config(state=NORMAL)

    s.lift(r)
    
def check_if_promoting():
    if game_state.board[position_start[0]][position_start[1]].name == 'white_pawn' or game_state.board[position_start[0]][position_start[1]].name == 'black_pawn':
        if game_state.board[position_start[0]][position_start[1]].promoted == True:
            if settings.auto_queen == True:
                game_state.board[position_start[0]][position_start[1]] = Queen(game_state.board[position_start[0]][position_start[1]].color)
            else:
                #open promotion window Here
                game_state.board[position_start[0]][position_start[1]] = Queen(game_state.board[position_start[0]][position_start[1]].color)
                print("NO INSTRUCTION FOR NON AUTO QUEEN PROMOTION")

def check_if_castling():
        #if your moving a king piece 2 square to either side
        if (game_state.board[position_start[0]][position_start[1]].name == 'white_king' and abs(position_start[1] - position_end[1]) == 2
            or game_state.board[position_start[0]][position_start[1]].name == 'black_king' and abs(position_start[1] - position_end[1]) == 2):

            #if you castling to the right
            if position_start[1] > position_end[1]:
                for i in range(0, position_end[1]):
                    #if the for loop finds a rook, break
                    if game_state.board[position_start[0]][i].name == 'black_rook' and game_state.board[position_start[0]][position_start[1]].name == 'black_king' or game_state.board[position_start[0]][i].name == 'white_rook' and game_state.board[position_start[0]][position_start[1]].name == 'white_king':
                        break

                game_state.board[position_end[0]][position_end[1]+1] = game_state.board[position_start[0]][i]
                game_state.board[position_start[0]][i] = empty_square

            elif position_start[1] < position_end[1]:
                for i in range(7, position_end[1], -1):
                    if game_state.board[position_start[0]][i].name == 'black_rook' and game_state.board[position_start[0]][position_start[1]].name == 'black_king' or game_state.board[position_start[0]][i].name == 'white_rook' and game_state.board[position_start[0]][position_start[1]].name == 'white_king':
                        break
                    
                game_state.board[position_end[0]][position_end[1]-1] = game_state.board[position_start[0]][i]
                game_state.board[position_start[0]][i] = empty_square

def update_ampasant():
    for x in range(8):
        # print('')
        for y in range(8):
        #     if board[x][y].can_be_taken_by_ampasant == False:
        #         print(0,end = '')
        #     else:
        #         print(1,end='')
        
        
            if game_state.board[x][y].color == 'white' and game_state.whites_turn == False:
                game_state.board[x][y].can_be_taken_by_ampasant = False
                
            elif game_state.board[x][y].color == 'black' and game_state.whites_turn == True:
                game_state.board[x][y].can_be_taken_by_ampasant = False
                
    # print('\n')

def update_board(board_state):
    resized_empty_square = 0
    for x in range(8):
        for y in range(8):
            board_of_buttons[x][y].config(image = board_state[x][y].image)
         
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
            #clears all overlays
            board_of_buttons[x][y].config(image=game_state.board[x][y].image)

            #clears everything if wipe == 'wipe' 
            if wipe == 'wipe':
                if x%2 == 0 and y%2 == 0 or x%2 != 0 and y%2 != 0:
                    board_of_buttons[x][y].config(bg = rgb_to_hex(settings.light_square_color))
                else:
                    board_of_buttons[x][y].config(bg = rgb_to_hex(settings.dark_square_color))

            #doesnt clear yellow highlight from moving a piece if wipe != 'wipe 
            elif not (board_of_buttons[x][y]['bg'] == rgb_to_hex(settings.primary_move_color) or board_of_buttons[x][y]['bg'] == rgb_to_hex(settings.secondary_move_color)):
                if x%2 == 0 and y%2 == 0 or x%2 != 0 and y%2 != 0:
                    board_of_buttons[x][y].config(bg = rgb_to_hex(settings.light_square_color))
                else:
                    board_of_buttons[x][y].config(bg = rgb_to_hex(settings.dark_square_color))
            
def flip_board(settings, board_of_buttons):
    settings.whites_perspective = not settings.whites_perspective
    for x in range(8):
        for y in range(8):
            # print(board_of_buttons[x][y])
            if settings.whites_perspective == True:
                board_of_buttons[x][y].grid(row=x+1, column=y)
            else:
                board_of_buttons[x][y].grid(row=7-x+1, column=y)

def clear_text_widget(text_widget):
    text_widget.config(state=NORMAL)
    text_widget.delete(1.0, tk.END)  # Clear from start (1.0) to end (tk.END)
    text_widget.config(state=DISABLED)

def move_piece(game_state, position_start, position_end):
    move_start = chr(position_start[1]+97) + str(8-position_start[0]) 
    move_end = chr(position_end[1]+97) + str(8-position_end[0])
    
    text = f"{game_state.board[position_start[0]][position_start[1]].annotated_name[1]}{move_start}{'x' if game_state.board[position_end[0]][position_end[1]].name != 'empty_square' else ''}{game_state.board[position_end[0]][position_end[1]].annotated_name[1]}{move_end}"
    text = f"{text:<8}"
    text_widget.config(state=NORMAL)
    text_widget.insert(tk.END, text)
    text_widget.insert(tk.END, '\n\n' if game_state.whites_turn == False else '  ')
    text_widget.config(state=DISABLED)
    
    #extra command if pawn is taking using ampasant
    if game_state.board[position_start[0]][position_start[1]].is_taking_by_ampasant[0] == True:
        game_state.board[position_end[0]+game_state.board[position_start[0]][position_start[1]].is_taking_by_ampasant[1]][position_end[1]] = game_state.board[position_end[0]][position_end[1]]
        
    game_state.board[position_end[0]][position_end[1]] = game_state.board[position_start[0]][position_start[1]]
    game_state.board[position_start[0]][position_start[1]] = empty_square
    
    game_state.board[position_end[0]][position_end[1]].has_moved = True
         
def pressed(a, b, position_start, position_end, game_state):
    button = board_of_buttons[a][b]

    #resets the boards backgrounds to remove button click highlights
    reset_board_bg('soft wipe')

    #highlights the square you clicked on
    button.config(bg = rgb_to_hex(settings.highlight_square_color))

    if game_state.board[a][b].color == 'white' and game_state.whites_turn == True or game_state.board[a][b].color == 'black' and game_state.whites_turn == False:
        for i in range(len(position_start)):
            position_start.pop(0)

        if len(position_start) == 0:
            # print('position_start before = ', position_start)
            position_start.append(a)
            position_start.append(b)
            # print('position start after = ',position_start)

            show_legal_moves(game_state, position_start)
        
    elif len(position_start) == 2:
        position_end.append(a)
        position_end.append(b)
        # print('position end after = ',position_end)

        #print(board[position_start[0]][position_start[1]].name)
        valid_move = game_state.board[position_start[0]][position_start[1]].is_legal(bool(game_state.whites_turn), game_state, position_start, position_end)

        if valid_move == True:
            check_if_promoting()
            check_if_castling()
            update_ampasant()

            move_piece(game_state, position_start, position_end)

            reset_board_bg('wipe')

            #highlights the square a piece moved from and to
            board_of_buttons[position_end[0]][position_end[1]].config(bg = rgb_to_hex(settings.primary_move_color))

            if (abs(position_start[0]-position_end[0]) == 1 and abs(position_start[1]-position_end[1]) == 0
                or abs(position_start[0]-position_end[0]) == 0 and abs(position_start[1]-position_end[1]) == 1):
                board_of_buttons[position_start[0]][position_start[1]].config(bg = rgb_to_hex(settings.secondary_move_color))

            else:
                board_of_buttons[position_start[0]][position_start[1]].config(bg = rgb_to_hex(settings.primary_move_color))

            update_board(game_state.board)
            game_state.piece_was_moved()

        else:
            pass
            #doesnt move the piece
            
            
        for i in range(len(position_start)):
            position_start.pop(0)
        for j in range(len(position_end)):
            position_end.pop(0)
    
    else:
        # reset_board_bg()
        pass
        
    
    
    # print(f"row = {a}, col = {b}")

#tracks vaiables and different game states
game_state = GameStateTracker()

game_state.create_new_board()

#tracks the screen size
tracker = WindowTracker(root)
tracker.bind_config(game_state)

#used to make buttons with text resize according to pixels not text
pixel = PhotoImage(width=1, height=1)

#make the main frame (r) for the game
home = tk.Frame(root, bg="blue")
home.place(relwidth=1, relheight=1)  # Filling the entire window

#initialize settings Frame
s = settings.init_settings_frame(root, home, rgb_to_hex, exit_settings, pixel)

#moves the settings frame behind the game frame
home.lift(s)

#game is made of 3 main frames: left, right, and center
left_frame = Frame(home, bg = rgb_to_hex(settings.left_side_bar_bg_color))
left_frame.place(x=0, y=0, width=100, height=600)

right_frame = Frame(home, bg = rgb_to_hex(settings.right_side_bar_bg_color))
right_frame.place(x=500, y=0, width=100, height=600)

center_frame = Frame(home)
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
            bg_color = rgb_to_hex(settings.light_square_color)
        else:
            bg_color = rgb_to_hex(settings.dark_square_color)
        button_on_board = tk.Button(center_frame,image = game_state.board[x][y].image, bg = bg_color, activebackground=bg_color, width = (400/8)-2, height = (400/8)-2, border=0)
        button_on_board.x, button_on_board.y = int(x), int(y)
        if settings.whites_perspective == True:
            button_on_board.grid(row=x+1,column=y)
        else:
            button_on_board.grid(row=x+1,column=y)

        lyst.append(button_on_board)
    board_of_buttons.append(list(lyst))

for x in range(8):
    for y in range(8):
        board_of_buttons[x][y].config(command= lambda x=x, y=y: pressed(x, y, position_start, position_end, game_state))


center_frame.rowconfigure(9, weight=1)
bottom_bar = Label(center_frame, bg = rgb_to_hex(settings.bottom_bottom_bar_bg_color))
bottom_bar.grid(column=0, row=9, columnspan=8, sticky=NSEW)

#stuff inside left side bar: exit game, setting, and ...
button_stop = Button(left_frame, text='Exit',width=100-2,padx=0, pady=10, border=0, font=('Helvatical bold', 10), bg = rgb_to_hex(settings.menu_button_color), fg = 'black', image=pixel, compound="c", command=root.destroy) 
button_stop.grid(row=0, column=0, sticky="nsew") 
button_stop.bind('<Enter>', lambda event: enter(event, button_stop))             
button_stop.bind('<Leave>', lambda event: exit_(event, button_stop))

button_setting = Button(left_frame, text='Settings', width=100-2,padx=0, pady=10, border=0, font=('Helvatical bold', 10), bg = rgb_to_hex(settings.menu_button_color), fg = 'black', image=pixel, compound="c", command= lambda: open_settings(home,s,lyst_of_game_buttons, button_stop)) 
button_setting.grid(row=1, column=0, sticky="nsew") 
button_setting.bind('<Enter>', lambda event: enter(event, button_setting))             
button_setting.bind('<Leave>', lambda event: exit_(event, button_setting))

button_play_online = Button(left_frame, text='Play Online', width=100-2,padx=0, pady=10, border=0, font=('Helvatical bold', 10), bg = rgb_to_hex(settings.menu_button_color), fg = 'black', image=pixel, compound="c")#, command= lambda: open_settings(home,s,lyst_of_game_buttons, button_stop)) 
button_play_online.grid(row=2, column=0, sticky="nsew") 
button_play_online.bind('<Enter>', lambda event: enter(event, button_play_online))             
button_play_online.bind('<Leave>', lambda event: exit_(event, button_play_online))
button_play_online.config(state='disabled')

button_play_local = Button(left_frame, text='Play Local', width=100-2,padx=0, pady=10, border=0, font=('Helvatical bold', 10), bg = rgb_to_hex(settings.menu_button_color), fg = 'black', image=pixel, compound="c")#, command= lambda: open_settings(home,s,lyst_of_game_buttons, button_stop)) 
button_play_local.grid(row=3, column=0, sticky="nsew") 
button_play_local.bind('<Enter>', lambda event: enter(event, button_play_local))             
button_play_local.bind('<Leave>', lambda event: exit_(event, button_play_local))
button_play_local.config(state='disabled')

button_play_bot = Button(left_frame, text='Play Computer', width=100-2,padx=0, pady=10, border=0, font=('Helvatical bold', 10), bg = rgb_to_hex(settings.menu_button_color), fg = 'black', image=pixel, compound="c")#, command= lambda: open_settings(home,s,lyst_of_game_buttons, button_stop)) 
button_play_bot.grid(row=4, column=0, sticky="nsew") 
button_play_bot.bind('<Enter>', lambda event: enter(event, button_play_bot))             
button_play_bot.bind('<Leave>', lambda event: exit_(event, button_play_bot))
button_play_bot.config(state='disabled')

#stuff inside right side bar: move history, and ...
reset_board_button = Button(right_frame, text='Reset Board', width=100-2,padx=0, pady=10, border=0, font=('Helvatical bold', 10), bg = rgb_to_hex(settings.menu_button_color), fg = 'black', image=pixel, compound="c", command= lambda: game_state.create_new_board())
reset_board_button.pack(side=TOP, fill=X) 
reset_board_button.bind('<Enter>', lambda event: enter(event, reset_board_button))             
reset_board_button.bind('<Leave>', lambda event: exit_(event, reset_board_button))

flip_board_button = Button(right_frame, text='Flip Board', width=100-2,padx=0, pady=10, border=0, font=('Helvatical bold', 10), bg = rgb_to_hex(settings.menu_button_color), fg = 'black', image=pixel, compound="c", command= lambda: flip_board(settings, board_of_buttons)) 
flip_board_button.pack(side=TOP, fill=X) 
flip_board_button.bind('<Enter>', lambda event: enter(event, flip_board_button))             
flip_board_button.bind('<Leave>', lambda event: exit_(event, flip_board_button))


move_history_frame = Frame(right_frame, bg=rgb_to_hex(settings.menu_button_highlight_color))
move_history_frame.pack(fill="both", expand=True, padx=20, pady=(150, 250))

move_history_text_frame = Frame(move_history_frame, bg='green')
move_history_text_frame.grid(row=0, column=0, sticky="nsew")
# Create a Text widget
text_widget = tk.Text(move_history_text_frame, font=("Helvetica", 12), wrap="word", state=tk.DISABLED, bg=rgb_to_hex(settings.menu_button_highlight_color), width=1,height=1)
text_widget.pack(side=LEFT, fill="both", expand=True)

# Create a Scrollbar widget and attach it to the Text widget
scrollbar = ttk.Scrollbar(move_history_text_frame, command=text_widget.yview)
scrollbar.pack(side="right", fill="y")
text_widget.config(yscrollcommand=scrollbar.set)

# create a forward and back button for move history
move_history_button_frame = Frame(move_history_frame, bg='blue')
move_history_button_frame.grid(row=1, column=0, sticky="nsew")

move_back_history = Button(move_history_button_frame, text='Back', width=1, height=1, border=1, relief=SOLID, font=('Helvatical bold', 10), bg=rgb_to_hex(settings.menu_button_highlight_color), fg='black', image=pixel, compound="c", command=lambda: game_state.show_previous_move())
move_back_history.pack(side=LEFT, padx=0, pady=0, fill="both", expand=True)

move_forward_history = Button(move_history_button_frame, text='Forward', width=1, height=1, border=1, relief=SOLID, font=('Helvatical bold', 10), bg=rgb_to_hex(settings.menu_button_highlight_color), fg='black', image=pixel, compound="c", command=lambda: game_state.show_next_move())
move_forward_history.pack(side=RIGHT, padx=0, pady=0, fill="both", expand=True)

# Configure row and column weights to make both frames take equal space
move_history_frame.grid_rowconfigure(0, weight=3)
move_history_frame.grid_rowconfigure(1, weight=1)
move_history_frame.grid_columnconfigure(0, weight=1)


#usefull when i need to modify every single button
lyst_of_game_buttons = [button_stop, button_setting, button_play_local, button_play_online, button_play_bot, reset_board_button, flip_board_button]
for x in board_of_buttons:
    for y in x:
        lyst_of_game_buttons.append(y)


root.mainloop() 