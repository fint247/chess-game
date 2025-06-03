import chess
import chess_openings
import random

class Bot:
    def __init__(self, depth=6):
        self.depth = depth
        self.best_move = None

        self.piece_value = {
            chess.PAWN: 1,
            chess.KNIGHT: 3,
            chess.BISHOP: 3,
            chess.ROOK: 5,
            chess.QUEEN: 9,
            chess.KING: 0  # King is invaluable
        }

    def evaluate_board(self, board):
        score = 0
        for piece_type in self.piece_value:
            score += len(board.pieces(piece_type, chess.WHITE)) * self.piece_value[piece_type]
            score -= len(board.pieces(piece_type, chess.BLACK)) * self.piece_value[piece_type]
        return score #if board.turn == chess.WHITE else -score

    def order_moves(self, board):
        def move_value(move):
            if board.is_capture(move):
                captured_piece = board.piece_at(move.to_square)
                return self.piece_value[captured_piece.piece_type] if captured_piece else 0
            return 0
        return sorted(board.legal_moves, key=move_value, reverse=True)

    def bestMove(self, board):
        """Finds the best move for the current board state using minimax with alpha-beta pruning."""
        self.best_move = None

        # get the FEN string without the move numbers
        fen = ' '.join(board.fen().split(' ')[:4]) 

        print(f"Current board FEN: {fen}")
        if fen in chess_openings.openings:
            opening_moves = chess_openings.openings[fen]

            # Extract moves and their probabilities
            moves = [move[1] for move in opening_moves]  # Get the UCI moves
            probabilities = [move[0] for move in opening_moves]  # Get the probabilities

            # Use random.choices to select a move based on probabilities
            return random.choices(moves, probabilities)[0]
        
        self.calcBestMove(board, self.depth)
        return self.best_move.uci() if self.best_move else None

    def calcBestMove(self, board, depth, alpha=float('-inf'), beta=float('inf')):
        """does NOT return the best move, but the best score for the current board state"""
        if depth == 0:
            return self.evaluate_board(board)

        if board.is_checkmate():
            return float('inf') if board.turn == chess.BLACK else float('-inf')
        
        if board.is_stalemate() or board.is_insufficient_material() or board.is_fivefold_repetition():
            return 0  # Draw

        best_weight = float('-inf') if board.turn == chess.WHITE else float('inf')

        for move in self.order_moves(board):
            board.push(move)
            score = self.calcBestMove(board, depth - 1, alpha, beta)
            board.pop()

            if board.turn == chess.BLACK:  # Minimizing
                if score < best_weight:
                    best_weight = score
                    if depth == self.depth:
                        self.best_move = move
                beta = min(beta, best_weight)
            else:  # Maximizing
                if score > best_weight:
                    best_weight = score
                    if depth == self.depth:
                        self.best_move = move
                alpha = max(alpha, best_weight)
            
            if beta <= alpha:
                break
        
        return best_weight
    
    def __str__(self):
        return f"Bot evaluating at depth {self.depth}"

def main1():
    bot1 = Bot()
    bot2 = Bot()
    
    game = chess.Board("r1bq1rk1/pppp1ppp/2n2n2/2b1p3/2B1P3/2N2N2/PPPP1PPP/R1BQ1RK1")
    print(game)
    
    for _ in range(4):
        bot1.bestMove(game, bot1.depth)
        if bot1.best_move is None:
            print("Game over!")
            break
        print(f"Bot 1 plays: {bot1.best_move}")
        game.push(bot1.best_move)
        print(game)
        
        bot2.bestMove(game, bot2.depth)
        if bot2.best_move is None:
            print("Game over!")
            break
        print(f"Bot 2 plays: {bot2.best_move}")
        game.push(bot2.best_move)
        print(game)

if __name__ == "__main__":
    main1()