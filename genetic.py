import time
import random
from board import Board

goal = []
fitness = []
population = []
found = False


def genetic():
    global goal
    global fitness  # fitnesses of states
    global found
    row = 0
    state = ""
    states = 0
    global population  # pop of states
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
    weight = []  # contains fitness function of current gen
    for i in fitness:
        weight.append(i / (sum(fitness)))
    # selection of pairs
    weight.sort(reverse=True)  # descending order weights
    index = 0
    selection = []
    for j in range(len(population)):
        r = random.random()
        if r < weight[0]:
            selection.append(population[0])
        elif r < sum(weight[:2]):
            selection.append(population[1])
        elif r < sum(weight[:3]):
            selection.append(population[2])
        elif r < sum(weight[:4]):
            selection.append(population[3])
        elif r < sum(weight[:5]):
            selection.append(population[4])
        elif r < sum(weight[:6]):
            selection.append(population[5])
        elif r < sum(weight[:7]):
            selection.append(population[6])
        else:
            selection.append(population[7])
    children = []  # holds children of crossed parents
    # crossing of the pairs
    for f, b in zip(population, selection):
        ran = random.randint(1, random.randint(1, len(population) - 1))
        children.append(f[:ran] + b[ran:])
    result_children = []
    for location in children:
        child = location
        ran = random.randint(0, 4)  # value to insert
        loc_ran = random.randint(0, len(child) - 1)  # location where to insert value
        temp = list(child)
        temp[loc_ran] = ran
        result_children.append(''.join(map(str, temp)))
    population.clear()  # clear population for next gen iteration
    fitness.clear()
    population = children
    for value in result_children:
        matrix = Board(5)
        for dex in range(len(matrix.map)):
            for c in range(len(matrix.map[dex])):
                if matrix.map[dex][c] == 1:
                    matrix.map[dex][c] = 0
            matrix.map[dex][int(value[dex])] = 1
        if matrix.get_fitness() == 0:
            goal = matrix
            found = True
            break
        fitness.append(matrix.get_fitness())


def main():
    start = time.time() * 1000
    while not found:
        genetic()
    end = time.time() * 1000
    print(f"Runtime of the program is {end - start:.2f}ms")
    # print(goal.get_fitness())
    goal.show_map()


if __name__ == '__main__':
    main()
