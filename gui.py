import tkinter as tk
from gui_settings import *
from game import GameState

class GUI():
    def start(gs = None):   # main function for the GUI
        """Main function to initialize and run the Tkinter GUI"""
        GUI.root = tk.Tk() 
        GUI.root.title('Chess') 
        GUI.root.geometry('900x600-0+0')    # "-0+0" puts window in top right corner
        GUI.root.is_destroying = False

        # GUI's refrence to the current game
        # if game state needs changed then update the refrence and store the old game elsewhere                                                       
        GUI.gameState = gs if gs else GameState() # Initialize game state if none provided

        GUI.theme = DefaultTheme()
        GUI.fonts = defaultFonts()

        GUI.root_frames = {}
        GUI.main_frames = {}
        GUI.setting_frames = {}

        # List to contain a refrence to every single widget
        GUI.widgets = [GUI.root_frames, GUI.main_frames, GUI.setting_frames]

        setting_f, set_cont_f, right_f, left_f, opp_f, GUI.game_f, player_f = GUI.create_frame_layout(GUI.root)
        
        GUI.create_setting_header_content(setting_f)
        GUI.create_setting_content(set_cont_f)

        # game_content must be called before left_content and right_content
        GUI.create_game_content(GUI.game_f)
        GUI.create_left_content(left_f)
        GUI.create_right_content(right_f)
        GUI.create_opponent_content(opp_f)
        GUI.create_player_content(player_f)

        # Defer the binding until the root and widgets are fully initialized
        GUI.root.after(0, lambda: GUI.root.bind("<Configure>", lambda event: UpdateBoard.resize_handler(event)))
        GUI.root.after(0, lambda: UpdateBoard.resize_handler(None))
        
        GUI.root.mainloop()

    def create_setting_header_content(frame):
        pass

    def create_setting_content(frame):
        pass

    def create_left_content(frame):
        left_widgets = []

        button_stop = tk.Button(frame, text='Exit', command= lambda: GUIController.destroy_root(GUI.root), border=0, font=GUI.fonts.default_font, bg = GUI.theme.button_color, fg=GUI.theme.text_color, pady=10) 
        left_widgets.append(button_stop)
        
        button_setting = tk.Button(frame, text='Settings', border=0, font=GUI.fonts.default_font, bg=GUI.theme.button_color, fg=GUI.theme.text_color, pady=10) 
        left_widgets.append(button_setting)
        
        button_play_local = tk.Button(frame, text='Play Local', command= lambda: GUIController.destroy_root(GUI.root), border=0, font=GUI.fonts.default_font, bg=GUI.theme.button_color, fg=GUI.theme.text_color, pady=10) 
        left_widgets.append(button_play_local)

        button_play_online = tk.Button(frame, text='Play Online', border=0, font=GUI.fonts.default_font, bg=GUI.theme.button_color, fg=GUI.theme.text_color, pady=10) 
        left_widgets.append(button_play_online)
        button_play_online.config(state='disabled')

        # Packing widgets to the left frame and binding hover events
        for widget in left_widgets:
            widget.pack(side='top', fill="x")
            widget.bind('<Enter>', lambda event, widget=widget: GUIController.on_hover(event, widget))
            widget.bind('<Leave>', lambda event, widget=widget: GUIController.on_leave(event, widget))
            
    def create_right_content(frame):
        right_widgets = []

        reset_button = tk.Button(frame, text='Reset', command=lambda : GUIController.reset_game(), border=0, font=GUI.fonts.default_font, bg=GUI.theme.button_color, fg=GUI.theme.text_color, pady=10)
        right_widgets.append(reset_button)

        flip_button = tk.Button(frame, text='Flip', command=lambda: GUIController.toggle_perspective(), border=0, font=GUI.fonts.default_font, bg=GUI.theme.button_color, fg=GUI.theme.text_color, pady=10)
        right_widgets.append(flip_button)

        # Packing widgets to the right frame and binding hover events
        for widget in right_widgets:
            widget.pack(side='top', fill="x")
            widget.bind('<Enter>', lambda event, widget=widget: GUIController.on_hover(event, widget))
            widget.bind('<Leave>', lambda event, widget=widget: GUIController.on_leave(event, widget))

    def create_opponent_content(frame):
        tk.Label(frame, text="Opponent", font=GUI.fonts.default_font, bg=GUI.theme.opp_header, fg=GUI.theme.text_color).pack(fill='both', expand=True)

    def create_game_content(frame):
        GUI.chess_buttons = []

        # Create the 8x8 chessboard buttons
        for x in range(8):
            row = []
            for y in range(8):
                button = tk.Button(frame, image=GUI.gameState.display_board.board[x][y].image, border=0, bg=GUI.theme.light_square if (x + y) % 2 == 0 else GUI.theme.dark_square)
                button.pos = f"{chr(97+x)}{8-y}"
                button.config(command=lambda pos=button.pos, y=y, x=x: GUIController.square_click(pos, y, x))
                row.append(button)
            GUI.chess_buttons.append(row)

        # Bind the resize event to dynamically adjust button sizes
        frame.bind("<Configure>", lambda event: UpdateBoard.resize_board(event, frame))

        # Trigger the initial resize to set up the buttons
        frame.update_idletasks()
        UpdateBoard.resize_board(None, frame)
            
    def create_player_content(frame):
        tk.Label(frame, text="You", font=GUI.fonts.default_font, bg=GUI.theme.player_header, fg=GUI.theme.text_color).pack(fill='both', expand=True)

    def create_frame_layout(frame):
        """Creates the main layout frames"""

        # SETTING FRAMES #
        GUI.setting_frame = tk.Frame(frame)
        GUI.setting_frame.place(relx=0,rely=0,relwidth=1, relheight=1)

        setting_header = tk.Frame(GUI.setting_frame, bg=GUI.theme.setting_header)
        setting_header.place(relx=0,rely=0,relwidth=1, relheight=.03)

        settings_content_frame = tk.Frame(GUI.setting_frame, bg=GUI.theme.settings_content_frame)
        settings_content_frame.place(relx=0,rely=.03,relwidth=1, relheight=.97)

        # MAIN FRAMES #
        GUI.main_frame = tk.Frame(frame)
        GUI.main_frame.place(relx=0,rely=0,relwidth=1, relheight=1)

        left_header = tk.Frame(GUI.main_frame, bg=GUI.theme.left_header)
        left_header.place(relx=0,rely=0,relwidth=.15, relheight=1)

        right_header = tk.Frame(GUI.main_frame, bg=GUI.theme.right_header)
        right_header.place(relx=.85,rely=0,relwidth=.15, relheight=1)

        opp_header = tk.Frame(GUI.main_frame, bg=GUI.theme.opp_header)
        opp_header.place(relx=.15,rely=0,relwidth=.7, relheight=.1)

        game_header = tk.Frame(GUI.main_frame, bg=GUI.theme.game_header)
        game_header.place(relx=.15,rely=.1,relwidth=.7, relheight=.8)

        player_header = tk.Frame(GUI.main_frame, bg=GUI.theme.player_header)
        player_header.place(relx=.15,rely=.9,relwidth=.7, relheight=.1)

        return setting_header, settings_content_frame, right_header, left_header, opp_header, game_header, player_header
    
    def create_setting_layout(frame):
        pass

class GUIController():
    pos_start = None
    pos_end = None

    def on_hover(event, button):
        button.config(bg=GUI.theme.button_highlight_color)

    def on_leave(event, button):
        button.config(bg=GUI.theme.button_color)

    def destroy_root(root):
        if root.is_destroying == False:
            root.is_destroying = True
            
            # stop time_control thread here!
            # stop any other threads here!

            print("Exiting program...")
            root.quit()

    def reset_game():
        GUI.gameState.reset_game()
        UpdateBoard.update_board()

    def toggle_perspective():
        gameSettings.perspective = not gameSettings.perspective
        UpdateBoard.resize_board(None, GUI.game_f)
        
    def square_click(pos, y, x):
        # print(pos)
        if not GUIController.pos_start:
            GUIController.pos_start = pos
            GUI.chess_buttons[x][y].config(bg=GUI.theme.button_highlight_color)
        else:
            GUIController.pos_end = pos
            move = GUIController.pos_start + GUIController.pos_end
            # print(type(GUI.gameState.get_legal_moves()))
            if GUI.gameState.is_legal_move(move):
                GUI.chess_buttons[x][y].config(bg=GUI.theme.button_color)
                GUI.gameState.move(move)  # Call the move function with the selected move
                UpdateBoard.update_board()
            else:
                UpdateBoard.update_board()
                GUIController.pos_start = pos
                GUIController.pos_end = None
                GUI.chess_buttons[x][y].config(bg=GUI.theme.button_highlight_color)
            


class UpdateBoard():
    img_size = 61 # default size of the image based on the default window size
    resize_timer = None
    def update_board(): # updates everything
        UpdateBoard.rescale_img()
        UpdateBoard.square_color()
        # print(GUI.gameState.display_board)

    def square_color():
        for x, row in enumerate(GUI.chess_buttons):
            for y, square in enumerate(row):
                if x%2 == 0 and y%2 == 0 or x%2 != 0 and y%2 != 0:
                    square.config(bg=GUI.theme.light_square)
                else:
                    square.config(bg=GUI.theme.dark_square)

    def resize_board(event, frame):
            # Get the current width and height of the frame
            frame_width = frame.winfo_width()
            frame_height = frame.winfo_height()

            # Calculate the size of each square (button)
            square_size = min(frame_width, frame_height) // 8

            offset_x = (frame_width - square_size * 8) / 2
            offset_y = (frame_height - square_size * 8) / 2

            # Update the position and size of each button
            for x in range(8):
                for y in range(8):
                    button = GUI.chess_buttons[x][y if gameSettings.perspective == 1 else 7 - y]
                    button.place(
                        x=x * square_size + offset_x,
                        y=y * square_size + offset_y,
                        width=square_size,
                        height=square_size
                    )

    def resize_handler(event):
        if event == None or event.widget == GUI.root:
            # Cancel any previously scheduled resize handling
            if UpdateBoard.resize_timer is not None:
                GUI.root.after_cancel(UpdateBoard.resize_timer)

            # Schedule the resize handling to occur after 100ms
            UpdateBoard.resize_timer = GUI.root.after(20, lambda: UpdateBoard.rescale_img(event))

    def rescale_img(event=None):
        size = min(GUI.game_f.winfo_width(), GUI.game_f.winfo_height()) // 8
        if(size != UpdateBoard.img_size) or event == None:
            if size > 0:
                UpdateBoard.img_size = size
            for y in range(8):
                for x in range(8):
                    GUI.gameState.display_board.board[x][y].rescale_img(UpdateBoard.img_size)
                    GUI.chess_buttons[y][x].config(image=GUI.gameState.display_board.board[x][y].image)
