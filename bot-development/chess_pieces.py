class ChessPiece:
    class Piece:
        def __init__(self, x, y, player):
            self.x = x
            self.y = y
            self.color = player
            self.piece_id = ""
            self.captured = False
            self.potential_positions = [f"{self.x}{self.y}"]

        def get_piece_code(self):
            if self.captured:
                return f"{self.color}{self.piece_id}00"
            return f"{self.color}{self.piece_id}{self.x}{self.y}"

        def get_potential_positions(self):
            return self.potential_positions

        def __str__(self):
            if self.captured:
                return f"{self.color}{self.piece_id}00"
            return f"{self.color}{self.piece_id}{self.x}{self.y}"

    class King(Piece):
        def __init__(self, x, y, player):
            super().__init__(x, y, player)
            self.piece_id = "K"

    class Queen(Piece):
        def __init__(self, x, y, player):
            super().__init__(x, y, player)
            self.piece_id = "Q"

    class Bishop(Piece):
        def __init__(self, x, y, player):
            super().__init__(x, y, player)
            self.piece_id = "B"

    class Knight(Piece):
        def __init__(self, x, y, player):
            super().__init__(x, y, player)
            self.piece_id = "N"

    class Rook(Piece):
        def __init__(self, x, y, player):
            super().__init__(x, y, player)
            self.piece_id = "R"

    class Pawn(Piece):
        def __init__(self, x, y, player, move_id):
            super().__init__(x, y, player)
            self.move_id = move_id
            self.piece_id = "P"

        def get_potential_positions(self):
            if self.move_id == "0":
                return [f"{self.x}{self.y + 1}",
                        f"{self.x}{self.y + 2}",
                        f"{self.x + 1}{self.y + 1}",
                        f"{self.x - 1}{self.y + 1}"]
            else:
                return [f"{self.x}{self.y + 1}",
                        f"{self.x + 1}{self.y + 1}",
                        f"{self.x - 1}{self.y + 1}"]

    def __init__(self):
        self.white_pieces = dict()
        self.black_pieces = dict()

    def add_piece(self, piece_id):
        player = piece_id[0]
        piece_type = piece_id[1]
        piece_x = piece_id[2]
        piece_y = piece_id[3]
        move_id = piece_id[4]

        if player == "W":
            if piece_type == "K":
                self.white_pieces[piece_x + piece_y] = ChessPiece.King(piece_x, piece_y, player)
            elif piece_type == "Q":
                self.white_pieces[piece_x + piece_y] = ChessPiece.Queen(piece_x, piece_y, player)
            elif piece_type == "B":
                self.white_pieces[piece_x + piece_y] = ChessPiece.Bishop(piece_x, piece_y, player)
            elif piece_type == "N":
                self.white_pieces[piece_x + piece_y] = ChessPiece.Knight(piece_x, piece_y, player)
            elif piece_type == "R":
                self.white_pieces[piece_x + piece_y] = ChessPiece.Rook(piece_x, piece_y, player)
            elif piece_type == "P":
                self.white_pieces[piece_x + piece_y] = ChessPiece.Pawn(piece_x, piece_y, player, move_id)
        elif player == "B":
            if piece_type == "K":
                self.black_pieces[piece_x + piece_y] = ChessPiece.King(piece_x, piece_y, player)
            elif piece_type == "Q":
                self.black_pieces[piece_x + piece_y] = ChessPiece.Queen(piece_x, piece_y, player)
            elif piece_type == "B":
                self.black_pieces[piece_x + piece_y] = ChessPiece.Bishop(piece_x, piece_y, player)
            elif piece_type == "N":
                self.black_pieces[piece_x + piece_y] = ChessPiece.Knight(piece_x, piece_y, player)
            elif piece_type == "R":
                self.black_pieces[piece_x + piece_y] = ChessPiece.Rook(piece_x, piece_y, player)
            elif piece_type == "P":
                self.black_pieces[piece_x + piece_y] = ChessPiece.Pawn(piece_x, piece_y, player, move_id)