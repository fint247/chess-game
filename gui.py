import tkinter as tk
from gui_settings import *


class GUI():
    def __init__(self):   # treate this as the main
        """Main function to initialize and run the Tkinter GUI"""
        self.root = tk.Tk() 
        self.root.title('UVSim') 
        self.root.geometry('900x600-0+0')    # "-0+0" puts window in top right corner

        self.theme = DefaultTheme()

        self.root_frames = {}
        self.main_frames = {}
        self.setting_frames = {}

        self.widgets = [self.root_frames, self.main_frame, self.setting_frames]


        self.create_layout(self.root)

        self.root.mainloop()

    def create_root_layout(root):
        pass

    def create_main_layout(self, frame):
        """Creates the main layout frames (header, editor, terminal)."""

        self.setting_frame = tk.Frame(frame)
        self.setting_frame.place(relx=0,rely=0,relwidth=1, relheight=1)

        setting_header = tk.Frame(self.setting_frame, bg=self.theme.header_color)
        setting_header.place(relx=0,rely=0,relwidth=1, relheight=.03)

        settings_content_frame = tk.Frame(self.setting_frame, bg=self.theme.editor_color)
        settings_content_frame.place(relx=0,rely=.03,relwidth=1, relheight=.97)

        self.main_frame = tk.Frame(frame)
        self.main_frame.place(relx=0,rely=0,relwidth=1, relheight=1)

        menu_header = tk.Frame(self.main_frame, bg=self.theme.header_color)
        menu_header.place(relx=0,rely=0,relwidth=.1, relheight=1)

        self.game_header = tk.Frame(self.main_frame, bg=self.theme.file_header_color)
        self.game_header.place(relx=.9,rely=0,relwidth=.1, relheight=1)

        editor = tk.Frame(self.main_frame, bg=self.theme.editor_color)
        editor.place(relx=0,rely=.06,relwidth=1, relheight=.57)

        terminal = tk.Frame(self.main_frame, bg=self.theme.output_color)
        terminal.place(relx=0,rely=.63,relwidth=1, relheight=.4)

        return menu_header, self.file_header, editor, terminal, setting_header, settings_content_frame

    def create_setting_layout(frame):
        pass

    def add_bot(bot, color : bool = True):
        pass