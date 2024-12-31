from aocd import get_data
import os

#load_dotenv()
session = os.getenv("SESSION_COOKIE")
data = get_data(day=6, year=2024, session=session)

# Part 1
map_data = data.split("\n")

# find starting location

for i in range(len(map_data)): # rows
    for j in range(len(map_data[i])): # cols
        if map_data[i][j] == "^":
            start = (i,j)
            break
print(start)

def next_pos_oob(current_position, direction, map):
    x, y = current_position
    if direction == "up" and x == 0:
        return True
    elif direction == "down" and x == len(map)-1:
        return True
    elif direction == "left" and y == 0:
        return True
    elif direction == "right" and y == len(map[0])-1:
        return True
    return False


visited_locations = [start]
current_position = start
direction = "up"

while True:
    if next_pos_oob(current_position, direction,map_data):
        break
    x, y = current_position
    if direction == "up": 
        if map_data[x-1][y] == ".":
            current_position = (x-1,y)
            if current_position not in visited_locations:
                visited_locations.append(current_position)
        elif map_data[x-1][y] == "#":
                direction = "right"
    elif direction == "right":
        if map_data[x][y+1] == ".":
            current_position = (x,y+1)
            if current_position not in visited_locations:
                visited_locations.append(current_position)
        elif map_data[x][y+1] == "#":
                direction = "down"
    elif direction == "down":
        if map_data[x+1][y] == ".":
            current_position = (x+1,y)
            if current_position not in visited_locations:
                visited_locations.append(current_position)
        elif map_data[x+1][y] == "#":
                direction = "left"
    elif direction == "left":
        if map_data[x][y-1] == ".":
            current_position = (x,y-1)
            if current_position not in visited_locations:
                visited_locations.append(current_position)
        elif map_data[x][y-1] == "#":
                direction = "up"

print(len(visited_locations))

# Part 2

def is_a_loop(start_pos, start_direction,map):
    visited = set()
    current_position = (start_pos[0], start_pos[1], start_direction)
    max_iterations = 10000000
    iterations = 0
    while iterations < max_iterations:
        iterations += 1
        x,y,dir = current_position
        if next_pos_oob((x,y), dir,map):
            return False
        if dir == "up": 
            if map[x-1][y] == "." or map[x-1][y] == "^":
                current_position = (x-1,y,"up")
            elif map[x-1][y] == "#":
                current_position = (x, y, "right")
        elif dir == "right":
            if map[x][y+1] == "." or map[x][y+1] == "^":
                current_position = (x, y+1, "right")
            elif map[x][y+1] == "#":
                current_position = (x, y, "down")
        elif dir == "down":
            if map[x+1][y] == "." or map[x+1][y] == "^":
                current_position = (x+1,y,"down")
            elif map[x+1][y] == "#":
                current_position = (x, y, "left")
        elif dir == "left":
            if map[x][y-1] == "." or map[x][y-1] == "^":
                current_position = (x,y-1,"left")
            elif map[x][y-1] == "#":
                current_position = (x, y, "up")
        if current_position in visited:
            return True
        visited.add(current_position)
    return False


positions = 0

for i, j in visited_locations:
    print(f"i: {i}, j: {j}")
    if map_data[i][j] == ".":
        # Create a deep copy of the map
        new_map = [row[:] for row in map_data]  # Alternative: copy.deepcopy(map_data)
        new_map[i] = new_map[i][:j] + "#" + new_map[i][j+1:]

        # Check for loops
        if is_a_loop(start, "up", new_map):
            positions += 1
            print(f"Loop found! Total loops: {positions}")
