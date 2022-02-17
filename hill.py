import random
import time

import numpy as np

from board import Board

start = time.time()

# body statement here
test = Board(5)
fitness = test.get_fitness()
current_fit = fitness
# for i in test.map[0]:
#     print(i)
while fitness > 0:
    row = 0
    for col, value in enumerate(test.map[row]):
        if value == 1:
            current_loc = col
            change_loc = 0
            while fitness >= current_fit:
                test.map[row][current_loc] = 0
                test.map[row][change_loc] = 1
                current_fit = test.get_fitness()
                if current_fit < fitness:
                    fitness = current_fit
                    row += 1
                else:
                    change_loc += 1
# result = make_move_steepest_hill(test)

# body end here
end = time.time()

print(f"Runtime of the program is {(end - start):.2f}")
# result.show_map()
