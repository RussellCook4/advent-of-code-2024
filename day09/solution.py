from aocd import get_data
import os

session = os.getenv("SESSION_COOKIE")
data = get_data(day=9, year=2024, session=session)

print(data)

file_blocks = [int(data[i]) for i in range(len(data)) if i % 2 == 0]
space_blocks = [int(data[i]) for i in range(len(data)) if i % 2 == 1]
print(len(file_blocks))
print(len(space_blocks))
print(len(data))

file_storage = []
total_file_blocks = 0
total_spaces = 0
for i in range(len(file_blocks)):
    file = file_blocks[i]
    total_file_blocks += file
    space = space_blocks[i]
    total_spaces += space
    for j in range(file):
        file_storage.append(i)
    for k in range(space):
        file_storage.append(-1)

print(file_storage)
file_storage.count(-1)

len(file_storage)

working_file_storage = file_storage.copy()
compact_file_storage = []
for i in range(len(working_file_storage)):
    if i%1000==0:
        print(f"Step: {i}")
    if working_file_storage[i] != -1:
        compact_file_storage.append(working_file_storage[i])
        working_file_storage[i] = -1
    else:
        compact_file_storage.append(max(working_file_storage))
        working_file_storage.remove(max(working_file_storage))
    if working_file_storage.count(-1) == 0:
        break

checksum = 0
for i in range(len(compact_file_storage)):
    if compact_file_storage[i] != -1:
        checksum += compact_file_storage[i] * (i)
print(checksum)

print(compact_file_storage)

compact_file_storage.remove(-1)

spaces_removed = [i for i in compact_file_storage if i!=-1]

spaces_removed

total_file_blocks
total_spaces

len(compact_file_storage)
print(working_file_storage[0:100])