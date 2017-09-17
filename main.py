import copy

boards = [
    [
        [0, 0, 0, 0, 0, 0, 0, 7, 8],
        [7, 5, 9, 8, 0, 2, 4, 6, 0],
        [0, 0, 0, 6, 7, 0, 5, 9, 0],
        [0, 3, 8, 0, 4, 0, 0, 0, 0],
        [6, 0, 0, 7, 0, 3, 0, 0, 9],
        [0, 0, 0, 0, 6, 0, 2, 3, 0],
        [0, 9, 3, 0, 8, 7, 0, 0, 0],
        [0, 4, 6, 5, 0, 1, 3, 8, 7],
        [8, 1, 0, 0, 0, 0, 0, 0, 0],
    ],
    [
        [0, 0, 0, 3, 5, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 1, 0, 6, 0, 7, 0, 5, 3],
        [0, 0, 4, 0, 0, 0, 0, 0, 1],
        [1, 0, 9, 0, 0, 5, 0, 6, 2],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 6, 0, 0, 7],
        [0, 0, 0, 7, 3, 0, 8, 2, 0],
        [0, 2, 0, 0, 0, 9, 0, 0, 0],
    ],
]

square_dict = {
    (0, 0): [(0, 0), (2, 2)],
    (0, 1): [(0, 3), (2, 5)],
    (0, 2): [(0, 6), (2, 8)],
    (1, 0): [(3, 0), (5, 2)],
    (1, 1): [(3, 3), (5, 5)],
    (1, 2): [(3, 6), (5, 8)],
    (2, 0): [(6, 0), (8, 2)],
    (2, 1): [(6, 3), (8, 5)],
    (2, 2): [(6, 6), (8, 8)],
}

all_candidates = set(range(1, 10))

for board in boards:
    loop_counter = 0
    print('\n\n\n*****     Starting Board     *****')
    for row in board:
        print(row)

    zero_on_board = 1
    for row in board:
        for cell in row:
            if cell == 0:
                zero_on_board = 1
                break

    number_of_iterations = 0

    dictionary_of_candidates = {}  # Dictionary to keep track of the possible candidates
    while zero_on_board:  # As long as there are any zeros on the board
        starting_board = copy.deepcopy(board)
        x = 0  # Reset the scan index for x
        while x <= 8:
            y = 0  # Reset the scan index for y
            while y <= 8:
                if board[y][x] == 0:  # If the current cell has not been confirmed

                    cell_now = (x, y)
                    row_to_scan, column_to_scan = cell_now

                    # take the mod 3 of x and y to determine which sub-square of 9 cells we are in
                    x_mod = int(x/3)
                    y_mod = int(y/3)
                    square_now = (x_mod, y_mod)
                    square_bounds = square_dict[square_now]  # Lookup the dictionary to determine the bounds of square
                    # Turn the bounds into a list of 9 coordinates to scan
                    x_square_range = range(square_bounds[0][0], 1 + square_bounds[1][0])
                    y_square_range = range(square_bounds[0][1], 1 + square_bounds[1][1])
                    square_list = [(x_sq, y_sq) for x_sq in x_square_range for y_sq in y_square_range]

                    set_of_numbers_intersecting = set()  # Reset the list of intersecting numbers

                    i = 0
                    while i <= 8:
                        set_of_numbers_intersecting.add(board[column_to_scan][i])
                        set_of_numbers_intersecting.add(board[i][row_to_scan])
                        set_of_numbers_intersecting.add(board[square_list[i][1]][square_list[i][0]])
                        i += 1

                    possible_candidates = all_candidates - set_of_numbers_intersecting
                    if len(possible_candidates) == 1:
                        print('Cell {}, {}: {}'.format(x, y, min(possible_candidates)))
                        board[y][x] = min(possible_candidates)

                    dictionary_of_candidates[cell_now] = possible_candidates

                y += 1
            x += 1

        no_zeros_on_board = 1
        for row in board:
            for cell in row:
                if cell == 0:
                    zero_on_board = 1
                    no_zeros_on_board = 0
                    break
        if no_zeros_on_board:
            zero_on_board = 0

        number_of_iterations += 1
        print('\n\nIteration #: {}'.format(number_of_iterations))
        for row in board:
            print(row)
        ending_board = copy.deepcopy(board)
        if ending_board == starting_board:
        #     loop_counter += 1
        # else:
        #     loop_counter = 0
        # if loop_counter == 2:
            zero_on_board = 0

        candidate_keys = sorted(dictionary_of_candidates.keys())
        for candidate_key in candidate_keys:
            print(candidate_key, dictionary_of_candidates[candidate_key])
