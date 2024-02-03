#add users so the settings can be save to users
#maybe add passwords and encryption
#maybe add verification when person enters email,phone number, or disord


from chess_color_picker import *
from chess_themes import *




class Settings():
    def __init__(self, theme):
        self.size = 40 
        self.auto_queen = True #change default to False later
        self.lyst_of_auto_queen_buttons = []

        self.display = 'window'
        self.lyst_of_display_buttons = []

        self.show_legal_moves = True
        self.lyst_of_legal_moves_buttons = []

        self.lyst_of_custom_color = []
        self.lyst_of_themes = []

        self.theme = theme
        self.change_theme(theme)

    #state = 'normal', 'iconic', 'withdrawn', or 'zoomed'
   

    def init_settings_frame(self, root, r, from_rgb, exit_settings, pixel):        
        s = Frame(root, bg = 'black')
        s.place(relwidth=1, relheight=1)
    

        # s.protocol("WM_DELETE_WINDOW", lambda: exit_settings(r,s))

        bg_color = [169,169,169]


        top_frame = Label(s, bg = from_rgb((100,200,100)),bd = 10)
        top_frame.pack(side=TOP, fill=X)

        exit_button = Button(top_frame, text='Save and Exit', width=7, height=3,font=('Helvatical bold',20), bg = 'teal', fg = 'black', command= lambda: exit_settings(r,s)) 
        exit_button.pack(fill=X) 

        # Create a main frame
        over_arching_main_frame = Frame(s)
        over_arching_main_frame.pack(fill=BOTH, expand=1)

        # Create a canvas
        my_canvas = Canvas(over_arching_main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        #Add a scrollbar to the canvas
        my_scrollbar = ttk.Scrollbar(over_arching_main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        #configure the canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

        # create another frame inside the canvas
        main_frame = Frame(my_canvas)
        main_frame.pack(fill=BOTH, expand=1)

        # add that new frame to a window in the canvas
        # print(settings_window.width, settings_window.height)

        my_canvas.create_window((0, 0), window=main_frame, anchor="nw", tags="main_frame_tag")
        # my_canvas.itemconfig("main_frame_tag", width=1, height=1)


        settings_window = SettingsWindowTracker(s, my_canvas, main_frame)
        
        
        

        setting_frame1 = Frame(main_frame, bg = from_rgb(bg_color),bd = 10)
        setting_frame1.pack(side=TOP, fill=X)
        setting_lbl = Label(setting_frame1, text = f"{'Auto Queen'}: ", width=int(15), height=int(2),font=('Helvatical bold',int(25)), bg = from_rgb(bg_color),fg = 'black', pady = 10)
        setting_lbl.pack(side=LEFT)
        auto_queen_b1 = tk.Button(setting_frame1, text = 'On', width=int(9), height=int(.5),font=('Helvatical bold', 25, 'bold' if self.auto_queen == True else 'normal'), bg = 'teal', fg = 'black', pady = 10)
        auto_queen_b1.config(command=lambda: self.change_auto_queen(True, auto_queen_b1))
        auto_queen_b1.pack(side=RIGHT, padx=(5,20))
        self.lyst_of_auto_queen_buttons.append(auto_queen_b1)
        auto_queen_b2 = tk.Button(setting_frame1, text = 'Off', width=int(9), height=int(.5),font=('Helvatical bold', 25, 'bold' if self.auto_queen == False else 'normal'), bg = 'teal', fg = 'black', pady = 10)
        auto_queen_b2.config(command=lambda: self.change_auto_queen(False, auto_queen_b2))
        auto_queen_b2.pack(side=RIGHT, padx=5)
        self.lyst_of_auto_queen_buttons.append(auto_queen_b2)
        bg_color[0], bg_color[1], bg_color[2] = self.change_color(bg_color)


        setting_frame13 = Frame(main_frame, bg = from_rgb(bg_color),bd = 10)
        setting_frame13.pack(side=TOP, fill=X)
        setting_lbl = Label(setting_frame13, text = f"{'Show Legal Moves'}: ", width=int(15), height=int(2),font=('Helvatical bold',int(25)), bg = from_rgb(bg_color),fg = 'black', pady = 10)
        setting_lbl.pack(side=LEFT)
        show_moves_b1 = tk.Button(setting_frame13, text = 'On', width=int(9), height=int(.5),font=('Helvatical bold',25, 'bold' if self.show_legal_moves == True else 'normal'), bg = 'teal', fg = 'black', pady = 10)
        show_moves_b1.config(command=lambda: self.change_show_moves(True, show_moves_b1))
        show_moves_b1.pack(side=RIGHT, padx=(5,20))
        self.lyst_of_legal_moves_buttons.append(show_moves_b1)
        show_moves_b2 = tk.Button(setting_frame13, text = 'Off', width=int(9), height=int(.5),font=('Helvatical bold',25, 'bold' if self.show_legal_moves == False else 'normal'), bg = 'teal', fg = 'black', pady = 10)
        show_moves_b2.config(command=lambda: self.change_show_moves(False, show_moves_b2))
        show_moves_b2.pack(side=RIGHT, padx=5)
        self.lyst_of_legal_moves_buttons.append(show_moves_b2)
        bg_color[0], bg_color[1], bg_color[2] = self.change_color(bg_color)


        setting_frame12 = Frame(main_frame, bg = from_rgb(self.setting_header),bd = 10)
        setting_frame12.pack(side=TOP, fill=X)
        setting_lbl = Label(setting_frame12, text = f"Display", width=int(15), height=int(2),font=('Helvatical bold',int(25)), bg = from_rgb(self.setting_header),fg = 'black', pady = 10)
        setting_lbl.pack()


        setting_frame2 = Frame(main_frame, bg = from_rgb(bg_color),bd = 10)
        setting_frame2.pack(side=TOP, fill=X)
        setting_lbl = Label(setting_frame2, text = f"{'Display type'}: ", width=int(15), height=int(2),font=('Helvatical bold',int(25)), bg = from_rgb(bg_color),fg = 'black', pady = 10)#, image=pixeling, compound="c")
        setting_lbl.pack(side=LEFT)
        bg_color[0], bg_color[1], bg_color[2] = self.change_color(bg_color)
        windowed_b1 = tk.Button(setting_frame2, text = 'Window', width=int(9), height=int(.5),font=('Helvatical bold',25, 'bold' if self.display == 'window' else 'normal'), bg = 'teal', fg = 'black', pady = 10)
        windowed_b1.config(command=lambda: self.change_display('window', windowed_b1))
        windowed_b1.pack(side=RIGHT, padx=(5,20))
        self.lyst_of_display_buttons.append(windowed_b1)
        windowed_b2 = tk.Button(setting_frame2, text = 'Full Screen', width=int(9), height=int(.5),font=('Helvatical bold',25, 'bold' if self.display == 'full_screen' else 'normal'), bg = 'teal', fg = 'black', pady = 10)
        windowed_b2.config(command=lambda: self.change_display('full_screen', windowed_b2))
        windowed_b2.pack(side=RIGHT, padx=5)
        self.lyst_of_display_buttons.append(windowed_b2)


        setting_frame3 = Frame(main_frame, bg = from_rgb(self.setting_header),bd = 10)
        setting_frame3.pack(side=TOP, fill=X)
        setting_lbl = Label(setting_frame3, text = f"Themes", width=int(15), height=int(2),font=('Helvatical bold',int(25)), bg = from_rgb(self.setting_header),fg = 'black', pady = 10)
        setting_lbl.pack()
        


        setting_frame10 = Frame(main_frame, bg = from_rgb(bg_color),bd = 10)
        setting_frame10.pack(side=TOP, fill=X)
        chess_com_lbl = Label(setting_frame10, text = f"Chess.com", width=int(15), height=int(2),font=('Helvatical bold',int(25)), bg = from_rgb(bg_color),fg = 'black', pady = 10)
        chess_com_lbl.pack(side=LEFT)
        chess_com_b1 = tk.Button(setting_frame10, text = 'Chess.com Theme', width=int(19), height=int(.5),font=('Helvatical bold',25, 'bold' if self.theme.name == 'chess_dot_com' else 'normal'), bg = 'teal', fg = 'black', pady = 10)
        chess_com_b1.config(command= lambda: self.change_theme(ChessDotCom, chess_com_b1))
        chess_com_b1.pack(side=RIGHT, padx=(5,20))
        self.lyst_of_themes.append(chess_com_b1)
        bg_color[0], bg_color[1], bg_color[2] = self.change_color(bg_color)


        setting_frame11 = Frame(main_frame, bg = from_rgb(bg_color),bd = 10)
        setting_frame11.pack(side=TOP, fill=X)
        grey_scale_lbl = Label(setting_frame11, text = f"Grey Scale", width=int(15), height=int(2),font=('Helvatical bold',25, 'bold' if self.theme.name == 'grey_scale' else 'normal'), bg = from_rgb(bg_color),fg = 'black', pady = 10)
        grey_scale_lbl.pack(side=LEFT)
        grey_scale_b1 = tk.Button(setting_frame11, text = 'Grey Scale Theme', width=int(19), height=int(.5),font=('Helvatical bold',int(25)), bg = 'teal', fg = 'black', pady = 10)
        grey_scale_b1.config(command= lambda: self.change_theme(GreyScale, grey_scale_b1))
        grey_scale_b1.pack(side=RIGHT, padx=(5,20))
        self.lyst_of_themes.append(grey_scale_b1)
        bg_color[0], bg_color[1], bg_color[2] = self.change_color(bg_color)


        setting_frame12 = Frame(main_frame, bg = from_rgb(bg_color),bd = 10)
        setting_frame12.pack(side=TOP, fill=X)
        blissful_blues_lbl = Label(setting_frame12, text = f"Blissful Blues", width=int(15), height=int(2),font=('Helvatical bold',25, 'bold' if self.theme.name == 'blissful_blues' else 'normal'), bg = from_rgb(bg_color),fg = 'black', pady = 10)
        blissful_blues_lbl.pack(side=LEFT)
        blissful_blues_b1 = tk.Button(setting_frame12, text = 'Blissful Blues Theme', width=int(19), height=int(.5),font=('Helvatical bold',int(25)), bg = 'teal', fg = 'black', pady = 10)
        blissful_blues_b1.config(command= lambda: self.change_theme(BlissfulBlues, blissful_blues_b1))
        blissful_blues_b1.pack(side=RIGHT, padx=(5,20))
        self.lyst_of_themes.append(blissful_blues_b1)
        bg_color[0], bg_color[1], bg_color[2] = self.change_color(bg_color)


        setting_frame9 = Frame(main_frame, bg = from_rgb(self.setting_header),bd = 10)
        setting_frame9.pack(side=TOP, fill=X)
        setting_lbl = Label(setting_frame9, text = f"Custom Theme", width=int(15), height=int(2),font=('Helvatical bold',int(25)), bg = from_rgb(self.setting_header),fg = 'black', pady = 10)
        setting_lbl.pack()


        setting_frame4 = Frame(main_frame, bg = from_rgb(bg_color),bd = 10)
        setting_frame4.pack(side=TOP, fill=X)
        setting_lbl = Label(setting_frame4, text = f"Light Square", width=int(15), height=int(2),font=('Helvatical bold',int(25)), bg = from_rgb(bg_color),fg = 'black', pady = 10)
        setting_lbl.pack(side=LEFT)
        bg_color[0], bg_color[1], bg_color[2] = self.change_color(bg_color)
        create_color_picker_frame(setting_frame4, self, 'light_square_color')


        setting_frame5 = Frame(main_frame, bg = from_rgb(bg_color),bd = 10)
        setting_frame5.pack(side=TOP, fill=X)
        setting_lbl = Label(setting_frame5, text = f"Dark Square", width=int(15), height=int(2),font=('Helvatical bold',int(25)), bg = from_rgb(bg_color),fg = 'black', pady = 10)
        setting_lbl.pack(side=LEFT)
        bg_color[0], bg_color[1], bg_color[2] = self.change_color(bg_color)
        create_color_picker_frame(setting_frame5, self, 'dark_square_color')


        setting_frame6 = Frame(main_frame, bg = from_rgb(bg_color),bd = 10)
        setting_frame6.pack(side=TOP, fill=X)
        setting_lbl = Label(setting_frame6, text = f"Highlight Square", width=int(15), height=int(2),font=('Helvatical bold',int(25)), bg = from_rgb(bg_color),fg = 'black', pady = 10)
        setting_lbl.pack(side=LEFT)
        bg_color[0], bg_color[1], bg_color[2] = self.change_color(bg_color)
        create_color_picker_frame(setting_frame6, self, 'highlight_square_color')



        setting_frame7 = Frame(main_frame, bg = from_rgb(bg_color),bd = 10)
        setting_frame7.pack(side=TOP, fill=X)
        setting_lbl = Label(setting_frame7, text = f"Primary Move", width=int(15), height=int(2),font=('Helvatical bold',int(25)), bg = from_rgb(bg_color),fg = 'black', pady = 10)
        setting_lbl.pack(side=LEFT)
        bg_color[0], bg_color[1], bg_color[2] = self.change_color(bg_color)
        create_color_picker_frame(setting_frame7, self, 'primary_move_color')



        setting_frame8 = Frame(main_frame, bg = from_rgb(bg_color),bd = 10)
        setting_frame8.pack(side=TOP, fill=X)
        setting_lbl = Label(setting_frame8, text = f"Secondary Move", width=int(15), height=int(2),font=('Helvatical bold',int(25)), bg = from_rgb(bg_color),fg = 'black', pady = 10)
        setting_lbl.pack(side=LEFT)
        bg_color[0], bg_color[1], bg_color[2] = self.change_color(bg_color)
        create_color_picker_frame(setting_frame8, self, 'secondary_move_color')




        # dark_square color
        # light_square color
        # highlight_square color
        # primary_move color
        # secondary_move color

        return s


    def change_color(self, color):
        if color == [120,120,120]:
            color = [169,169,169]
        elif color == [169,169,169]:
            color = [120,120,120]
        return color[0], color[1], color[2]

    def change_auto_queen(self, on_off, button=''):
        self.auto_queen = on_off
        if button != '':
            for b in self.lyst_of_auto_queen_buttons:
                if button == b:
                    b.config(font=('Helvatical bold',25, 'bold'))
                else:
                    b.config(font=('Helvatical bold',25, 'normal'))

    def change_show_moves(self, on_off, button=''):
        self.show_legal_moves = on_off
        if button != '':
            for b in self.lyst_of_legal_moves_buttons:
                if button == b:
                    b.config(font=('Helvatical bold',25, 'bold'))
                else:
                    b.config(font=('Helvatical bold',25, 'normal'))

    def change_display(self, display_type, button=''):
        self.display = display_type
        if button != '':
            for b in self.lyst_of_display_buttons:
                if button == b:
                    b.config(font=('Helvatical bold',25, 'bold'))
                else:
                    b.config(font=('Helvatical bold',25, 'normal'))

    def change_theme(self, theme, button=''):
        #board interaction colors
        self.dark_square_color = theme.dark_square_color
        self.light_square_color = theme.light_square_color
        self.highlight_square_color = theme.highlight_square_color
        self.primary_move_color = theme.primary_move_color
        self.secondary_move_color = theme.secondary_move_color

        #menu button colors
        self.menu_button_color = theme.menu_button_color
        self.menu_button_highlight_color = theme.menu_button_highlight_color
        #maybe add a activebackground color for these menu buttons
        #activebackground is the color of the button when you click and hold
    

        #back ground colors
        self.left_side_bar_bg_color = theme.left_side_bar_bg_color
        self.right_side_bar_bg_color = theme.right_side_bar_bg_color
        self.top_top_bar_bg_color = theme.top_top_bar_bg_color
        self.bottom_bottom_bar_bg_color = theme.bottom_bottom_bar_bg_color
        
        #settings Colors
        self.setting_header = (100,150,255)

        if button != '':
            for b in self.lyst_of_themes:
                if button == b:
                    b.config(font=('Helvatical bold',25, 'bold'))
                else:
                    b.config(font=('Helvatical bold',25, 'normal'))


class SettingsWindowTracker():
    """ windows resize event tracker """

    def __init__(self, root, my_canvas, main_frame):
        self.root = root
        self.width, self.height = root.winfo_width(), root.winfo_height()        
        self._func_id = self.root.bind("<Configure>", lambda event: self.resize(event, my_canvas, main_frame))



    def resize(self, event, my_canvas, main_frame):
        if(event.widget == self.root and
        (self.width != event.width or self.height != event.height)):
            self.width, self.height = event.width, event.height
            # print(f'{self.height}, {self.width}')

            #calculate what the height should be depending on how many widgets i put in
            my_canvas.itemconfig("main_frame_tag", width=self.width, height=main_frame.winfo_reqheight())
            
