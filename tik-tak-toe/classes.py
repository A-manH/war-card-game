players = []
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

    def check_winner(self, player_1, player_2):
        solution_1 = playing_board[:3]
        solution_2 = playing_board[3:6]
        solution_3 = playing_board[6:9]
        horizontal_win = [solution_1, solution_2, solution_3]

        solution_4 = [i for i in range(0, 7, 3)]
        solution_5 = [i for i in range(1, 8, 3)]
        solution_6 = [i for i in range(2, 9, 3)]
        vertical_win = [solution_4, solution_5, solution_6]

        solution_7 = [i for i in range(0, 9, 4)]
        solution_8 = [i for i in range(2, 8, 2)]
        diagonal_win = [solution_4, solution_5, solution_6]

        for win in (horizontal_win, vertical_win, diagonal_win):
            for solution in win:
                if all(i == "X" for i in solution):
                    print("Solution found!")

                    if player_1.move == "X":

                elif all(i == "O" for i in solution):
                    print("Solution found!")

                else:
                    pass

    def reset(self):
        self.new_board()
        for p in players:
            #clear players self.move
            p.move = None

class Player():
    def __init__(self, name, move="X/O"):
        self.name = name
        self.move = None
        players.append(self)


    def play_move(self, opponent=None):
        square = int(input(f"{self.name}, pick a sqaure: "))
        while True:
            move = input(f"{self.name}, play {self.move or 'X/O'}: ").upper()

            if move == opponent.move:
                if opponent.move == "X":
                    print("Opponent is plaiying X, play O")
                else:
                    print("Opponent is playing O, play X")
            else:
                self.move = move
                Board().update(square, move)
                break