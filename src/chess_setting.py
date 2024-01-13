#change this to be a text file so it remembers you settings
#add users so the settings can be save to users
#maybe add passwords and look into encryption
#add verification when person enters email,phone number, or disord


from tkinter import *
from tkinter import ttk
import tkinter as tk                                                      
from PIL import Image, ImageTk, ImageDraw




class Settings():
    def __init__(self):
        self.size = 40
        self.auto_queen = True #change default to False later
        self.display = 'window'


        

        #board interaction colors
        self.dark_square_color = (119, 153, 84)
        self.light_square_color = (233, 237, 204)
        self.highlight_square_color = (188, 188, 160)
        self.primary_move_color = (244, 246, 128)
        self.secondary_move_color = (187, 204, 68)

        #menu button colors
        self.menu_button_color = (128, 128, 128)
        self.menu_button_highlight_color = (128, 100, 100)
        #maybe add a activebackground color for these menu buttons
        #activebackground is the color of the button when you click and hold
    

        #back ground colors
        self.left_side_bar_bg_color = (128, 128, 128)
        self.right_side_bar_bg_color = (128, 128, 128)
        self.top_top_bar_bg_color = (64, 64 ,64)
        self.bottom_bottom_bar_bg_color = (64, 64 ,64)

    #state = 'normal', 'iconic', 'withdrawn', or 'zoomed'

    

    def change_color(self, color):
        if color == [120,120,120]:
            color = [169,169,169]
        elif color == [169,169,169]:
            color = [120,120,120]
        return color[0], color[1], color[2]
   

    def open_settings_window(self, r, from_rgb, exit_settings, pixel):
        global pixeling
        pixeling = PhotoImage(width=1,height=1)
        # r.state('iconic')
        
        s = tk.Tk() 
        s.title('Settings')
        if self.display == 'full_screen':
            s.geometry(f'{r.winfo_width()}x{r.winfo_height()}+{int(r.winfo_rootx())-8}+{int(r.winfo_rooty())}')
        else:
            s.geometry(f'{r.winfo_width()}x{r.winfo_height()}+{int(r.winfo_rootx())-8}+{int(r.winfo_rooty())-30}')

        # print(f"root window = {int(r.winfo_rootx())}+{int(r.winfo_rooty())}")
        # print(f"settings window = {int(s.winfo_rootx())}+{int(s.winfo_rooty())}")
            
        s.config(bg = 'black')

        s.protocol("WM_DELETE_WINDOW", lambda: exit_settings(r,s))

        bg_color = [169,169,169]


        top_frame = Label(s, bg = from_rgb((100,200,100)),bd = 10)
        top_frame.pack(side=TOP, fill=X)

        exit_button = Button(top_frame, text='Exit', width=7, height=3,font=('Helvatical bold',20), bg = 'teal', fg = 'black', command= lambda: exit_settings(r,s)) 
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


        settings_window = SettingsWindowTracker(s, my_canvas)
        
        
        

        setting_frame1 = Frame(main_frame, bg = from_rgb(bg_color),bd = 10)
        setting_frame1.pack(side=TOP, fill=X)
        setting_lbl = Label(setting_frame1, text = f"{'AUTO QUEEN'}: ", width=int(15), height=int(2),font=('Helvatical bold',int(25)), bg = from_rgb(bg_color),fg = 'black', pady = 10)
        setting_lbl.pack(side=LEFT)
        bg_color[0], bg_color[1], bg_color[2] = self.change_color(bg_color)
        auto_queen_b1 = tk.Button(setting_frame1, text = 'On', width=int(9), height=int(.5),font=('Helvatical bold',int(25)), bg = 'teal', fg = 'black', pady = 10,)
        auto_queen_b1.pack(side=LEFT, padx=5)
        auto_queen_b2 = tk.Button(setting_frame1, text = 'Off', width=int(9), height=int(.5),font=('Helvatical bold',int(25)), bg = 'teal', fg = 'black', pady = 10,)
        auto_queen_b2.pack(side=LEFT, padx=5)


        setting_frame2 = Frame(main_frame, bg = from_rgb(bg_color),bd = 10)
        setting_frame2.pack(side=TOP, fill=X)
        setting_lbl = Label(setting_frame2, text = f"{'WINDOWED'}: ", width=int(15), height=int(2),font=('Helvatical bold',int(25)), bg = from_rgb(bg_color),fg = 'black', pady = 10)#, image=pixeling, compound="c")
        setting_lbl.pack(side=LEFT)
        bg_color[0], bg_color[1], bg_color[2] = self.change_color(bg_color)
        windowed_b1 = tk.Button(setting_frame2, text = 'Window', width=int(9), height=int(.5),font=('Helvatical bold',int(25)), bg = 'teal', fg = 'black', pady = 10,)
        windowed_b1.pack(side=LEFT, padx=5)
        windowed_b2 = tk.Button(setting_frame2, text = 'Full Screen', width=int(9), height=int(.5),font=('Helvatical bold',int(25)), bg = 'teal', fg = 'black', pady = 10,)
        windowed_b2.pack(side=LEFT, padx=5)


        setting_frame3 = Frame(main_frame, bg = from_rgb(bg_color),bd = 10)
        setting_frame3.pack(side=TOP, fill=X)

        setting_lbl = Label(setting_frame3, text = f"{'COLOR'}: ", width=int(15), height=int(2),font=('Helvatical bold',int(25)), bg = from_rgb(bg_color),fg = 'black', pady = 10)
        setting_lbl.pack(side=LEFT)
        bg_color[0], bg_color[1], bg_color[2] = self.change_color(bg_color)

        





        setting_frame4 = Frame(main_frame, bg = from_rgb(bg_color),bd = 10)
        setting_frame4.pack(side=TOP, fill=X)

        setting_lbl = Label(setting_frame4, text = f"{'one'}: ", width=int(15), height=int(2),font=('Helvatical bold',int(25)), bg = from_rgb(bg_color),fg = 'black', pady = 10)
        setting_lbl.pack(side=LEFT)
        bg_color[0], bg_color[1], bg_color[2] = self.change_color(bg_color)

        print(setting_frame4.winfo_reqheight())

        setting_frame5= Frame(main_frame, bg = from_rgb(bg_color),bd = 10)
        setting_frame5.pack(side=TOP, fill=X)

        setting_lbl = Label(setting_frame5, text = f"{'two'}: ", width=int(15), height=int(2),font=('Helvatical bold',int(25)), bg = from_rgb(bg_color),fg = 'black', pady = 10)
        setting_lbl.pack(side=LEFT)
        bg_color[0], bg_color[1], bg_color[2] = self.change_color(bg_color)


        setting_frame6 = Frame(main_frame, bg = from_rgb(bg_color),bd = 10)
        setting_frame6.pack(side=TOP, fill=X)

        setting_lbl = Label(setting_frame6, text = f"{'three'}: ", width=int(15), height=int(2),font=('Helvatical bold',int(25)), bg = from_rgb(bg_color),fg = 'black', pady = 10)
        setting_lbl.pack(side=LEFT)
        bg_color[0], bg_color[1], bg_color[2] = self.change_color(bg_color)


        setting_frame7 = Frame(main_frame, bg = from_rgb(bg_color),bd = 10)
        setting_frame7.pack(side=TOP, fill=X)

        setting_lbl = Label(setting_frame7, text = f"{'Done'}: ", width=int(15), height=int(2),font=('Helvatical bold',int(25)), bg = from_rgb(bg_color),fg = 'black', pady = 10)
        setting_lbl.pack(side=LEFT)
        bg_color[0], bg_color[1], bg_color[2] = self.change_color(bg_color)


class SettingsWindowTracker():
    """ windows resize event tracker """

    def __init__(self, root, my_canvas):
        self.root = root
        self.width, self.height = root.winfo_width(), root.winfo_height()
        self._func_id = None
        

        self._func_id = self.root.bind("<Configure>", lambda event: self.resize(event, my_canvas))



    def resize(self, event, my_canvas):
        if(event.widget == self.root and
        (self.width != event.width or self.height != event.height)):
            self.width, self.height = event.width, event.height
            # print(f'{self.height}, {self.width}')

            #calculate what the height should be depending on how many widgets i put in
            my_canvas.itemconfig("main_frame_tag", width=self.width, height=self.height)
            
