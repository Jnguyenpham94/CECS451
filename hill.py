
import time
from board import Board


def hill(board):
    # body statement here
    count = 0  # loop 5 times then restart board
    n = 5
    fitness = board.get_fitness()
    h = [0] * n  # fitness of potential board
    current_fit = fitness
    while fitness != 0:
        for i in range(len(board.map)):
            for j in range(len(board.map[i])):
                board.map[i] = [0] * n
                board.map[i][j] = 1
                h[j] = board.get_fitness()
                board.map[i][j] = 0
            min_h = min(h)
            min_index = h.index(min_h)
            board.map[i][min_index] = 1
            fitness = board.get_fitness()
        count += 1
        #  if after 5 loops to bottom row restart with fresh board
        if count == 5:
            count = 0
            board = Board(5)  # restart with fresh board
    return board

    # body end here


def main():
    start = time.time() * 1000
    test = Board(5)
    test = hill(test)
    end = time.time() * 1000
    # fitness = test.get_fitness()
    # print(fitness)
    print(f"Runtime of the program is {(end - start):.2f}ms")
    test.show_map()


if __name__ == '__main__':
    main()
