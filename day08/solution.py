from aocd import get_data
import os
from math import gcd

#load_dotenv()
session = os.getenv("SESSION_COOKIE")
data = get_data(day=8, year=2024, session=session)

print(data)

# Part 1

map = data.split("\n")
print(map)
print(len(map))
print(len(map[0]))

frequencies = set()
for i in range(len(map)): 
    for j in range(len(map[i])):
        if map[i][j] != ".":
            frequencies.add(map[i][j])

print(frequencies)

antinodes = set()
for f in frequencies:
    locations = []
    for row in range(len(map)):
        l = map[row].find(f)
        if l != -1:
            locations.append((row,l))
    print(locations)
    for x in locations:
        for y in locations:
            if x != y:
                # x - y is vector from y to x
                # so 2x - y is potential antinode as it's another (x-y) away from x 
                d1 = (2*x[0]-y[0], 2*x[1]-y[1])
                d2 = (2*y[0]-x[0], 2*y[1]-x[1])
                if d1[0] >= 0 and d1[0] < len(map) and d1[1] >= 0 and d1[1] < len(map[0]):
                    antinodes.add(d1)
                    print(f"Successful frequency: {f}")
                if d2[0] >= 0 and d2[0] < len(map) and d2[1] >= 0 and d2[1] < len(map[0]):
                    antinodes.add(d2)
print(len(antinodes))

# Part 2

def is_within_map(x, y, map):
    return (
        0 <= round(x) < len(map) and
        0 <= round(y) < len(map[0])
    )

harmonic_anti_nodes = set()
for f in frequencies:
    locations = []
    for row in range(len(map)):
        l = map[row].find(f)
        if l != -1:
            locations.append((row,l))
    for n in locations:
        for m in locations:
            if n != m:
                dx, dy = n[0] - m[0], n[1] - m[1]
                magnitude = gcd(dx, dy)
                d = (dx / magnitude, dy / magnitude)
                for i in range(1, int(((len(map)**2 + len(map[0])**2)**0.5)//1)+1):
                    x1, y1 = i*d[0] + n[0], i*d[1] + n[1]
                    x2, y2 = i*-d[0] + m[0], i*-d[1] + m[1]
                    if is_within_map(x1, y1, map):
                        harmonic_anti_nodes.add((x1, y1))
                    if is_within_map(x2, y2, map):
                        harmonic_anti_nodes.add((x2, y2))
    if len(locations) >= 2:
        for l in locations:
            harmonic_anti_nodes.add(l)
print(len(harmonic_anti_nodes))
