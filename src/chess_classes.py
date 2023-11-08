from tkinter import *
import tkinter as tk 
from PIL import Image, ImageTk

from chess_setting import *




class EmptySquare():
    def __init__(self):
        self.name = 'empty_square'
        self.color = None
        self.image = Image.open(f"trans_bg.png")
        self.image = ImageTk.PhotoImage(self.image.resize((size,size)))
    def is_legal(self, valid_move, whites_turn, *arg):
        valid_move[0] = False
        print("Cant move an empty square")
        return valid_move[0], whites_turn[0]

class Piece():
    def __init__(self):
        # self.image = None
        pass

    def is_pieces_turn(self, valid_move, whites_turn):
        if whites_turn[0] == True and self.color == 'white' and valid_move[0] == True:
            whites_turn[0] = False
            return valid_move[0], whites_turn[0]

        elif whites_turn[0] == False and self.color == 'black' and valid_move[0] == True:
            whites_turn[0] = True
            return valid_move[0], whites_turn[0]

        else:
            if valid_move[0] == True:
                print(f"Its not your turn")
            valid_move[0] = False
            return valid_move[0], whites_turn[0]
        
        

    def not_taking_own_piece(self, valid_move, board, position_start, position_end):
        if self.color == board[position_end[0]][position_end[1]].color:
            print("Cant take your own pieces")
            valid_move[0] = False
        return valid_move[0]

    def is_legal(self, valid_move, whites_turn, board, position_start, position_end):
        valid_move[0] = self.not_taking_own_piece(valid_move, board, position_start, position_end)
        valid_move[0], whites_turn[0] = self.is_pieces_turn(valid_move, whites_turn) #this must be the last method called because of whites_turn variable
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

    def is_on_col_row(self, valid_move, position_start, position_end):
        if position_start[0] != position_end[0] and position_start[1] != position_end[1]:
            valid_move[0] = False
            print(f"{self.name}s can only move in columns or rows")
        return valid_move[0]
    
    def thru_piece_col_row_helper(self, valid_move, board, position_start, position_end, index_num, op_index_num):
        if position_end[index_num] > position_start[index_num]:
            pos_neg = 1
        elif position_end[index_num] < position_start[index_num]:
            pos_neg = -1
        else:
            pos_neg = 0
        
        if index_num == 0 and op_index_num == 1:
            for i in range(position_start[index_num] + pos_neg, position_end[index_num], pos_neg):
                if board[i][position_start[op_index_num]].name != 'empty_square':
                    print('Cant move thru pieces')
                    valid_move[0] = False
                    return valid_move[0]

                    
        elif index_num == 1 and op_index_num == 0:
            for i in range(position_start[index_num] + pos_neg, position_end[index_num], pos_neg):
                if board[position_start[op_index_num]][i].name != 'empty_square':
                    print('Cant move thru pieces')
                    valid_move[0] = False
                    return valid_move[0]

        else:
            raise Exception("bad input for index_nun or op_index_num in thru_piece_col_row_helper")



    def is_moving_thru_piece_col_row(self, valid_move, board, position_start, position_end):
        if position_start[1] == position_end[1]: #checks on columns
            valid_move[0] = self.thru_piece_col_row_helper(valid_move, board, position_start, position_end, 0, 1)
        
        elif position_start[0] == position_end[0]: #checks on rows
            valid_move[0] = self.thru_piece_col_row_helper(valid_move, board, position_start, position_end, 1, 0)
        
        return valid_move[0]
                

    def is_legal(self, valid_move, whites_turn, board, position_start, position_end):
        valid_move[0] = self.is_on_col_row(valid_move, position_start, position_end)
        valid_move[0] = self.is_moving_thru_piece_col_row(valid_move, board, position_start, position_end)

        valid_move[0], whites_turn[0] = super().is_legal(valid_move, whites_turn, board, position_start, position_end)# must be called last
        return valid_move[0], whites_turn[0]



class Bishop(Piece):
    def __init__(self, color):
        self.name = f"{color}_bishop"
        self.color = color
        self.image = Image.open(f"{color}_bishop.png")
        self.image = ImageTk.PhotoImage(self.image.resize((size,size)))

    def is_on_diagonal(self, valid_move, position_start, position_end):
        # print(f"({(position_start[0])}-{(position_end[0])})/({(position_start[1])}-{(position_end[1])}) = {(abs((position_start[0]) - (position_end[0]))+1)}/{(abs((position_start[1]) - (position_end[1]))+1)}")
        if (abs(position_start[0] - position_end[0]) + 1) / (abs(position_start[1] - position_end[1]) + 1) != 1:
            print(f'{self.name}s can only move on a diagonal')
            valid_move[0] = False
        return valid_move[0]

    def is_moving_thru_piece_diagonal():
        pass

    def is_legal(self, valid_move, whites_turn, board, position_start, position_end):
        valid_move[0] = self.is_on_diagonal(valid_move, position_start, position_end)

        valid_move[0], whites_turn[0] = super().is_legal(valid_move, whites_turn, board, position_start, position_end)
        return valid_move[0], whites_turn[0]
    


class Queen(Rook, Bishop):
    def __init__(self, color):
        self.name = f"{color}_queen"
        self.color = color
        self.image = Image.open(f"{color}_queen.png")
        self.image = ImageTk.PhotoImage(self.image.resize((size,size)))


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



