class Board():
    def __init__(self):
        self.players = []
        self.grid = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.playing_board = self.grid.copy()
        
    def visualize(self):
        counter = 0

        for row in range(3):
            if row in range(3):
                print("-------------")

            for i in range(3):
                print(f"| {self.playing_board[counter]} ", end="")
                counter += 1
                if i == 2:
                    print("|", end="")

            if row == 2:
                print("\n-------------")
            print()

    def check_winner(self, player, opponenet):
        solution_1 = self.playing_board[:3]
        solution_2 = self.playing_board[3:6]
        solution_3 = self.playing_board[6:9]
        horizontal_win = [solution_1, solution_2, solution_3]

        solution_4 = self.playing_board[:7:3]
        solution_5 = self.playing_board[1:8:3]
        solution_6 = self.playing_board[2:9:3]
        vertical_win = [solution_4, solution_5, solution_6]

        solution_7 = self.playing_board[:9:4]
        solution_8 = self.playing_board[2:7:2]
        diagonal_win = [solution_7, solution_8]

        for win in (horizontal_win, vertical_win, diagonal_win):
            for solution in win:
                if all(i == "X" for i in solution):
                    if player.move == "X":
                        player.score += 1
                        print(f"Solution found! Winner is {player.name}!")
                        print(f"Score is: {player.score} - {opponenet.score}")
                        self.reset()
                elif all(i == "O" for i in solution):
                        player.score += 1
                        self.reset()
                        print(f"Solution found! Winner is {player.name}!")
                        print(f"\tScore is: {player.score} - {opponenet.score}")

    def reset(self):
        self.new_board()
        for player in self.players:
            player.move = None

    def new_board(self):
        self.playing_board = self.grid.copy()

    def update(self, square, move):
        self.playing_board[square] = move

class Player():
    def __init__(self, name, move="X/O"):
        self.name = name
        self.move = None
        self.score = 0

    def play_move(self, board, opponent):
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
                board.update(square, move)
                break