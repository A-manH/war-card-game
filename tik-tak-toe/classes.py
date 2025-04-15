grid = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
class Board():
    def __init__(self):
        pass
    def visualize(self):
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

    def update(self, square, move, player):
        grid[square] = move
        self.visualize()

    def reset():
        pass

class Player():
    def __init__(self):
        pass
    def play_move(move):
        pass