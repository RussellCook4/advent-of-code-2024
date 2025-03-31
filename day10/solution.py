from aocd import get_data
import os

session = os.getenv("SESSION_COOKIE")
data = get_data(day=10, year=2024, session=session)

print(data)

map_data = data.split("\n")

map_data = [list(map(int, row)) for row in map_data]

print(map_data)


#  any path that starts at h0, ends at h9, and increases by h1 left right up or down
# # Hiking trails never include diagonal steps

# trailheads are points at 0 that start valid hiking trials
# a trailhead's score is the number of unique endpoints of its hiking trails

def find_next_positions(current_position):
    i,j = current_position 
    next_positions = []
    if i < len(map_data) and  map_data[i+1][j] == map_data[i][j] + 1:
        next_positions.append((i+1,j))
    if i - 1 >= 0 and map_data[i-1][j] == map_data[i][j] + 1:
        next_positions.append((i-1,j))
    if j < len(map_data[0]) and map_data[i][j+1] == map_data[i][j] + 1:
        next_positions.append((i,j+1))
    if j - 1 >= 0 and map_data[i][j-1] == map_data[i][j] + 1:
        next_positions.append((i,j-1))
    return next_positions


def find_hiking_trails(current_position):
    i, j = current_position

    # Base case: If the current position is 9, return a set containing this endpoint
    if map_data[i][j] == 9:
        return {(i, j)}

    # Get all valid next positions
    next_positions = find_next_positions(current_position)

    # Collect unique endpoints
    unique_endpoints = set()
    for next_pos in next_positions:
        unique_endpoints.update(find_hiking_trails(next_pos))

    return unique_endpoints

trailheads = []
for i in range(len(map_data)):
    for j in range(len(map_data[0])):
        if map_data[i][j] == 0:  # Start positions
            endpoints = find_hiking_trails((i, j))
            trailheads.append(((i, j), len(endpoints))) 

trailhead_sum = 0
for i in trailheads:
    trailhead_sum += i[1]
trailhead_sum

print(trailheads)


# def find_hiking_trails(current_position, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(current_position)
#     next_positions = find_next_positions(map_data, current_position)
#     hiking_in_progress = True
#     current_position = start_position
#     endpoints = set()
#     while hiking_in_progress:
#         next_positions = find_next_positions(current_position)
#         if len(next_positions) == 0:
#             hiking_in_progress = False
#         endpoints.append([position for position in next_positions if map_data[position[0]][position[1]] == 9])
#         for position in next_positions:
#             current_position = position
#             find_hiking_trails(current_position)
#     return len(endpoints)

trailheads = []
for i in range(len(map_data)):
    for j in range(len(map_data[0])):
        if map_data[i][j] == 0:
            trailheads.append(((i,j),find_hiking_trails((i,j))))


