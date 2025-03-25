import chess
from display_board import Piece, CustomBoard


 


class GameState():
    def __init__(self):
        self.board = chess.Board()
        self.display_board = CustomBoard(self.get_position())

    def move(self, move):
        self.board.push(move)
        
    def undo_move(self):
        self.board.pop()
       
    def reset_game(self):
        self.board.reset()
       
    def get_legal_moves(self):
        return self.board.legal_moves

    def get_board(self):
        return self.board

    def get_move_history(self):
        return self.board.move_stack

    def get_move_count(self):
        return self.board.fullmove_number

    def get_turn(self):
        return self.board.turn

    def get_winner(self):
        if self.board.is_checkmate():
            return "White Wins!" if GameState.get_turn() else "Black Wins!"
        if self.board.is_stalemate():
            return "Stalemate"
        if self.board.is_insufficient_material():
            return "Draw"
        if self.board.is_fivefold_repetition():
            return "Draw"
        return None

    def get_position(self):
        board_str = ""
        for rank in range(7, -1, -1):  # Iterate from rank 8 to rank 1
            for file in range(8):  # Iterate from file 'a' to 'h'
                square = chess.square(file, rank)  # Get the square index
                piece = self.board.piece_at(square)
                if piece:
                    board_str += piece.symbol()  # Add the piece symbol (e.g., 'p', 'P', 'r', etc.)
                else:
                    board_str += "."  # Add a special character for empty squares
            # board_str += "\n"  # Add a newline after each rank
        return board_str
    
