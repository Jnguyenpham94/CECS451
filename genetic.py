import time
import random
from board import Board

start = time.time() * 1000

# body statement here
fitness = []  # fitnesses of states
row = 0
state = ""
states = 0
population = []  # pop of states
while states < 8:
    test = Board(5)
    fitness.append(test.get_fitness())
    for i in range(len(test.map[row])):
        state += str(test.map[row].index(1))
        row += 1
    population.append(state)
    row = 0
    states += 1
    state = ""
print(population)
print(fitness)
# while fitness > 0:
#     print("FITNESS")

# body end here
end = time.time() * 1000

print(f"Runtime of the program is {end - start:.2f}ms")
test.show_map()
