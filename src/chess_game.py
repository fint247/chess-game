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
from tkinter import messagebox 
import time
import threading

root = tk.Tk() 
root.title('Chess') 
root.geometry('900x600-0+0')
root.config(bg = 'grey')


# Override the destroy method with destroy_root method
root.destroy = lambda: destroy_root(root)
# root.bind("<Destroy>", lambda e: destroy_root(root))
#flag used for closing the app
root.is_destroying = False

# root.overrideredirect(True)
# root.state('zoomed')

position_start = []
position_end = []


# list_of_pieces_classes = [Rook, Knight, Bishop, Queen, King, Pawn, EmptySquare]

empty_square = EmptySquare()

class GameStateTracker():
    def create_new_board(self, position_start, position_end):
        self.__init__()

        try:
            if game_widgets.board_of_buttons and game_widgets.text_widget:
                pass
        except:
            pass
        else:
                update_board(self.board, game_widgets)
                game_widgets.reset_board_bg('wipe')
                game_widgets.clear_text_widget(game_widgets.text_widget)
                #maybe fix code so that I dont have to pass any variables into create_new_board
                for x in range(len(position_start)):
                    position_start.pop(0)
                for x in range(len(position_end)):
                    position_end.pop(0)
   
    def __init__(self):
        self.master_move_history = []
        self.move_count = 0
        self.current_displayed_move = 0
        self.whites_turn = True
        self.draw = False
        self.in_simulation = False

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

        self.master_move_history.append([])
        for x in range(8):
            self.master_move_history[-1].append([])
            for y in range(8):
                self.master_move_history[-1][-1].append(self.board[x][y])
    
    def piece_was_moved(self):
        self.move_count += 1
        self.current_displayed_move = self.move_count
        update_board(self.board, game_widgets)
        
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
            update_board(self.master_move_history[self.current_displayed_move], game_widgets)
            # print(self.current_displayed_move)
    
    def show_next_move(self):
        if self.current_displayed_move < self.move_count:
            self.current_displayed_move += 1
            update_board(self.master_move_history[self.current_displayed_move], game_widgets)
            # print(self.current_displayed_move)

class WindowTracker():
    """ windows resize event tracker """

    def __init__(self, root):
        self.root = root
        self.width, self.height = root.winfo_width(), root.winfo_height()
        self._func_id = None

    def bind_config(self, game_state, game_widgets):
        self._func_id = self.root.bind("<Configure>", lambda event: self.resize(event, game_state, game_widgets))

    def unbind_config(self):  # Untested.
        if self._func_id: 
            self.root.unbind("<Configure>", self._func_id)
            self._func_id = None

    def resize(self, event, game_state, game_widgets):
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

            rescale_game(game_state, game_widgets, int(self.side_bar_width), int(self.chess_board_width))

class TimeControlTracker():
    def __init__(self):
        self.clock_start_time = 0
        self.clock_bonus_time = 0
        self.stop_timers = True

    def start_game_timers(self, game_widgets):
        self.stop_timers = False
        self.clock_increment_legth = 100 #ms

        if self.clock_start_time <= 0:
            pass



        else:
            self.self_time = self.clock_start_time
            self.opp_time = self.clock_start_time
            root.after(self.clock_increment_legth, self.update_timer)

    def update_timer(self):
        if self.self_time > 0 and self.opp_time > 0:
            root.after(self.clock_increment_legth, self.update_timer)

        elif self.self_time <= 0:
            show_game_reveiw("Black")
        elif self.opp_time <= 0:
            show_game_reveiw("White")

def offer_draw():
    if messagebox.askyesno("Draw Offer", "Are you sure you want to draw"):
        game_state.draw = True
        show_game_reveiw("Draw")
    
def resign():
    if game_state.whites_turn == True: 
        color = "White"
    else: 
        color = "Black"
    if messagebox.askyesno("Resign", f"Are you sure you ({color}) want to Resign"):
        if color == "White":
            color = "Black"
        else:
            color = "White"
        show_game_reveiw(color)

def show_game_reveiw(winner):
    time_control.stop_timers = True
    messagebox.showinfo(f"Game Reveiw", f"winner:  {winner}") 
    open_home()

def time_control_picker(contianer):
    time_control_bg_color = (150, 145, 135)
    
    time_control_button_list = []

    time_control.clock_start_time = 0
    time_control.clock_bonus_time = 0

    game_widgets.button_play_local.config(state=DISABLED)
    game_widgets.button_play_bot.config(state=DISABLED)
    game_widgets.button_play_online.config(state=DISABLED)


    time_control_frame = Frame(contianer, bg=rgb_to_hex(time_control_bg_color))
    time_control_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    time_control_menu_frame = Frame(time_control_frame, bg=rgb_to_hex((115, 125, 140)))
    time_control_menu_frame.place(relx=0,rely=0/6,relwidth=1,relheight=.2)

    time_control_back_button = Button(time_control_menu_frame, text='Back', command= lambda: time_control_back_func(time_control_frame))
    time_control_back_button.place(relx=.05,rely=.1,relwidth=.4, relheight=.8)

    time_control_back_button = Button(time_control_menu_frame, text='Start Game', command= lambda: start_local_game(time_control_frame))
    time_control_back_button.place(relx=.55,rely=.1,relwidth=.4, relheight=.8)


    no_time_control_frame = Frame(time_control_frame, bg=rgb_to_hex(time_control_bg_color))
    no_time_control_frame.place(relx=0,rely=1.5/6,relwidth=1,relheight=0.25)

    no_time_control_button = Button(no_time_control_frame, text='No Time Control', font=('Helvatical',10, 'bold'), command= lambda: time_control_button_press(time_control_button_list, no_time_control_button))
    no_time_control_button.place(relx=.1,rely=.0,relwidth=.8, relheight=.4)
    time_control_button_list.append(no_time_control_button)

    bullet_frame = Frame(time_control_frame, bg=rgb_to_hex(time_control_bg_color))
    bullet_frame.place(relx=0,rely=2/6,relwidth=1,relheight=0.25)

    bullet_lbl = Label(bullet_frame,text='Bullet:', font=('Helvatical bold', 25), bg=rgb_to_hex(time_control_bg_color))
    bullet_lbl.place(relx=0, rely=.25, relwidth=.2, relheight=.5)

    bullet_button_1 = Button(bullet_frame, text='1 min', font=('Helvatical',10, 'normal'), command= lambda start_time=1, bonus_time=0: time_control_button_press(start_time, bonus_time, time_control_button_list, bullet_button_1))
    bullet_button_1.place(relx=.25, rely=.3, relwidth=.2, relheight=.4)
    time_control_button_list.append(bullet_button_1)
    bullet_button_2 = Button(bullet_frame, text='1|1', font=('Helvatical',10, 'normal'), command= lambda start_time=1, bonus_time=1: time_control_button_press(start_time, bonus_time, time_control_button_list, bullet_button_2))
    bullet_button_2.place(relx=.50, rely=.3, relwidth=.2, relheight=.4)
    time_control_button_list.append(bullet_button_2)
    bullet_button_3 = Button(bullet_frame, text='2|1', font=('Helvatical',10, 'normal'), command= lambda start_time=2, bonus_time=1: time_control_button_press(start_time, bonus_time, time_control_button_list, bullet_button_3))
    bullet_button_3.place(relx=.75, rely=.3, relwidth=.2, relheight=.4)
    time_control_button_list.append(bullet_button_3)

    blitz_frame = Frame(time_control_frame, bg=rgb_to_hex(time_control_bg_color))
    blitz_frame.place(relx=0,rely=3/6,relwidth=1,relheight=0.25)

    blitz_lbl = Label(blitz_frame,text='Blitz:', font=('Helvatical bold', 25), bg=rgb_to_hex(time_control_bg_color))
    blitz_lbl.place(relx=0, rely=.25, relwidth=.2, relheight=.5)

    blitz_button_1 = Button(blitz_frame, text='3 min', font=('Helvatical',10, 'normal'), command= lambda start_time=3, bonus_time=0: time_control_button_press(start_time, bonus_time, time_control_button_list, blitz_button_1))
    blitz_button_1.place(relx=.25, rely=.3, relwidth=.2, relheight=.4)
    time_control_button_list.append(blitz_button_1)
    blitz_button_2 = Button(blitz_frame, text='3|2', font=('Helvatical',10, 'normal'), command= lambda start_time=3, bonus_time=2: time_control_button_press(start_time, bonus_time, time_control_button_list, blitz_button_2))
    blitz_button_2.place(relx=.50, rely=.3, relwidth=.2, relheight=.4)
    time_control_button_list.append(blitz_button_2)
    blitz_button_3 = Button(blitz_frame, text='5 min', font=('Helvatical',10, 'normal'), command= lambda start_time=5, bonus_time=0: time_control_button_press(start_time, bonus_time, time_control_button_list, blitz_button_3))
    blitz_button_3.place(relx=.75, rely=.3, relwidth=.2, relheight=.4)
    time_control_button_list.append(blitz_button_3)

    rapid_frame = Frame(time_control_frame, bg=rgb_to_hex(time_control_bg_color))
    rapid_frame.place(relx=0,rely=4/6,relwidth=1,relheight=0.25)

    rapid_lbl = Label(rapid_frame,text='Rapid:', font=('Helvatical bold', 25), bg=rgb_to_hex(time_control_bg_color))
    rapid_lbl.place(relx=0, rely=.25, relwidth=.2, relheight=.5)

    rapid_button_1 = Button(rapid_frame, text='10 min', font=('Helvatical',10, 'normal'), command= lambda start_time=10, bonus_time=0: time_control_button_press(start_time, bonus_time, time_control_button_list, rapid_button_1))
    rapid_button_1.place(relx=.25, rely=.3, relwidth=.2, relheight=.4)
    time_control_button_list.append(rapid_button_1)
    rapid_button_2 = Button(rapid_frame, text='10|5', font=('Helvatical',10, 'normal'), command= lambda start_time=10, bonus_time=5: time_control_button_press(start_time, bonus_time, time_control_button_list, rapid_button_2))
    rapid_button_2.place(relx=.50, rely=.3, relwidth=.2, relheight=.4)
    time_control_button_list.append(rapid_button_2)
    rapid_button_3 = Button(rapid_frame, text='15 min', font=('Helvatical',10, 'normal'), command= lambda start_time=15, bonus_time=0: time_control_button_press(start_time, bonus_time, time_control_button_list, rapid_button_3))
    rapid_button_3.place(relx=.75, rely=.3, relwidth=.2, relheight=.4)
    time_control_button_list.append(rapid_button_3)

    custom_frame = Frame(time_control_frame, bg=rgb_to_hex(time_control_bg_color))
    custom_frame.place(relx=0,rely=5/6,relwidth=1,relheight=0.25)

    custom_lbl = Label(custom_frame,text='Custum:', font=('Helvatical bold', 25), bg=rgb_to_hex(time_control_bg_color))
    custom_lbl.place(relx=0, rely=.15, relwidth=.25, relheight=.5)

    custom_button_1 = Button(custom_frame, text='Start Time')
    custom_button_1.place(relx=.33, rely=.2, relwidth=.2, relheight=.4)
    # time_control_button_list.append(custom_button_1)
    custom_button_2 = Button(custom_frame, text='Bonus Time')
    custom_button_2.place(relx=.66, rely=.2, relwidth=.2, relheight=.4)
    # time_control_button_list.append(custom_button_2)

    custom_button_1.config(state=DISABLED)
    custom_button_2.config(state=DISABLED)
    
def time_control_button_press(start_time, bonus_time, time_control_button_list, button_pressed):
    time_control.clock_start_time = start_time
    time_control.clock_bonus_time = bonus_time
    print(time_control.clock_start_time, time_control.clock_bonus_time)
    for button in time_control_button_list:
        if button is button_pressed:
            button.config(font=('Helvatical',9, 'bold'))
        else:
            button.config(font=('Helvatical',9, 'normal'))

def time_control_back_func(time_control_frame):
    game_widgets.button_play_local.config(state=NORMAL)
    # game_widgets.button_play_bot.config(state=NORMAL)
    # game_widgets.button_play_online.config(state=NORMAL)

    time_control_frame.destroy()

def start_local_game(time_control_frame):
    time_control_frame.destroy()
    game_widgets.reset_board_button.config(state=DISABLED)
    game_widgets.draw_button.config(state=NORMAL)
    game_widgets.resign_button.config(state=NORMAL)
    game_state.create_new_board(position_start, position_end)
    # start_game_timers.start()
    time_control.start_game_timers(game_widgets)

def open_home():
    game_state.create_new_board(position_start, position_end)
    game_widgets.draw_button.config(state=DISABLED)
    game_widgets.resign_button.config(state=DISABLED)
    game_widgets.reset_board_button.config(state=NORMAL)
    game_widgets.button_play_local.config(state=NORMAL)
    # game_widgets.button_play_online.config(state=NORMAL)
    # game_widgets.button_play_bot.config(state=NORMAL)

def start_computer_game():
    game_widgets.reset_board_button.config(state=DISABLED)
    game_state.create_new_board(position_start, position_end)

def rescale_game(game_state,game_widgets, side_bar_width,chess_board_width):
    game_widgets.left_frame.place(x=0, y=0, width=side_bar_width, height=tracker.height)
    game_widgets.right_frame.place(x=side_bar_width+chess_board_width, y=0, width=side_bar_width+3, height=tracker.height)
    game_widgets.center_frame.place(x=side_bar_width, y=0, width=chess_board_width, height=tracker.height)

    game_widgets.button_stop.config(width=side_bar_width)
    game_widgets.button_setting.config(width=side_bar_width)
    # move_history_frame.config(width=500, height=300)

    resized_empty_square = 0
    for x in range(8):
        for y in range(8):
            if game_state.board[x][y].name == 'empty_square':
                resized_empty_square += 1
            if game_state.board[x][y].name != 'empty_square' or resized_empty_square == 1:
                game_widgets.board_of_buttons[x][y].config(width=int(chess_board_width*(1/8))-1, height=int(chess_board_width*(1/8)), image=game_state.board[x][y].rescale_img())
            else:
                game_widgets.board_of_buttons[x][y].config(width=int(chess_board_width*(1/8))-1, height=int(chess_board_width*(1/8)), image=game_state.board[x][y].image)
    
    game_widgets.text_widget.config(font=("Helvetica", side_bar_width//20))


    # print(f"{tracker.width=}")

def enter(event, button): # function to be called when mouse enters in a frame
    button.config(bg=rgb_to_hex(settings.menu_button_highlight_color))
	# print('Button-2 pressed at x = % d, y = % d'%(event.x, event.y))

def exit_(event, button): # function to be called when mouse exits the frame
    button.config(bg=rgb_to_hex(settings.menu_button_color))
	# print('Button-3 pressed at x = % d, y = % d'%(event.x, event.y))  

def show_legal_moves(game_state,game_widgets, position_start):
    game_state.in_simulation = True
    for x in range(8):
        for y in range(8):
            temp_position_end = [x,y]
            if game_state.board[position_start[0]][position_start[1]].is_legal(bool(game_state.whites_turn),game_state, position_start, temp_position_end) == True:
                if settings.show_legal_moves == True:
                    game_widgets.board_of_buttons[x][y].config(image=game_state.board[x][y].show_legal_move_img)
    game_state.in_simulation = False
    
def exit_settings(r, s):
    root.overrideredirect(settings.display == 'full_screen')
    if settings.display == 'full_screen':
        root.state('zoomed')
    
    r.lift(s)
    game_widgets.reset_board_bg()
    
def open_settings(r, s, lyst_of_game_buttons, button_stop):
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

def update_board(board_state, game_widgets):
    resized_empty_square = 0
    for x in range(8):
        for y in range(8):
            game_widgets.board_of_buttons[x][y].config(image=board_state[x][y].rescale_img())
         
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

def move_piece(game_state, position_start, position_end):
    move_start = chr(position_start[1]+97) + str(8-position_start[0]) 
    move_end = chr(position_end[1]+97) + str(8-position_end[0])
    
    text = f"{game_state.board[position_start[0]][position_start[1]].annotated_name[1]}{move_start}{'x' if game_state.board[position_end[0]][position_end[1]].name != 'empty_square' else ''}{game_state.board[position_end[0]][position_end[1]].annotated_name[1]}{move_end}"
    text = f"{text:<8}"
    game_widgets.text_widget.config(state=NORMAL)
    game_widgets.text_widget.insert(tk.END, text)
    game_widgets.text_widget.insert(tk.END, '\n\n' if game_state.whites_turn == False else '  ')
    game_widgets.text_widget.config(state=DISABLED)
    
    #extra command if pawn is taking using ampasant
    
    if game_state.board[position_start[0]][position_start[1]].is_taking_by_ampasant[0] == True:
        game_state.board[position_start[0]][position_start[1]].is_taking_by_ampasant = (False, False) #resets value to avoid bug
        game_state.board[position_end[0]+game_state.board[position_start[0]][position_start[1]].is_taking_by_ampasant[1]][position_end[1]] = game_state.board[position_end[0]][position_end[1]]
        
    game_state.board[position_end[0]][position_end[1]] = game_state.board[position_start[0]][position_start[1]]
    game_state.board[position_start[0]][position_start[1]] = empty_square
    
    game_state.board[position_end[0]][position_end[1]].has_moved = True
         
def pressed(a, b, position_start, position_end, game_state):
    button = game_widgets.board_of_buttons[a][b]

    #resets the boards backgrounds to remove button click highlights
    game_widgets.reset_board_bg('soft wipe')

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

            show_legal_moves(game_state,game_widgets, position_start)
        
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

            game_widgets.reset_board_bg('wipe')

            #highlights the square a piece moved from and to
            game_widgets.board_of_buttons[position_end[0]][position_end[1]].config(bg = rgb_to_hex(settings.primary_move_color))

            if (abs(position_start[0]-position_end[0]) == 1 and abs(position_start[1]-position_end[1]) == 0
                or abs(position_start[0]-position_end[0]) == 0 and abs(position_start[1]-position_end[1]) == 1):
                game_widgets.board_of_buttons[position_start[0]][position_start[1]].config(bg = rgb_to_hex(settings.secondary_move_color))

            else:
                game_widgets.board_of_buttons[position_start[0]][position_start[1]].config(bg = rgb_to_hex(settings.primary_move_color))

            
            update_board(game_state.board, game_widgets)
            game_state.piece_was_moved()

        else:
            pass
            #doesnt move the piece
            
            
        for i in range(len(position_start)):
            position_start.pop(0)
        for j in range(len(position_end)):
            position_end.pop(0)
    
    else:
        # game_widgets.reset_board_bg()
        pass
        
    
    
    # print(f"row = {a}, col = {b}")

class GameWidgets():
    def __init__(self):
        

        #make the main frame (r) for the game
        self.home = tk.Frame(root, bg="blue")
        self.home.place(relwidth=1, relheight=1)  # Filling the entire window

        #initialize settings Frame
        self.s = settings.init_settings_frame(root, self.home, rgb_to_hex, exit_settings, pixel)

        #moves the settings frame behind the game frame
        self.home.lift(self.s)

        self.make_home_pages_main_frames()
        self.make_user_headers()
        self.make_chess_board()
        self.make_navigation_buttons()
        self.make_game_interface_buttons()
        self.make_move_history()
        self.make1_lyst_of_game_buttons()

    def make_home_pages_main_frames(self):
        #game is made of 3 main frames: left, right, and center
        self.left_frame = Frame(self.home, bg = rgb_to_hex(settings.left_side_bar_bg_color))
        self.left_frame.place(x=0, y=0, width=100, height=600)

        self.right_frame = Frame(self.home, bg = rgb_to_hex(settings.right_side_bar_bg_color))
        self.right_frame.place(x=500, y=0, width=100, height=600)

        self.center_frame = Frame(self.home)
        self.center_frame.place(x=100, y=0, width=400, height=600)

    def make_user_headers(self):
        #stuff inside center frame: opponents username, and users name
        self.center_frame.rowconfigure(0, weight=1)
        self.top_bar = Label(self.center_frame, text="Opponent",bg = rgb_to_hex(settings.top_top_bar_bg_color))
        self.top_bar.grid(column=0, row=0, columnspan=8, sticky=NSEW)

        self.center_frame.rowconfigure(9, weight=1)
        self.bottom_bar = Label(self.center_frame, text="You", bg = rgb_to_hex(settings.bottom_bottom_bar_bg_color))
        self.bottom_bar.grid(column=0, row=9, columnspan=8, sticky=NSEW)

    def make_chess_board(self):
        
        self.board_of_buttons = []


        for x in range(8):
            lyst = []
            for y in range(8):
                if x%2 == 0 and y%2 == 0 or x%2 != 0 and y%2 != 0:
                    bg_color = rgb_to_hex(settings.light_square_color)
                else:
                    bg_color = rgb_to_hex(settings.dark_square_color)
                button_on_board = tk.Button(self.center_frame,image = game_state.board[x][y].image, bg = bg_color, activebackground=bg_color, width = (400/8)-2, height = (400/8)-2, border=0)
                button_on_board.x, button_on_board.y = int(x), int(y)

                # important line for fixing he scaling of the chess board however implimentation requires changing a lot of code in other places
                # button_on_board.place(relx=y/8, rely=x/8, relwidth=1/8, relheight=1/8)

                if settings.whites_perspective == True:
                    button_on_board.grid(row=x+1,column=y)
                else:
                    button_on_board.grid(row=x+1,column=y)

                lyst.append(button_on_board)
            self.board_of_buttons.append(list(lyst))

        for x in range(8):
            for y in range(8):
                self.board_of_buttons[x][y].config(command= lambda x=x, y=y: pressed(x, y, position_start, position_end, game_state))

    def make_navigation_buttons(self):
        #stuff inside left side bar: exit game, setting, and ...
        self.button_stop = Button(self.left_frame, text='Exit',width=100-2,padx=0, pady=10, border=0, font=('Helvatical bold', 10), bg = rgb_to_hex(settings.menu_button_color), fg = 'black', image=pixel, compound="c", command= lambda: root.destroy) 
        self.button_stop.grid(row=0, column=0, sticky="nsew") 
        self.button_stop.bind('<Enter>', lambda event: enter(event, self.button_stop))             
        self.button_stop.bind('<Leave>', lambda event: exit_(event, self.button_stop))

        self.button_setting = Button(self.left_frame, text='Settings', width=100-2,padx=0, pady=10, border=0, font=('Helvatical bold', 10), bg = rgb_to_hex(settings.menu_button_color), fg = 'black', image=pixel, compound="c", command= lambda: open_settings(self.home, self.s, self.lyst_of_game_buttons, self.button_stop)) 
        self.button_setting.grid(row=1, column=0, sticky="nsew") 
        self.button_setting.bind('<Enter>', lambda event: enter(event, self.button_setting))             
        self.button_setting.bind('<Leave>', lambda event: exit_(event, self.button_setting))

        self.button_play_local = Button(self.left_frame, text='Play Local', width=100-2,padx=0, pady=10, border=0, font=('Helvatical bold', 10), bg = rgb_to_hex(settings.menu_button_color), fg = 'black', image=pixel, compound="c", command= lambda: time_control_picker(game_widgets.center_frame)) 
        self.button_play_local.grid(row=2, column=0, sticky="nsew") 
        self.button_play_local.bind('<Enter>', lambda event: enter(event, self.button_play_local))             
        self.button_play_local.bind('<Leave>', lambda event: exit_(event, self.button_play_local))

        self.button_play_bot = Button(self.left_frame, text='Play Computer', width=100-2,padx=0, pady=10, border=0, font=('Helvatical bold', 10), bg = rgb_to_hex(settings.menu_button_color), fg = 'black', image=pixel, compound="c", command= lambda: start_computer_game()) 
        self.button_play_bot.grid(row=3, column=0, sticky="nsew") 
        self.button_play_bot.bind('<Enter>', lambda event: enter(event, self.button_play_bot))             
        self.button_play_bot.bind('<Leave>', lambda event: exit_(event, self.button_play_bot))
        self.button_play_bot.config(state='disabled')

        self.button_play_online = Button(self.left_frame, text='Play Online', width=100-2,padx=0, pady=10, border=0, font=('Helvatical bold', 10), bg = rgb_to_hex(settings.menu_button_color), fg = 'black', image=pixel, compound="c")#, command= lambda: start_online_game()) 
        self.button_play_online.grid(row=4, column=0, sticky="nsew") 
        self.button_play_online.bind('<Enter>', lambda event: enter(event, self.button_play_online))             
        self.button_play_online.bind('<Leave>', lambda event: exit_(event, self.button_play_online))
        self.button_play_online.config(state='disabled')

    def make_game_interface_buttons(self):
        #stuff inside right side bar: move history, and ...
        self.reset_board_button = Button(self.right_frame, text='Reset Board', width=100-2,padx=0, pady=10, border=0, font=('Helvatical bold', 10), bg = rgb_to_hex(settings.menu_button_color), fg = 'black', image=pixel, compound="c", command= lambda: game_state.create_new_board(position_start, position_end))
        self.reset_board_button.pack(side=TOP, fill=X) 
        self.reset_board_button.bind('<Enter>', lambda event: enter(event, self.reset_board_button))             
        self.reset_board_button.bind('<Leave>', lambda event: exit_(event, self.reset_board_button))

        self.flip_board_button = Button(self.right_frame, text='Flip Board', width=100-2,padx=0, pady=10, border=0, font=('Helvatical bold', 10), bg = rgb_to_hex(settings.menu_button_color), fg = 'black', image=pixel, compound="c", command= lambda: game_widgets.flip_board(settings, self.board_of_buttons)) 
        self.flip_board_button.pack(side=TOP, fill=X) 
        self.flip_board_button.bind('<Enter>', lambda event: enter(event, self.flip_board_button))             
        self.flip_board_button.bind('<Leave>', lambda event: exit_(event, self.flip_board_button))

        self.resign_button = Button(self.right_frame, text='Resign', width=100-2,padx=0, pady=10, border=0, font=('Helvatical bold', 10), bg = rgb_to_hex(settings.menu_button_color), fg = 'black', state=DISABLED, image=pixel, compound="c", command= lambda: resign())
        self.resign_button.pack(side=BOTTOM, fill=X)
        self.resign_button.bind('<Enter>', lambda event: enter(event, self.resign_button))             
        self.resign_button.bind('<Leave>', lambda event: exit_(event, self.resign_button))

        self.draw_button = Button(self.right_frame, text='Draw', width=100-2,padx=0, pady=10, border=0, font=('Helvatical bold', 10), bg = rgb_to_hex(settings.menu_button_color), fg = 'black',state=DISABLED, image=pixel, compound="c", command= lambda: offer_draw())
        self.draw_button.pack(side=BOTTOM, fill=X)
        self.draw_button.bind('<Enter>', lambda event: enter(event, self.draw_button))             
        self.draw_button.bind('<Leave>', lambda event: exit_(event, self.draw_button))

    def make_move_history(self):
        self.move_history_frame = Frame(self.right_frame, bg=rgb_to_hex(settings.menu_button_highlight_color))
        self.move_history_frame.pack(pady=(10,0))

        self.move_history_text_frame = Frame(self.move_history_frame, bg='green')
        self.move_history_text_frame.grid(row=0, column=0, sticky="nsew")
        # Create a Text widget
        self.text_widget = tk.Text(self.move_history_text_frame,width=int(settings.size//2.1), height=settings.size//5, font=("Helvetica", 12), wrap="word", state=tk.DISABLED, bg=rgb_to_hex(settings.menu_button_highlight_color))
        self.text_widget.pack(side=LEFT, fill="both", expand=True)

        # Create a Scrollbar widget and attach it to the Text widget
        self.scrollbar = ttk.Scrollbar(self.move_history_text_frame, command=self.text_widget.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.text_widget.config(yscrollcommand=self.scrollbar.set)

        # create a forward and back button for move history
        self.move_history_button_frame = Frame(self.move_history_frame, bg='blue')
        self.move_history_button_frame.grid(row=1, column=0, sticky="nsew")

        self.move_back_history = Button(self.move_history_button_frame, text='Back', width=1, height=settings.size, border=1, relief=SOLID, font=('Helvatical bold', 10), bg=rgb_to_hex(settings.menu_button_highlight_color), fg='black', image=pixel, compound="c", command=lambda: game_state.show_previous_move())
        self.move_back_history.pack(side=LEFT, padx=0, pady=0, fill="both", expand=True)

        self.move_forward_history = Button(self.move_history_button_frame, text='Forward', width=1, height=settings.size, border=1, relief=SOLID, font=('Helvatical bold', 10), bg=rgb_to_hex(settings.menu_button_highlight_color), fg='black', image=pixel, compound="c", command=lambda: game_state.show_next_move())
        self.move_forward_history.pack(side=RIGHT, padx=0, pady=0, fill="both", expand=True)
 
        # Configure row and column weights to make both frames take equal space
        self.move_history_frame.grid_rowconfigure(0, weight=3)
        self.move_history_frame.grid_rowconfigure(1, weight=1)
        self.move_history_frame.grid_columnconfigure(0, weight=1)

    def make1_lyst_of_game_buttons(self):
        #usefull when i need to modify every single button
        self.lyst_of_game_buttons = [self.button_stop, self.button_setting, self.button_play_local, self.button_play_online, self.button_play_bot, self.reset_board_button, self.flip_board_button]
        for x in self.board_of_buttons:
            for y in x:
                self.lyst_of_game_buttons.append(y)

    def reset_board_bg(self, wipe=''):
        for x in range(8):
            # print('\n')
            for y in range(8):
                #clears all overlays
                self.board_of_buttons[x][y].config(image=game_state.board[x][y].image)

                #clears everything if wipe == 'wipe' 
                if wipe == 'wipe':
                    if x%2 == 0 and y%2 == 0 or x%2 != 0 and y%2 != 0:
                        self.board_of_buttons[x][y].config(bg = rgb_to_hex(settings.light_square_color))
                    else:
                        self.board_of_buttons[x][y].config(bg = rgb_to_hex(settings.dark_square_color))

                #doesnt clear yellow highlight from moving a piece if wipe != 'wipe 
                elif not (self.board_of_buttons[x][y]['bg'] == rgb_to_hex(settings.primary_move_color) or self.board_of_buttons[x][y]['bg'] == rgb_to_hex(settings.secondary_move_color)):
                    if x%2 == 0 and y%2 == 0 or x%2 != 0 and y%2 != 0:
                        self.board_of_buttons[x][y].config(bg = rgb_to_hex(settings.light_square_color))
                    else:
                        self.board_of_buttons[x][y].config(bg = rgb_to_hex(settings.dark_square_color))
                
    def flip_board(self, settings, board_of_buttons):
        settings.whites_perspective = not settings.whites_perspective
        if settings.whites_perspective == True:
            self.top_bar.grid(column=0, row=0, columnspan=8, sticky=NSEW)
            self.bottom_bar.grid(column=0, row=9, columnspan=8, sticky=NSEW)
        else:
            self.top_bar.grid(column=0, row=9, columnspan=8, sticky=NSEW)
            self.bottom_bar.grid(column=0, row=0, columnspan=8, sticky=NSEW)

        for x in range(8):
            for y in range(8):
                # print(board_of_buttons[x][y])
                if settings.whites_perspective == True:
                    board_of_buttons[x][y].grid(row=x+1, column=y)
                else:
                    board_of_buttons[x][y].grid(row=7-x+1, column=y)

    def clear_text_widget(self, text_widget):
        self.text_widget.config(state=NORMAL)
        self.text_widget.delete(1.0, tk.END)  # Clear from start (1.0) to end (tk.END)
        self.text_widget.config(state=DISABLED)

def destroy_root(root):
    if root.is_destroying == False:
        print("Done1")
        root.is_destroying = True
        print('Done2')
        time_control.stop_timers = True
        print('Done3')
        root.quit()
        print('done4')
        

#tracks vaiables and different game states
game_state = GameStateTracker()
game_state.create_new_board(position_start, position_end)

#used to make buttons with text resize according to pixels not text
pixel = PhotoImage(width=1, height=1)
 
#idk what to say
game_widgets = GameWidgets()

#tracks the screen size
tracker = WindowTracker(root)
tracker.bind_config(game_state, game_widgets)

#track the time control for any game
time_control = TimeControlTracker()

# start_game_timers = threading.Thread(target=time_control.start_game_timers, args=(game_widgets,))

root.mainloop() 