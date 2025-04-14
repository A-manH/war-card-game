class Board():
    def visualize():
        grid = [1, 2, 3, 4, 5, 6, 7, 8, 9]
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

    def add_move():
        pass
    
    def reset():
        pass

class Player():
    def play_move(move):
        pass