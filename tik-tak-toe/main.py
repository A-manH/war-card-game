'''
    1.Create grid 3x3 grid 
        !-create list of ints through range 1-9
            !*each index represents spot on teh grid
            !*each sqaure is numbers +1 the square before it (square 1 is 1 square 2 is 2 and so on)
        -player plays the square they want by typing the square number
        -each square allows 2 values:
            *X , O

    2. Visualize grid
        -for loop: iterate through grid list 3 times creating a row on each iteration
            *for _ in range(3): for i in grid: print(grid[i[]])
        
    3. Design turn based mechinism
        -computer chooses random spot

        -player chooses spot
        
        
    4. Check if 3 consecutive moves have been made and declare winner
        -after each move fire function that checks if 3 conssecutive moves have been made 
            *iterate through list_grid, if 3 indxes have the same value (O or X) declare the winner
            *else other players turn
    5. Clear board and restart game
'''

from classes import Board, Player
import classes

board = Board()
player_1 = Player("Player1")
player_2 = Player("Player2")
board.visualize()

while True:
    player_1.play_move(board, player_2)