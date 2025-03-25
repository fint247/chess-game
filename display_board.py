from PIL import Image, ImageTk, ImageDraw

class Piece():
    Pieces = {"p" : ("pawn", "white"),
             "n" : ("knight", "white"),
             "b" : ("bishop", "white"),
             "r" : ("rook", "white"),
             "q" : ("queen", "white"),
             "k" : ("king", "white"),
             "P" : ("pawn", "black"),
             "N" : ("knight", "black"),
             "B" : ("bishop", "black"),
             "R" : ("rook", "black"),
             "Q" : ("queen", "black"),
             "K" : ("king", "black"),
             "." : ("square", "empty")}
    
    def __init__(self, letter):
        self.color = Piece.Pieces[letter][1]
        self.name = f"{self.color}-{Piece.Pieces[letter][0]}"
        
        self.open_image= Image.open(f"img\\{self.name}.png")
        self.image= ImageTk.PhotoImage(self.open_image)

    def rescale_img(self, size):
        self.scaled_image = self.open_image.resize((size, size), Image.LANCZOS)
        self.image = ImageTk.PhotoImage(self.scaled_image)

        # # Create a new image with a transparent background
        # width, height = self.scaled_image.size  # Adjust as needed
        # self.image_overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        # # Create a drawing object
        # draw = ImageDraw.Draw(self.image_overlay)

        # # Define circle parameters
        # circle_center = (width // 2, height // 2)
        # circle_radius = self.scaled_image.size[0] // 5

        # # Draw a circle with X % transparency
        # if self.color == 'black':
        #     circle_color = (255, 255, 255, int(255 * 0.2))  # RGBA format (red, green, blue, alpha)
        # else:
        #     circle_color = (0, 0, 0, int(255 * 0.2))  # RGBA format (red, green, blue, alpha)
        # draw.ellipse(
        #     [
        #         circle_center[0] - circle_radius,
        #         circle_center[1] - circle_radius,
        #         circle_center[0] + circle_radius,
        #         circle_center[1] + circle_radius,
        #     ],
        #     fill=circle_color,
        # )

        # # Apply the mask       
        # self.legal_move_image = Image.new("RGBA", self.scaled_image.size)
        # self.legal_move_image = Image.alpha_composite(self.legal_move_image, self.scaled_image)
        # self.legal_move_image = Image.alpha_composite(self.legal_move_image, self.image_overlay)
        # self.show_legal_move_img = ImageTk.PhotoImage(self.legal_move_image)

        return self.image


class CustomBoard():    # maybe rename to DisplayBoard
    def __init__(self, string_board):
        CustomBoard.board = [[], [], [], [], [], [], [], []]
        self.update_board(string_board)
        # self.print_board()

    def update_board(self, string_board):
        for x in range(8):
            for y in range(8):
                CustomBoard.board[x].append(Piece(string_board[x*8+y]))
    
    def print_board(self):
        for row in CustomBoard.board:
            for piece in row:
                print(piece.name, end=" ")
            print()

    



        