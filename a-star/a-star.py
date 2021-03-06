# Aβ search
# βͺIdea: avoid expanding paths that are already expensive
# βͺEvaluation function π(π) = π(π) + β(π)
# βͺπ(π) = cost so far to reach π
# βͺβ(π) = estimated cost to goal from π
# βͺπ(π) = estimated total cost of path through π to goal
import collections
import math
import sys


# convert straight line distance between 2 points using 2 sets of latitude & longitude values
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
        self.distance = data  # g value
        self.children = []
        self.f = 0
        self.h = 0

    def __repr__(self):
        rep = self.name
        return rep

    def add_child(self, name, data):
        new_node = Node(name, data)
        self.children.append(new_node)


def isfloat(element):
    try:
        float(element)
        return True
    except ValueError:
        return False


def recon_path(came, current):
    total = current
    while current in came.Keys:
        current = came[current]
        total.insert(current)
    return total


# parsing the map.txt & coordinates.txt
try:
    city_list = collections.defaultdict(dict)
    map_text = open("map.txt").read()
    remove_chars = "-,()"
    for chars in remove_chars:
        map_text = map_text.replace(chars, " ")
    map_text = map_text.splitlines()
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
        city_list[city_node.name] = city_node
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
except FileNotFoundError:
    print("coordinates.txt Not Found")
    exit(2)


def a_star(start, goal, straight_distance):
    global city_list
    f = collections.defaultdict(dict)
    h = straight_distance
    g = collections.defaultdict(dict)
    list_1 = collections.defaultdict(dict)
    cameFrom = collections.defaultdict(dict)

    #   find starting & end node in city list
    if start in city_list:
        begin = city_list[start]
    if goal in city_list:
        end = city_list[goal]
    end_node = city_list[end]

    traversal = [city_list[begin]]
    list_1[begin.name] = begin
    f[begin.name] = h
    g[begin.name] = city_list[start]
    #   TODO: implement the search
    while len(list_1) > 0:
        current = list_1[begin.name]

        if current.name == goal:  # TODO: pathing
            return recon_path(cameFrom, current)
        del list_1[current.name]
        for loc, child in enumerate(current.children):
            temp_g = g[current.name].distance + city_list.get(current.name).children[loc].distance
            if temp_g < g.get(current.name).children[loc].distance:  # TODO: ISSUE HERE!!
                cameFrom[child] = current.name
                g.get(current.name).children[loc] = temp_g
                f[current.name] = temp_g + haversine(distance[current.name]["latitude"],
                                                     distance[current.name]["longitude"],
                                                     distance[str(child)]["latitude"],
                                                     distance[str(child)]["longitude"])
                if child not in list_1:
                    list_1[child.name] = city_list.get(str(child))
    return "Failed to find path"


def main(args):
    start = args[0]  # starting city (SanFrancisco)
    end = args[1]  # ending city (LongBeach)
    straight_line = haversine(distance[start]["latitude"], distance[start]["longitude"], distance[end]["latitude"],
                              distance[end]["longitude"], )  # h(n)

    # print(city_list.get("SanFrancisco").children[0].distance)
    stuff = a_star(start, end, straight_line)
    print("From city: " + start)
    print("To city: " + end)
    print("Best Route: ")
    print("Total distance: " + stuff)


if __name__ == '__main__':
    main(sys.argv[1:])
