solution_1 = [i for i in range(3)]
        solution_2 = [i for i in range(3, 6)]
        solution_3 = [i for i in range(6, 9)]
        horizontal_win = [solution_1, solution_2, solution_3]

        solution_4 = [i for i in range(0, 7, 3)]
        solution_5 = [i for i in range(1, 8, 3)]
        solution_6 = [i for i in range(2, 9, 3)]
        vertical_win = [solution_4, solution_5, solution_6]

        print(*(horizontal_win+vertical_win))