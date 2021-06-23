class Board:
    def __init__(self, board=None):
        # self.board[self.x[] + self.y[]] = f""
        self.x = ["a", "b", "c", "d", "e", "f", "g", "h"]
        self.y = ["1", "2", "3", "4", "5", "6", "7", "8"]
        if board == None:
            self.board = dict()
            self.board["captured"] = []
            for x in self.x:
                for y in self.y:
                    self.board[x + y] = " 0 "
            # Kings
            self.board[self.x[4] + self.y[0]] = "WK1"  # {self.x[4]}{self.y[1]}
            self.board[self.x[4] + self.y[7]] = "BK1"  # {self.x[4]}{self.y[1]}
            # Queens
            self.board[self.x[3] + self.y[0]] = "WQ1"
            self.board[self.x[3] + self.y[7]] = "BQ1"
            # Bishops
            self.board[self.x[2] + self.y[0]] = "WB1"
            self.board[self.x[5] + self.y[0]] = "WB1"
            self.board[self.x[2] + self.y[7]] = "BB1"
            self.board[self.x[5] + self.y[7]] = "BB1"
            # Knights
            self.board[self.x[1] + self.y[0]] = "WN1"
            self.board[self.x[6] + self.y[0]] = "WN1"
            self.board[self.x[1] + self.y[7]] = "BN1"
            self.board[self.x[6] + self.y[7]] = "BN1"
            # Rooks
            self.board[self.x[0] + self.y[0]] = "WR1"
            self.board[self.x[7] + self.y[0]] = "WR1"
            self.board[self.x[0] + self.y[7]] = "BR1"
            self.board[self.x[7] + self.y[7]] = "BR1"
            # Pawns
            for x in self.x:
                self.board[x + self.y[1]] = "WP0"
                self.board[x + self.y[6]] = "BP0"
        else:
            pass

    def get_board(self):
        return [] # a list containing all 32 pieces along with their current positions

    def get_piece(self, coordinates):
        return self.board[coordinates]

    def move_piece(self, beg_pos, end_pos):
        pass

    def get_available_moves(self, piece=None):
        pass

    def display_board(self):
        print("     a   b   c   d   e   f   g   h   ")
        print("    ___ ___ ___ ___ ___ ___ ___ ___  ")
        counter = 0
        for y in self.y:
            counter += 1
            print("", counter, end=" ")
            for x in self.x:
                print(f"|{self.board[x + y]}", end="")
            print("|")
        print("    --- --- --- --- --- --- --- ---   ")