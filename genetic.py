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
    # test.show_map()
    fitness.append(test.get_fitness())
    for i in range(len(test.map[row])):
        state += str(test.map[row].index(1))
        row += 1
    population.append(state)
    row = 0
    states += 1
    state = ""
print(population)
weight = []  # contains fitness function of current gen
for i in fitness:
    weight.append(i / (sum(fitness)))
print(weight)
# selection of pairs
weight.sort(reverse=True)
print(weight)
index = 0
selection = []
# while 0 in fitness:
for j in range(len(population)):
    r = random.random()
    if r < weight[0]:
        selection.append(population[0])
    elif r < sum(weight[:index + 2]):
        selection.append(population[1])
    elif r < sum(weight[:index + 3]):
        selection.append(population[2])
    elif r < sum(weight[:index + 4]):
        selection.append(population[3])
    elif r < sum(weight[:index + 5]):
        selection.append(population[4])
    elif r < sum(weight[:index + 6]):
        selection.append(population[5])
    elif r < sum(weight[:index + 7]):
        selection.append(population[6])
    else:
        selection.append(population[7])
# print("mating pairs: " + str(pairs))
# mates = [zip(population, selection)]
# print(tuple(mates[0]))
children = []  # holds children of crossed parents
for f, b in zip(population, selection):
    ran = random.randint(1, random.randint(1, len(population) - 1))
    children.append(f[:ran] + b[ran:])
print("Children are: " + str(children))
result_children = []
for location in children:
    child = location
    ran = random.randint(0, 4)  # value to insert
    loc_ran = random.randint(0, len(child) - 1)  # location where to insert value
    temp = list(child)
    temp[loc_ran] = ran
    result_children.append(''.join(map(str, temp)))
print("Mutated children: " + str(result_children))
# convert children into matrix
population.clear()  # clear population for next gen iteration
fitness.clear()
for value in result_children:
    matrix = Board(5)
    for dex in range(len(matrix.map)):
        for c in range(len(matrix.map[dex])):
            if matrix.map[dex][c] == 1:
                matrix.map[dex][c] = 0
        matrix.map[dex][int(value[dex])] = 1
    if matrix.get_fitness() == 0:
        goal = matrix
        break
    fitness.append(matrix.get_fitness())
# body end here
end = time.time() * 1000

print(f"Runtime of the program is {end - start:.2f}ms")
goal.show_map()
