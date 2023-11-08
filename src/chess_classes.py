from tkinter import *
import tkinter as tk 
from PIL import Image, ImageTk

from chess_setting import *




class EmptySquare():
    def __init__(self):
        self.name = 'empty_square'
        self.image = Image.open(f"trans_bg.png")
        self.image = ImageTk.PhotoImage(self.image.resize((size,size)))


class Piece():
    def __init__(self):
        # self.image = None
        pass

    def is_pieces_turn(self, valid_move, whites_turn):
        if whites_turn[0] == True and self.color == 'white':
            whites_turn[0] = False
            return valid_move[0], whites_turn[0]

        elif whites_turn[0] == False and self.color == 'black':
            whites_turn[0] = True
            return valid_move[0], whites_turn[0]

        else:
            print(f"Its not your turn")
            valid_move[0] = False
            return valid_move[0], whites_turn[0]
        
        

    def is_taking_enemy_piece():
        #might need moved to the 'pressed' function
        pass

    def is_legal(self, valid_move, whites_turn):
        valid_move[0], whites_turn[0] = self.is_pieces_turn(valid_move, whites_turn)
        return valid_move[0] , whites_turn[0]


class King(Piece):
    def __init__(self, color):
        self.name = f"{color}_king"
        self.color = color
        self.image = Image.open(f"{color}_king.png")
        self.image = ImageTk.PhotoImage(self.image.resize((size,size)))
        count = 0

        
    def is_moving_one_square():
        pass

    def is_castleing():
        pass

    def is_moving_into_check():
        pass


class Rook(Piece):
    def __init__(self, color):
        self.name = f"{color}_rook"
        self.color = color
        self.image = Image.open(f"{color}_rook.png")
        self.image = ImageTk.PhotoImage(self.image.resize((size,size)))

    def is_on_col_row():
        pass

    def is_moving_thru_piece_col_row():
        pass


class Bishop(Piece):
    def __init__(self, color):
        self.name = f"{color}_bishop"
        self.color = color
        self.image = Image.open(f"{color}_bishop.png")
        self.image = ImageTk.PhotoImage(self.image.resize((size,size)))

    def is_on_diagonal():
        pass

    def is_moving_thru_piece_diagonal():
        pass


class Queen(Rook, Bishop):
    def __init__(self, color):
        self.name = f"{color}_queen"
        self.color = color
        self.image = Image.open(f"{color}_queen.png")
        self.image = ImageTk.PhotoImage(self.image.resize((size,size)))

    pass


class Knight(Piece):
    def __init__(self, color):
        self.name = f"{color}_knight"
        self.color = color
        self.image = Image.open(f"{color}_knight.png")
        self.image = ImageTk.PhotoImage(self.image.resize((size,size)))

    def is_knight_move():
        pass


class Pawn(Piece):
    def __init__(self, color):
        self.name = f"{color}_pawn"
        self.color = color
        self.image = Image.open(f"{color}_pawn.png")
        self.image = ImageTk.PhotoImage(self.image.resize((size,size)))

    def is_one_square_forward():
        pass
    
    def is_taking_one_square_diagonal():
        pass

    def is_ampasant():
        pass

    def is_queening():
        pass



