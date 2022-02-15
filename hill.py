import time

from board import Board

start = time.time()

# body statement here
test = Board(5)
fitness = test.get_fitness()
print("FITNESS: " + str(test.get_fitness()))
while fitness > 0:
    print("FITNESS")

# body end here
end = time.time()

print(f"Runtime of the program is {(end - start):.2f}")
test.show_map()
