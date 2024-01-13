# from tkinter import *
# from PIL import Image, ImageTk, ImageDraw

from chess_setting import *


settings = Settings()





class Piece():
    def __init__(self, color):
        self.ampasant = False
        self.color = color
        self.has_moved = False

        self.open_image= Image.open(f"{self.name}.png")
        self.image= ImageTk.PhotoImage(self.open_image)



    def rescale_img(self):
        self.scaled_image = self.open_image.resize((settings.size,settings.size), Image.LANCZOS)
        self.image = ImageTk.PhotoImage(self.scaled_image)


        # Create a new image with a transparent background
        width, height = self.scaled_image.size  # Adjust as needed
        self.image_overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        # Create a drawing object
        draw = ImageDraw.Draw(self.image_overlay)

        # Define circle parameters
        circle_center = (width // 2, height // 2)
        circle_radius = self.scaled_image.size[0] // 5

        # Draw a circle with X % transparency
        circle_color = (255, 0, 255, int(255 * 0.5))  # RGBA format (red, green, blue, alpha)
        draw.ellipse(
            [
                circle_center[0] - circle_radius,
                circle_center[1] - circle_radius,
                circle_center[0] + circle_radius,
                circle_center[1] + circle_radius,
            ],
            fill=circle_color,
        )

        # Apply the mask       
        self.legal_move_image = Image.new("RGBA", self.scaled_image.size)
        self.legal_move_image = Image.alpha_composite(self.legal_move_image, self.scaled_image)
        self.legal_move_image = Image.alpha_composite(self.legal_move_image, self.image_overlay)
        self.show_legal_move_img = ImageTk.PhotoImage(self.legal_move_image)

        return self.image
    
   
    def is_pieces_turn(self, valid_move, whites_turn):
        if whites_turn[0] == True and self.color == 'white' and valid_move == True:
            return valid_move

        elif whites_turn[0] == False and self.color == 'black' and valid_move == True:
            return valid_move

        else:
            if valid_move == True:
                print(f"Its not your turn")
            valid_move = False
            return valid_move
        
    def not_taking_own_piece(self, valid_move, board, position_start, position_end):
        if self.color == board[position_end[0]][position_end[1]].color:
            # print("Cant take your own pieces")
            # print(board[position_end[0]][position_end[1]].name)
            # print(board[position_start[0]][position_start[1]].name)
            valid_move = False
        return valid_move

    def is_legal(self, valid_move, whites_turn, board, position_start, position_end):
        valid_move = self.not_taking_own_piece(valid_move, board, position_start, position_end)
        valid_move = self.is_pieces_turn(valid_move, whites_turn) 
        return valid_move



class EmptySquare(Piece):
    def __init__(self):
        self.name = 'empty_square'
        self.color = 'None'

        super().__init__(self.color)

       
    def is_legal(self, whites_turn, board, position_start, position_end):
        valid_move = False
        # print("Rule Break: Cant move an empty square")
        return valid_move
    


class King(Piece):
    def __init__(self, color):
        self.name = f"{color}_king"
        super().__init__(color)

    
    def is_king_move(self, valid_move, whites_turn, board, position_start, position_end):
        temp_valid_move = bool(valid_move)
        if abs(position_start[0] - position_end[0]) <= 1 and abs(position_start[1] - position_end[1]) <= 1:
            # if self.is_moving_into_check(temp_valid_move, whites_turn, board, position_start, position_end) == False:
            #     print("Rule Break: cant move into check")
            #     temp_valid_move = False
            # print('valid move should = True --> ',valid_move)
            pass
            
        else:
            # print("Rule Break: king can only move one square at a time")
            temp_valid_move = False
            return temp_valid_move
        
        return temp_valid_move

    def is_castleing(self, valid_move, whites_turn, board, position_start, position_end):
        if board[position_start[0]][position_start[1]].has_moved == False:
            temp_valid_move = bool(valid_move)
            if abs(position_start[1] - position_end[1]) == 2 and position_start[0] - position_end[0] == 0:
                rook_pos = []
                if whites_turn[0] == True:
                    colors_row = 7
                else:
                    colors_row = 0

                for i in range(8):
                    if board[colors_row][i].name == f"{self.color}_king":
                        king_pos = i
                    elif board[colors_row][i].name == f"{self.color}_rook" and board[colors_row][i].has_moved == False:
                        rook_pos.append(i)
        
                # print(rook_pos, king_pos)
                if len(rook_pos) > 0:
                    for x in rook_pos:
                        if position_end[1] < position_start[1] and x < king_pos:
                            for y in range(x+1, king_pos):
                                print(y,':',board[colors_row][y].name)
                                if board[colors_row][y].name != 'empty_square':
                                    # print('Rule Break: cant castle thru ',board[colors_row][y].name)
                                    temp_valid_move = False
                        
                        elif position_end[1] > position_start[1] and x > king_pos:
                            for y in range(king_pos+1 , x):
                                print(y,': ',board[colors_row][y].name)
                                if board[colors_row][y].name != 'empty_square':
                                    # print('Rule Break: cant castle thru ',board[colors_row][y].name)
                                    temp_valid_move = False
                else:
                    temp_valid_move = False
            else:
                temp_valid_move = False
        else:
            temp_valid_move = False

        return temp_valid_move
                
            

    def is_moving_into_check(self, valid_move, whites_turn, board, position_start, position_end):

        """
        problem where a kings .legal func keeps calling itself over and over

        A king should be able to move next to another king as long as its defended which is a problem
        """

        # print('HERE = ', valid_move)
        temp_empty_square = EmptySquare()
        temp_board = [ row.copy() for row in board]
        temp_valid_move = bool(valid_move)
        temp_whites_turn = whites_turn.copy()

        temp_board[position_end[0]][position_end[1]] = temp_board[position_start[0]][position_start[1]]
        temp_board[position_start[0]][position_start[1]] = temp_empty_square

        for a in range(8):
            for b in range(8):
                temp_position_start = [a,b]
                # print(f"{temp_position_start} --> {position_end}")
                # if self.name != "white_king":
                if self.name == "white_king" and temp_board[temp_position_start[0]][temp_position_start[1]].name == 'black_king' or self.name == "black_king" and temp_board[temp_position_start[0]][temp_position_start[1]].name == 'white_king':
                    print('found a king',temp_position_start, position_end)
                    if abs(temp_position_start[0] - position_end[0]) <= 1 and abs(temp_position_start[1] - position_end[1]) <= 1:
                        print('NONONONONONONONON') 
                        z = True
                elif temp_position_start == position_end:
                    pass
                else:
                    z = temp_board[temp_position_start[0]][temp_position_start[1]].is_legal(temp_valid_move, temp_whites_turn, temp_board, temp_position_start, position_end)
                    print(temp_position_start, position_end, z, '\n')
                if z == True: 
                    print('\n\n',temp_position_start,position_end,'++++++++++++++++++++++++++++++++++++++++\n\n')
                    valid_move = False
        
        # print('HERE = ', valid_move)
        valid_move = True
        return valid_move



    def is_legal(self, whites_turn, board, position_start, position_end):
        # print('\n\n===============',position_start,position_end,'=========================\n\n')
        valid_move = True
        if self.is_king_move(valid_move, whites_turn, board, position_start, position_end) == True:
            pass
        elif self.is_castleing(valid_move, whites_turn, board, position_start, position_end) == True:
            pass
        else:
            valid_move = False

        if valid_move == True:
            valid_move = super().is_legal(valid_move, whites_turn, board, position_start, position_end)
        return valid_move



class Pawn(Piece):
    def __init__(self, color):
        self.name = f"{color}_pawn"
        self.ampasant = False
        self.promoted = False
        super().__init__(color)

    
    def is_one_square_forward(self, valid_move, whites_turn, board, position_start, position_end, pos_neg):
        temp_valid_move = bool(valid_move)
        if position_start[0] == 1 and position_end[0] == 3 and self.color == 'black' and position_start[1] - position_end[1] == 0 and board[position_start[0]-pos_neg][position_start[1]].name == 'empty_square' and board[position_start[0]-pos_neg-pos_neg][position_start[1]].name == 'empty_square' or position_start[0] == 6 and position_end[0] == 4 and self.color == 'white' and position_start[1] - position_end[1] == 0 and board[position_start[0]-pos_neg][position_start[1]].name == 'empty_square' and board[position_start[0]-pos_neg-pos_neg][position_start[1]].name == 'empty_square':
            #moved two squares forward
            self.ampasant = True
            # if position_start[1] - position_end[1] == 0 and board[position_start[0]-pos_neg][position_start[1]].name == 'empty_square' and board[position_start[0]-pos_neg-pos_neg][position_start[1]].name == 'empty_square':
           
        elif position_start[0] - position_end[0] == 1*pos_neg and position_start[1] - position_end[1] == 0 and board[position_end[0]][position_end[1]].name == 'empty_square':
            pass

        else:
            temp_valid_move = False
        
        # print(position_start[0] - position_end[0] , 1*pos_neg ,'and', position_start[1] - position_end[1] , 0 ,'and', board[position_end[0]][position_end[1]].name , 'empty_square')
        return temp_valid_move
    
    def is_taking_one_square_diagonal(self, valid_move, whites_turn, board, position_start, position_end, pos_neg):
        temp_valid_move = bool(valid_move)
        if board[position_end[0]][position_end[1]].name != 'empty_square' and abs(position_start[1] - position_end[1]) == 1 and position_start[0] - position_end[0] == 1*pos_neg:
            pass
        
        elif True == False:#awpasant rule
            pass
        else:
            temp_valid_move = False
        return temp_valid_move

    def is_ampasant(self, valid_move, whites_turn, board, position_start, position_end, pos_neg):
        # print(board[position_end[0]+pos_neg][position_end[1]].name ,'==', 'white_pawn' ,'and', self.color ,'!=', board[position_end[0]+pos_neg][position_end[1]].color ,'or', board[position_end[0]+pos_neg][position_end[1]].name ,'==', 'black_pawn' ,'and', self.color ,'!=', board[position_end[0]+pos_neg][position_end[1]].color)
        # print(board[position_end[0]+pos_neg][position_end[1]].ampasant, f"({position_end[0]+pos_neg},{position_end[1]})" ,'==', True , 'and', abs(position_start[1] - position_end[1]) ,'==', 1 ,'and', position_start[0] - position_end[0] ,'==', 1*pos_neg)
        
        if not(pos_neg + position_end[0] < 0 or  pos_neg + position_end[0] > 7):#fix to a pawn bug due to pos_neg variable
            if board[position_end[0]+pos_neg][position_end[1]].name == 'white_pawn' and self.color != board[position_end[0]+pos_neg][position_end[1]].color or board[position_end[0]+pos_neg][position_end[1]].name == 'black_pawn' and self.color != board[position_end[0]+pos_neg][position_end[1]].color:
                if board[position_end[0]+pos_neg][position_end[1]].ampasant == True and abs(position_start[1] - position_end[1]) == 1 and position_start[0] - position_end[0] == 1*pos_neg:
                    board[position_end[0]+pos_neg][position_end[1]] = board[position_end[0]][position_end[1]]
                else:
                    valid_move = False  
            else:
                valid_move = False
        else:
            valid_move = False

        return valid_move

    def is_pawn_move(self, valid_move, whites_turn, board, position_start, position_end):
        if self.color == 'white':
            pos_neg = 1
        elif self.color == 'black':
            pos_neg = -1

        if (self.is_one_square_forward(valid_move, whites_turn, board, position_start, position_end, pos_neg) == True 
            or self.is_taking_one_square_diagonal(valid_move, whites_turn, board, position_start, position_end, pos_neg) == True 
            or self.is_ampasant(valid_move, whites_turn, board, position_start, position_end, pos_neg) == True):
            pass
        else:
            valid_move = False
            return valid_move
        return valid_move
    
    def is_queening(self, valid_move, whites_turn, board, position_start, position_end):
        if position_end[0] == 0 and self.color == 'white' or position_end[0] == 7 and self.color == 'black':
            self.promoted = True
        return valid_move

    def is_legal(self, whites_turn, board, position_start, position_end):
        valid_move = True
        if valid_move == True:
            valid_move = self.is_pawn_move(valid_move, whites_turn, board, position_start, position_end)
        if valid_move == True:
            valid_move = self.is_queening(valid_move, whites_turn, board, position_start, position_end)
        if valid_move == True:
            valid_move = super().is_legal(valid_move, whites_turn, board, position_start, position_end)


        if self.promoted == True and valid_move == False:
            self.promoted = False
        return valid_move



class Rook(Piece):
    def __init__(self, color):
        self.name = f"{color}_rook"
        super().__init__(color)

    
    def is_on_col_row(self, valid_move, position_start, position_end):
        temp_valid_move = bool(valid_move)
        if position_start[0] != position_end[0] and position_start[1] != position_end[1]:
            temp_valid_move = False
            # print(f"{self.name}s can only move in columns or rows")
        if position_start == position_end:
            temp_valid_move = False
        return temp_valid_move
    
    def thru_piece_col_row_helper(self, valid_move, board, position_start, position_end, index_num, op_index_num):
        if position_end[index_num] > position_start[index_num]:
            pos_neg = 1
        elif position_end[index_num] < position_start[index_num]:
            pos_neg = -1
        else:
            print(position_start, position_end)
            raise Exception('not moving on a row/column which is breaking pos_neg variable')

        if index_num == 0 and op_index_num == 1:
            for i in range(position_start[index_num] + pos_neg, position_end[index_num], pos_neg):
                if board[i][position_start[op_index_num]].name != 'empty_square':
                    valid_move = False
                    
        elif index_num == 1 and op_index_num == 0:
            for i in range(position_start[index_num] + pos_neg, position_end[index_num], pos_neg):
                if board[position_start[op_index_num]][i].name != 'empty_square':
                    valid_move = False
                    
        else:
            raise Exception("bad input for index_nun or op_index_num in thru_piece_col_row_helper")
        
        return valid_move


    def is_moving_thru_piece_col_row(self, valid_move, board, position_start, position_end):
        if position_start[1] == position_end[1]: #checks on columns
            valid_move = self.thru_piece_col_row_helper(valid_move, board, position_start, position_end, 0, 1)
        
        elif position_start[0] == position_end[0]: #checks on rows
            valid_move = self.thru_piece_col_row_helper(valid_move, board, position_start, position_end, 1, 0)
        
        return valid_move
                

    def is_legal(self, whites_turn, board, position_start, position_end):
        valid_move = True
        valid_move = self.is_on_col_row(valid_move, position_start, position_end)
        if valid_move == True:
            valid_move = self.is_moving_thru_piece_col_row(valid_move, board, position_start, position_end)
        
        if valid_move == True:
            valid_move = super().is_legal(valid_move, whites_turn, board, position_start, position_end)
        return valid_move



class Bishop(Piece):
    def __init__(self, color):
        self.name = f"{color}_bishop"
        super().__init__(color)

    
    def is_on_diagonal(self, valid_move, position_start, position_end):
        temp_valid_move = bool(valid_move)
        # print(f"({(position_start[0])}-{(position_end[0])})/({(position_start[1])}-{(position_end[1])}) = {(abs((position_start[0]) - (position_end[0]))+1)}/{(abs((position_start[1]) - (position_end[1]))+1)}")
        if (abs(position_start[0] - position_end[0]) + 1) / (abs(position_start[1] - position_end[1]) + 1) != 1:
            # print(f'Rule Break: {self.name}s can only move on a diagonal')
            temp_valid_move = False

        if position_start == position_end:
            temp_valid_move = False
        return temp_valid_move

    def is_moving_thru_piece_diagonal(self, valid_move, board, position_start, position_end):
        if position_end[1] > position_start[1]:
            pos_neg = 1
        elif position_end[1] < position_start[1]:
            pos_neg = -1
        else:
            print(position_start, position_end)
            raise Exception('not moving on diagonal which is breaking pos_neg variable')

        if position_end[0] > position_start[0]:
            neg_pos = 1
        elif position_end[0] < position_start[0]:
            neg_pos = -1
        else:
            # print('problem with pos_neg diagonal variable')
            neg_pos = False
            valid_move = False


        if pos_neg != False and neg_pos != False:
        #    print('loop number = ',abs(position_start[0] - position_end[0])-1)
           for x in range(1,abs(position_start[0] - position_end[0])):
                # print('')
                # print(f"x = {x}")
                # print(f"{position_start[0]+x*neg_pos}, {position_start[1]+x*pos_neg}")
                # print(f"{position_start[0]}+{x}*{neg_pos}, {position_start[1]}+{x}*{pos_neg}")
                # print(board[position_start[0]+x*neg_pos][position_start[1]+x*pos_neg].name)
                if board[position_start[0]+x*neg_pos][position_start[1]+x*pos_neg].name != 'empty_square':
                    # print("Rule Break: Cant move thru your own peices")
                    valid_move = False
                    return valid_move

        return valid_move


    def is_legal(self, whites_turn, board, position_start, position_end):
        valid_move = True
        valid_move = self.is_on_diagonal(valid_move, position_start, position_end)
        if valid_move == True:
            valid_move = self.is_moving_thru_piece_diagonal(valid_move, board, position_start, position_end)
        if valid_move == True:
            valid_move = super().is_legal(valid_move, whites_turn, board, position_start, position_end)
        return valid_move
    


class Queen(Rook, Bishop):
    def __init__(self, color):
        self.name = f"{color}_queen"
        Piece.__init__(self, color)

   
    def is_legal(self, whites_turn, board, position_start, position_end):
        valid_move = True
        if self.is_on_col_row(valid_move, position_start, position_end) == True:
            if not self.is_moving_thru_piece_col_row(valid_move, board, position_start, position_end) == True:
                valid_move = False

        elif self.is_on_diagonal(valid_move, position_start, position_end) == True:
            if not self.is_moving_thru_piece_diagonal(valid_move, board, position_start, position_end) == True:
                valid_move = False
        
        else:
            valid_move = False

        if valid_move == True:
            valid_move = self.not_taking_own_piece(valid_move, board, position_start, position_end)
        if valid_move == True:
            valid_move = self.is_pieces_turn(valid_move, whites_turn) 
        return valid_move



class Knight(Piece):
    def __init__(self, color):
        self.name = f"{color}_knight"
        super().__init__(color)

    
    def is_knight_move(self, valid_move, whites_turn, board, position_start, position_end):
        # print(abs(position_end[1]-position_start[1]) , abs(position_end[0] - position_start[0]) , 'or',  abs(position_end[1]-position_start[1]) , abs(position_end[0] - position_start[0]))
        if abs(position_end[1]-position_start[1]) == 1 and abs(position_end[0] - position_start[0]) == 2 or abs(position_end[1]-position_start[1]) == 2 and abs(position_end[0] - position_start[0]) == 1:
            pass
        else:
            # print("Rule Break: knight can only move in an 'L' shape")
            valid_move = False
        return valid_move

    def is_legal(self, whites_turn, board, position_start, position_end):
        valid_move = True
        valid_move = self.is_knight_move(valid_move, whites_turn, board, position_start, position_end)

        if valid_move == True:
            valid_move = super().is_legal(valid_move, whites_turn, board, position_start, position_end)
        return valid_move


