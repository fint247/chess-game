from tkinter import *
import tkinter as tk 
from PIL import Image, ImageTk

from chess_setting import *


settings = Settings()


class EmptySquare():
    def __init__(self):
        self.name = 'empty_square'
        self.color = None
        self.ampasant = 0
        self.image = Image.open(f"trans_bg.png")
        self.image = ImageTk.PhotoImage(self.image.resize((settings.size,settings.size)))
    def is_legal(self, valid_move, whites_turn, *arg):
        valid_move[0] = False
        print("Cant move an empty square")
        return valid_move[0], whites_turn[0]



class Piece():
    def __init__(self):
        self.ampasant = 0

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
        self.image = ImageTk.PhotoImage(self.image.resize((settings.size,settings.size)))
        count = 0


    def is_king_move(self, valid_move, whites_turn, board, position_start, position_end):
        if abs(position_start[0] - position_end[0]) <= 1 and abs(position_start[1] - position_end[1]) <= 1:
            pass
        else:
            print("king can only move one square at a time")
            valid_move[0] = False
            return valid_move[0]
        
        return valid_move[0]

    def is_castleing():
        pass

    def is_moving_into_check():
        pass

    def is_legal(self, valid_move, whites_turn, board, position_start, position_end):
        valid_move[0] = self.is_king_move(valid_move, whites_turn, board, position_start, position_end)

        valid_move[0], whites_turn[0] = super().is_legal(valid_move, whites_turn, board, position_start, position_end)# must be called last
        return valid_move[0], whites_turn[0]



class Pawn(Piece):
    def __init__(self, color):
        self.name = f"{color}_pawn"
        self.ampasant = False
        self.color = color
        self.image = Image.open(f"{color}_pawn.png")
        self.image = ImageTk.PhotoImage(self.image.resize((settings.size,settings.size)))

    def is_one_square_forward(self, valid_move, whites_turn, board, position_start, position_end, pos_neg):
        temp_valid_move = valid_move.copy()
        if position_start[0] == 1 and position_end[0] == 3 and self.color == 'black' and position_start[1] - position_end[1] == 0 and board[position_start[0]-pos_neg][position_start[1]].name == 'empty_square' and board[position_start[0]-pos_neg-pos_neg][position_start[1]].name == 'empty_square' or position_start[0] == 6 and position_end[0] == 4 and self.color == 'white' and position_start[1] - position_end[1] == 0 and board[position_start[0]-pos_neg][position_start[1]].name == 'empty_square' and board[position_start[0]-pos_neg-pos_neg][position_start[1]].name == 'empty_square':
            pass
            # if position_start[1] - position_end[1] == 0 and board[position_start[0]-pos_neg][position_start[1]].name == 'empty_square' and board[position_start[0]-pos_neg-pos_neg][position_start[1]].name == 'empty_square':
           
        elif position_start[0] - position_end[0] == 1*pos_neg and position_start[1] - position_end[1] == 0 and board[position_end[0]][position_end[1]].name == 'empty_square':
            pass

        else:
            temp_valid_move[0] = False
        
        # print(position_start[0] - position_end[0] , 1*pos_neg ,'and', position_start[1] - position_end[1] , 0 ,'and', board[position_end[0]][position_end[1]].name , 'empty_square')
        return temp_valid_move[0]
    
    def is_taking_one_square_diagonal(self, valid_move, whites_turn, board, position_start, position_end, pos_neg):
        temp_valid_move = valid_move.copy()
        if board[position_end[0]][position_end[1]].name != 'empty_square' and abs(position_start[1] - position_end[1]) == 1 and position_start[0] - position_end[0] == 1*pos_neg:
            pass
        
        elif True == False:#awpasant rule
            pass
        else:
            temp_valid_move[0] = False
        return temp_valid_move[0]

    def is_ampasant(self, valid_move, whites_turn, board, position_start, position_end, pos_neg):
        print(board[position_end[0]+pos_neg][position_end[1]].name ,'==', 'white_pawn' ,'and', self.color ,'!=', board[position_end[0]+pos_neg][position_end[1]].color ,'or', board[position_end[0]+pos_neg][position_end[1]].name ,'==', 'black_pawn' ,'and', self.color ,'!=', board[position_end[0]+pos_neg][position_end[1]].color)
        print(board[position_end[0]+pos_neg][position_end[1]].ampasant, f"({position_end[0]+pos_neg},{position_end[1]})" ,'==', True , 'and', abs(position_start[1] - position_end[1]) ,'==', 1 ,'and', position_start[0] - position_end[0] ,'==', 1*pos_neg)
        if board[position_end[0]+pos_neg][position_end[1]].name == 'white_pawn' and self.color != board[position_end[0]+pos_neg][position_end[1]].color or board[position_end[0]+pos_neg][position_end[1]].name == 'black_pawn' and self.color != board[position_end[0]+pos_neg][position_end[1]].color:
            if board[position_end[0]+pos_neg][position_end[1]].ampasant == True and abs(position_start[1] - position_end[1]) == 1 and position_start[0] - position_end[0] == 1*pos_neg:
                board[position_end[0]+pos_neg][position_end[1]] = board[position_end[0]][position_end[1]]
            else:
                valid_move[0] = False
        else:
            valid_move[0] = False
        return valid_move[0]

    def is_queening():
        pass #when queening add a window that pops up asking what piece you want to promote to
    
    def is_pawn_move(self, valid_move, whites_turn, board, position_start, position_end):
        if self.color == 'white':
            pos_neg = 1
        elif self.color == 'black':
            pos_neg = -1

        if self.is_one_square_forward(valid_move, whites_turn, board, position_start, position_end, pos_neg) == True or self.is_taking_one_square_diagonal(valid_move, whites_turn, board, position_start, position_end, pos_neg) == True or self.is_ampasant(valid_move, whites_turn, board, position_start, position_end, pos_neg) == True:
            pass
        else:
            valid_move[0] = False
            return valid_move[0]
        return valid_move[0]

    def is_legal(self, valid_move, whites_turn, board, position_start, position_end):
        valid_move[0] = self.is_pawn_move(valid_move, whites_turn, board, position_start, position_end)
        
        valid_move[0], whites_turn[0] = super().is_legal(valid_move, whites_turn, board, position_start, position_end)# must be called last
    
        return valid_move[0], whites_turn[0]




class Rook(Piece):
    def __init__(self, color):
        self.name = f"{color}_rook"
        self.color = color
        self.image = Image.open(f"{color}_rook.png")
        self.image = ImageTk.PhotoImage(self.image.resize((settings.size,settings.size)))

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
            raise Exception('problem with pos_neg variable')

        if index_num == 0 and op_index_num == 1:
            for i in range(position_start[index_num] + pos_neg, position_end[index_num], pos_neg):
                if board[i][position_start[op_index_num]].name != 'empty_square':
                    valid_move[0] = False
                    
        elif index_num == 1 and op_index_num == 0:
            for i in range(position_start[index_num] + pos_neg, position_end[index_num], pos_neg):
                if board[position_start[op_index_num]][i].name != 'empty_square':
                    valid_move[0] = False
                    
        else:
            raise Exception("bad input for index_nun or op_index_num in thru_piece_col_row_helper")
        
        return valid_move[0]


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
        self.image = ImageTk.PhotoImage(self.image.resize((settings.size,settings.size)))

    def is_on_diagonal(self, valid_move, position_start, position_end):
        # print(f"({(position_start[0])}-{(position_end[0])})/({(position_start[1])}-{(position_end[1])}) = {(abs((position_start[0]) - (position_end[0]))+1)}/{(abs((position_start[1]) - (position_end[1]))+1)}")
        if (abs(position_start[0] - position_end[0]) + 1) / (abs(position_start[1] - position_end[1]) + 1) != 1:
            print(f'{self.name}s can only move on a diagonal')
            valid_move[0] = False
        return valid_move[0]

    def is_moving_thru_piece_diagonal(self, valid_move, board, position_start, position_end):
        if position_end[1] > position_start[1]:
            pos_neg = 1
        elif position_end[1] < position_start[1]:
            pos_neg = -1
        else:
            print('problem with pos_neg diagonal variable')
            pos_neg = False
            valid_move[0] = False

        if position_end[0] > position_start[0]:
            neg_pos = 1
        elif position_end[0] < position_start[0]:
            neg_pos = -1
        else:
            print('problem with pos_neg diagonal variable')
            neg_pos = False
            valid_move[0] = False


        if pos_neg != False and neg_pos != False:
        #    print('loop number = ',abs(position_start[0] - position_end[0])-1)
           for x in range(1,abs(position_start[0] - position_end[0])):
                # print('')
                # print(f"x = {x}")
                # print(f"{position_start[0]+x*neg_pos}, {position_start[1]+x*pos_neg}")
                # print(f"{position_start[0]}+{x}*{neg_pos}, {position_start[1]}+{x}*{pos_neg}")
                # print(board[position_start[0]+x*neg_pos][position_start[1]+x*pos_neg].name)
                if board[position_start[0]+x*neg_pos][position_start[1]+x*pos_neg].name != 'empty_square':
                    print("Cant move thru your own peices")
                    valid_move[0] = False
                    return valid_move[0]

        return valid_move[0]


    def is_legal(self, valid_move, whites_turn, board, position_start, position_end):
        valid_move[0] = self.is_on_diagonal(valid_move, position_start, position_end)
        valid_move[0] = self.is_moving_thru_piece_diagonal(valid_move, board, position_start, position_end)
        
        valid_move[0], whites_turn[0] = super().is_legal(valid_move, whites_turn, board, position_start, position_end)
        return valid_move[0], whites_turn[0]
    


class Queen(Rook, Bishop):
    def __init__(self, color):
        self.name = f"{color}_queen"
        self.color = color
        self.image = Image.open(f"{color}_queen.png")
        self.image = ImageTk.PhotoImage(self.image.resize((settings.size,settings.size)))

    def is_legal(self, valid_move, whites_turn, board, position_start, position_end):
        if self.is_on_col_row(valid_move, position_start, position_end) == True:
            valid_move[0] = self.is_moving_thru_piece_col_row(valid_move, board, position_start, position_end)
        
        elif self.is_on_diagonal(valid_move, position_start, position_end) == True:
            valid_move[0] = self.is_moving_thru_piece_diagonal(valid_move, board, position_start, position_end)
        
        valid_move[0] = self.not_taking_own_piece(valid_move, board, position_start, position_end)
        valid_move[0], whites_turn[0] = self.is_pieces_turn(valid_move, whites_turn) #this must be the last method called because of whites_turn variable
        return valid_move[0], whites_turn[0]



class Knight(Piece):
    def __init__(self, color):
        self.name = f"{color}_knight"
        self.color = color
        self.image = Image.open(f"{color}_knight.png")
        self.image = ImageTk.PhotoImage(self.image.resize((settings.size,settings.size)))

    def is_knight_move(self, valid_move, whites_turn, board, position_start, position_end):
        # print(abs(position_end[1]-position_start[1]) , abs(position_end[0] - position_start[0]) , 'or',  abs(position_end[1]-position_start[1]) , abs(position_end[0] - position_start[0]))
        if abs(position_end[1]-position_start[1]) == 1 and abs(position_end[0] - position_start[0]) == 2 or abs(position_end[1]-position_start[1]) == 2 and abs(position_end[0] - position_start[0]) == 1:
            pass
        else:
            print("knight can only move in an 'L' shape")
            valid_move[0] = False
        return valid_move[0]

    def is_legal(self, valid_move, whites_turn, board, position_start, position_end):
        valid_move[0] = self.is_knight_move(valid_move, whites_turn, board, position_start, position_end)

        valid_move[0], whites_turn[0] = super().is_legal(valid_move, whites_turn, board, position_start, position_end)# must be called last
        return valid_move[0], whites_turn[0]


