grid = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
playing_board = grid.copy()
class Board():
    def __init__(self):
        pass
    
    def new_board(self):
        counter = 0

        for row in range(3):
            if row in range(3):
                print("-------------")

            for i in range(3):
                print(f"| {grid[counter]} ", end="")
                counter += 1
                if i == 2:
                    print("|", end="")
                    
            if row == 2:
                print("\n-------------")
            print()

    def visualize(self):
        counter = 0

        for row in range(3):
            if row in range(3):
                print("-------------")

            for i in range(3):
                print(f"| {playing_board[counter]} ", end="")
                counter += 1
                if i == 2:
                    print("|", end="")
                    
            if row == 2:
                print("\n-------------")
            print()

    def update(self, square, move):
        playing_board[square] = move
        self.visualize()

    def check_winner():
        pass

    def reset(self):
        self.new_board()

class Player():
    def __init__(self, name, move = "X/O"):
        self.name = name
        self.move = move
        self.score = 0
        
    def play_move(self, opponent=None):
        while True:
            square = int(input("Pick a sqaure: "))
            move = input(f"{self.name}, play {self.move}: ").upper()

            if move == opponent.move:
                if opponent.move == "X":
                    print("Opponent is plaiying X, play O")
                else:
                    print("Opponent is playing O, play X")
            else:
                self.move = move
                Board().update(square, move)
                break