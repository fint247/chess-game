import chess


class GameState():
    def __init__(self):
        self.board = chess.Board()
        # self.move_history = []
        # self.move_count = 0

    def make_move(self, move):
        self.board.push(move)
        # self.move_history.append(move)
        # self.move_count += 1

    def undo_move(self):
        self.board.pop()
        # self.move_history.pop()
        # self.move_count -= 1

    def reset_game(self):
        self.board.reset()
        # self.move_history = []
        # self.move_count = 0

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
        return self.board.fen()