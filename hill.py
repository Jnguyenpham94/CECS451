
import time
from board import Board


def hill(board, n_queens):
    # count = 0  # how many restarts occurred
    n = n_queens
    fitness = board.get_fitness()
    h = [0] * n  # fitness of potential board
    while fitness != 0:
        for i in range(len(board.map)):
            for j in range(len(board.map[i])):
                board.map[i] = [0] * n  # remove any 1s in that row
                board.map[i][j] = 1
                h[j] = board.get_fitness()
                board.map[i][j] = 0
            min_h = min(h)
            min_index = h.index(min_h)
            board.map[i][min_index] = 1
            fitness = board.get_fitness()
        # count += 1
        board = Board(n)  # restart with fresh board
    # print("count: " + str(count))
    return board


def main():
    start = time.time() * 1000  # times 1000 for ms
    n = 5  # CHANGE ME for more or less queens
    test = Board(n)
    test = hill(test, n)
    end = time.time() * 1000
    # fitness = test.get_fitness()
    # print(fitness)
    print(f"Runtime of the program is {(end - start):.2f}ms")
    test.show_map()


if __name__ == '__main__':
    main()