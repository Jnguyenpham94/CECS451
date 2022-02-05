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
    distance = 0

    def __init__(self, name, data):
        self.name = name
        self.distance = data
        self.child = []


def add_node(name, data):
    new_node = Node(name, data)
    return new_node


try:
    map_text = open("map.txt").read()
    remove_chars = "-,()"
    for chars in remove_chars:
        map_text = map_text.replace(chars, " ")
    map_text = map_text.split()
    # TODO: need to parse map.txt into nodes
    for x in range(len(map_text)):
        distance = 0
        if map_text[x].isalpha():
            city = map_text[x]
        else:
            distance = float(map_text[x])

        city_map = Node(city, distance)

    print(map_text)
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
    # print(distance)
    # print(coordinates_text)
except FileNotFoundError:
    print("coordinates.txt Not Found")
    exit(2)


def main(args):
    start = args[0]  # starting city (SanFrancisco)
    end = args[1]  # ending city (LongBeach)
    straight_line = haversine(distance[start]["latitude"], distance[start]["longitude"], distance[end]["latitude"],
                              distance[end]["longitude"], )  # h(n)


if __name__ == '__main__':
    main(sys.argv[1:])
