# A∗ search
# ▪Idea: avoid expanding paths that are already expensive
# ▪Evaluation function 𝑓(𝑛) = 𝑔(𝑛) + ℎ(𝑛)
# ▪𝑔(𝑛) = cost so far to reach 𝑛
# ▪ℎ(𝑛) = estimated cost to goal from 𝑛
# ▪𝑓(𝑛) = estimated total cost of path through 𝑛 to goal
import math


# convert straight line distance between 2 points
def haversine(deg1, deg2):
    lat1 = math.radians(float(deg1))
    lat2 = math.radians(float(deg2))
    r = 3958.8  # miles
    d = 2 * r * math.asin(math.sqrt(math.sin((lat2 - lat1) / 2) ** 2) + math.cos(lat1) * math.cos(lat2) * math.sin(
        (lat2 - lat1) / 2) ** 2)
    # print(lat1)
    # print(lat2)
    # print(d)
    return d


try:
    map_text = open("map.txt").read().strip()
# print(map_text)
except FileNotFoundError:
    print("File Not Found")
    exit(1)

# parse coordinates.txt to usable values
try:
    coordinates_text = open("coordinates.txt").read()
    remove_chars = ":,\n()"
    for chars in remove_chars:
        coordinates_text = coordinates_text.replace(chars, " ")
    coordinates_text = coordinates_text.split()
    distance = {}
    latitude = 1
    for x in range(len(coordinates_text)):
        try:
            distance[coordinates_text[x]] = haversine(coordinates_text.pop(latitude), coordinates_text.pop(latitude))
            latitude += 1
        except IndexError:
            break
    print(distance)
    # print(coordinates_text)
except FileNotFoundError:
    print("File Not Found")
    exit(1)

with open('map.txt') as f:
    map_text = f.readlines()

with open('coordinates.txt') as f:
    coordinates = f.readlines()

# print(map_text)
# print(coordinates)

# haversine(37.38305013, -121.8734782)
