# A∗ search
# ▪Idea: avoid expanding paths that are already expensive
# ▪Evaluation function 𝑓(𝑛) = 𝑔(𝑛) + ℎ(𝑛)
# ▪𝑔(𝑛) = cost so far to reach 𝑛
# ▪ℎ(𝑛) = estimated cost to goal from 𝑛
# ▪𝑓(𝑛) = estimated total cost of path through 𝑛 to goal
import collections
import math
import sys


# convert straight line distance between 2 points
def haversine(latitude1, longitude1, latitude2, longigude2):
    lat1 = math.radians(float(latitude1))
    long1 = math.radians(float(longitude1))
    lat2 = math.radians(float(latitude2))
    long2 = math.radians(float(longigude2))
    r = 3958.8  # miles
    d = 2 * r * math.asin(math.sqrt(math.sin((lat2 - lat1) / 2) ** 2) + math.cos(lat1) * math.cos(lat2) * math.sin(
        (long2 - long1) / 2) ** 2)
    return d


class Node:

    def __init__(self, name, data):
        self.name = name
        self.distance = data
        self.children = []

    def add_child(self, name, data):
        new_node = Node(name, data)
        self.children.append(new_node)


def isfloat(element):
    try:
        float(element)
        return True
    except ValueError:
        return False


# parsing the map.txt & coordinates.txt
try:
    list_map = []
    map_text = open("map.txt").read()
    # print(map_text)
    remove_chars = "-,()"
    for chars in remove_chars:
        map_text = map_text.replace(chars, " ")
    # print(map_text)
    map_text = map_text.splitlines()
    # print(map_text)
    for line in map_text:
        line = line.split()
        x = 0
        city_node = Node("empty", 0)
        count = 0
        while len(line) > 0:
            distance = 0.0
            if line[x].isalpha():
                city = line.pop(x)
                if isfloat(line[x]):
                    distance = float(line.pop(x))
            if count > 0:
                city_node.add_child(city, distance)
                count += 1
            else:
                city_node = Node(city, distance)
                count += 1
        list_map.append(city_node)
        count = 0
except FileNotFoundError:
    print("map.txt Not Found")
    exit(1)

# parse coordinates.txt to usable values in dictionary; city : latitude, longitude
try:
    coordinates_text = open("coordinates.txt").read()
    remove_chars = ":,\n()"
    for chars in remove_chars:
        coordinates_text = coordinates_text.replace(chars, " ")
    coordinates_text = coordinates_text.split()
    distance = collections.defaultdict(dict)
    index = 1
    for x in range(len(coordinates_text)):
        try:
            distance[coordinates_text[x]]["latitude"] = coordinates_text.pop(index)
            distance[coordinates_text[x]]["longitude"] = coordinates_text.pop(index)
            index += 1
        except IndexError:
            break
    print(distance)
    # print(coordinates_text)
except FileNotFoundError:
    print("coordinates.txt Not Found")
    exit(2)


def main(args):
    start = args[0]  # starting city (SanFrancisco)
    end = args[1]  # ending city (LongBeach)
    straight_line = haversine(distance[start]["latitude"], distance[start]["longitude"], distance[end]["latitude"],
                              distance[end]["longitude"], )  # h(n)
    # TODO: A* algo below
    # p = Node("SanFrancisco", 48.3)
    # p.add_child("Monterey", 71.7)
    # p.add_child("Fresno", 149)
    # for child in p.child:
    #     print(child.name + " " + str(child.distance))


if __name__ == '__main__':
    main(sys.argv[1:])
