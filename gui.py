import tkinter as tk
from gui_settings import *
from game import GameState

class GUI():
    def start(gameState = None):   # main function for the GUI
        """Main function to initialize and run the Tkinter GUI"""
        GUI.root = tk.Tk() 
        GUI.root.title('UVSim') 
        GUI.root.geometry('900x600-0+0')    # "-0+0" puts window in top right corner
        GUI.root.is_destroying = False

        if gameState is None:
            gameState = GameState()

        GUI.theme = DefaultTheme()
        GUI.fonts = defaultFonts()

        GUI.root_frames = {}
        GUI.main_frames = {}
        GUI.setting_frames = {}

        # List to contain a refrence to every single widget
        GUI.widgets = [GUI.root_frames, GUI.main_frames, GUI.setting_frames]

        setting_f, set_cont_f, right_f, left_f, opp_f, game_f, player_f = GUI.create_frame_layout(GUI.root)
        
        GUI.create_setting_header_content(setting_f)
        GUI.create_setting_content(set_cont_f)

        # game_content must be called before left_content and right_content
        GUI.create_game_content(game_f, gameState)
        GUI.create_left_content(left_f)
        GUI.create_right_content(right_f, gameState)
        GUI.create_opponent_content(opp_f)
        GUI.create_player_content(player_f)
        
        GUI.root.mainloop()

    def create_setting_header_content(frame):
        pass

    def create_setting_content(frame):
        pass

    def create_left_content(frame):
        left_widgets = []

        button_stop = tk.Button(frame, text='Exit', command= lambda: GUI_action.destroy_root(GUI.root), border=0, font=GUI.fonts.default_font, bg = GUI.theme.button_color, fg=GUI.theme.text_color, pady=10) 
        left_widgets.append(button_stop)
        
        button_setting = tk.Button(frame, text='Settings', border=0, font=GUI.fonts.default_font, bg=GUI.theme.button_color, fg=GUI.theme.text_color, pady=10) 
        left_widgets.append(button_setting)
        
        button_play_local = tk.Button(frame, text='Play Local', border=0, font=GUI.fonts.default_font, bg=GUI.theme.button_color, fg=GUI.theme.text_color, pady=10) 
        left_widgets.append(button_play_local)

        button_play_bot = tk.Button(frame, text='Play Computer', border=0, font=GUI.fonts.default_font, bg=GUI.theme.button_color, fg=GUI.theme.text_color, pady=10) 
        left_widgets.append(button_play_bot)
        button_play_bot.config(state='disabled')

        button_play_online = tk.Button(frame, text='Play Online', border=0, font=GUI.fonts.default_font, bg=GUI.theme.button_color, fg=GUI.theme.text_color, pady=10) 
        left_widgets.append(button_play_online)
        button_play_online.config(state='disabled')

        # Packing widgets to the left frame and binding hover events
        for widget in left_widgets:
            widget.pack(side='top', fill="x")
            widget.bind('<Enter>', lambda event, widget=widget: GUI_action.on_hover(event, widget))
            widget.bind('<Leave>', lambda event, widget=widget: GUI_action.on_leave(event, widget))
            
    def create_right_content(frame, gameState):
        right_widgets = []

        reset_button = tk.Button(frame, text='Reset', command=lambda : GUI_action.reset_game(gameState), border=0, font=GUI.fonts.default_font, bg=GUI.theme.button_color, fg=GUI.theme.text_color, pady=10)
        right_widgets.append(reset_button)

        flip_button = tk.Button(frame, text='Flip', command=lambda: UpdateBoard.toggle_perspective(), border=0, font=GUI.fonts.default_font, bg=GUI.theme.button_color, fg=GUI.theme.text_color, pady=10)
        right_widgets.append(flip_button)

        # Packing widgets to the right frame and binding hover events
        for widget in right_widgets:
            widget.pack(side='top', fill="x")
            widget.bind('<Enter>', lambda event, widget=widget: GUI_action.on_hover(event, widget))
            widget.bind('<Leave>', lambda event, widget=widget: GUI_action.on_leave(event, widget))

    def create_opponent_content(frame):
        tk.Label(frame, text="Opponent", font=GUI.fonts.default_font, bg=GUI.theme.opp_header, fg=GUI.theme.text_color).pack(fill='both', expand=True)

    def create_game_content(frame, gameState):
        GUI.chess_buttons = []
        for x in range(8): # 8x8 chess board
            row = []
            for y in range(8):
                button = tk.Button(frame, border=0)#image=gameState.img(gameState.piece(x,y)), border=0) 
                # TODO add image
                # TODO fix button sizes to be square
                button.place(relx=x/8, rely=y/8, relwidth=1/8, relheight=1/8)
                row.append(button)
            GUI.chess_buttons.append(row)
        UpdateBoard.update_board()
            
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

class GUI_action():
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

    def reset_game(gameState):
        gameState.reset_game()
        UpdateBoard.update_board()

class UpdateBoard(GameState):
    def update_board(): # updates everything
        UpdateBoard.board_size()
        UpdateBoard.square_color()

    def toggle_perspective():
        gameSettings.perspective = not gameSettings.perspective
        for x in range(8):
            for y in range(8):
                if gameSettings.perspective:
                    GUI.chess_buttons[x][y].place(relx=x/8, rely=y/8, relwidth=1/8, relheight=1/8)
                else:
                    GUI.chess_buttons[x][y].place(relx=x/8, rely=(7-y)/8, relwidth=1/8, relheight=1/8)

    def board_size():
        pass

    def square_color():
        for x, row in enumerate(GUI.chess_buttons):
            for y, square in enumerate(row):
                if x%2 == 0 and y%2 == 0 or x%2 != 0 and y%2 != 0:
                    square.config(bg=GUI.theme.light_square)
                else:
                    square.config(bg=GUI.theme.dark_square)

def main():
    GUI.start()

if __name__ == "__main__":
    main()