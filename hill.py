import random
import time

from board import Board


def make_move_steepest_hill(board):
    moves = {}
    for col in range(len(board)):
        best_move = board[col]

        for row in range(len(board)):
            if board[col] == row:
                # We don't need to evaluate the current
                # position, we already know the h-value
                continue

            board_copy = list(board)
            # Move the queen to the new row
            board_copy[col] = row
            moves[(col, row)] = board_copy.get_fitness()

    best_moves = []
    h_to_beat = board_copy.get_fitness()
    for k, v in moves.iteritems():
        if v < h_to_beat:
            h_to_beat = v

    for k, v in moves.iteritems():
        if v == h_to_beat:
            best_moves.append(k)

    # Pick a random best move
    if len(best_moves) > 0:
        pick = random.randint(0, len(best_moves) - 1)
        col = best_moves[pick][0]
        row = best_moves[pick][1]
        board[col] = row

    return board


start = time.time()

# body statement here
test = Board(5)
fitness = test.get_fitness()
result = make_move_steepest_hill(test)

# body end here
end = time.time()

print(f"Runtime of the program is {(end - start):.2f}")
result.show_map()
