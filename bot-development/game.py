from board import Board


class Game:
    def __init__(self):
        self.board = Board()
        self.done = False

    def start_game_loop(self):
        while not self.done:
            self.board.display_board()
            self.get_move("White")
            self.board.display_board()
            self.get_move("Black")

    def get_move(self, player):
        valid = False
        usr_origin = "   "
        while not valid:
            usr_origin = input(f"{player}, which piece would you like to move? (x, y)\n> ")
            if len(usr_origin) == 2 and usr_origin[0] in self.board.x and usr_origin[1] in self.board.y:
                valid = True
            if not valid:
                print("Error: Invalid Coordinate please try again.")
        valid = False
        usr_destination = "   "
        while not valid:
            usr_destination = input(f"{player}, where would you like to move {self.board.get_piece(usr_origin)}? (x, y)\n> ")
            if len(usr_destination) == 2 and usr_destination[0] in self.board.x and usr_destination[1] in self.board.y:
                valid = True
            if not valid:
                print("Error: Invalid Coordinate please try again.")