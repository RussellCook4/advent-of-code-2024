from aocd import get_data
import os

session = os.getenv("SESSION_COOKIE")
data = get_data(day=9, year=2024, session=session)

# Part 1

file_blocks = [int(data[i]) for i in range(len(data)) if i % 2 == 0]
space_blocks = [int(data[i]) for i in range(len(data)) if i % 2 == 1]

file_storage = []
for i,file in enumerate(file_blocks):
    file_storage.extend([i] * file)
    if i < len(space_blocks):
        file_storage.extend([-1] * space_blocks[i])

working_file_storage = file_storage.copy()
compact_file_storage = []
i=0
while len(working_file_storage) > 0 and len(working_file_storage) != working_file_storage.count(-1):
    current_val = working_file_storage.pop(0)
    if current_val != -1:
        compact_file_storage.append(current_val)
    elif any(x!= -1 for x in working_file_storage):
            max_file = max([x for x in working_file_storage if x != -1])
            compact_file_storage.append(max_file)
            working_file_storage.remove(max_file)
    i += 1
    if i % 10000 == 0:
        print(f"Step {i}: Working storage size = {len(working_file_storage)}, Compact storage size = {len(compact_file_storage)}")

checksum = 0
for i in range(len(compact_file_storage)):
    checksum += compact_file_storage[i] * (i)
print(checksum)

# Part 2

#
len(file_blocks)
len(space_blocks)

file_storage_new =[[int(data[i]), int(i/2) if i % 2 == 0 else -1] for i in range(len(data))]

for i in range(len(file_storage_new)):
    j = len(file_storage_new)-i-1
    if file_storage_new[j][1] != -1:
        for k in range(j): #adding new things will mess with the range
            if file_storage_new[k][1] == -1 and file_storage_new[k][0] >= file_storage_new[j][0]:
                file_storage_new
                
                file_storage_new[j], file_storage_new[k] = file_storage_new[k], file_storage_new[j]
                break


working_file_storage = file_storage.copy()
whole_compact_storage = []

while len(working_file_storage) > 0 and len(working_file_storage) != working_file_storage.count(-1):
    current_val = working_file_storage.pop(0)
    if current_val != -1:
        whole_compact_storage.append(current_val)
    elif any(x!= -1 for x in working_file_storage):
            max_file = max([x for x in working_file_storage if x != -1])
            whole_compact_storage.append(max_file)
            working_file_storage.remove(max_file)






used_files = [False] * len(file_blocks)
whole_compact_storage = []
for i,file in enumerate(file_blocks):
    whole_compact_storage.extend([i] * file)
    if i < len(space_blocks):
        space = space_blocks[i]
        while space > 0:
            moved_file = False
            for j, moving_file in enumerate(reversed(file_blocks)):
                if moving_file <= space and not used_files[j]:
                    whole_compact_storage.extend([len(file_blocks)-j-1] * moving_file)
                    space -= moving_file
                    used_files[j] = True
                    moved_file = True
            if not moved_file:
                break
checksum2 = 0
for i in range(len(whole_compact_storage)):
    checksum2 += whole_compact_storage[i] * (i)

print(checksum2)
whole_compact_storage[-100:]

file_storage[0:100]
file_storage[-100:]

file_blocks = file_blocks[0:10]
space_blocks = space_blocks[0:10]

used_files = [False] * len(file_blocks)
whole_compact_storage = []


for i, file in enumerate(file_blocks):
    # Add the current file to compact storage
    whole_compact_storage.extend([i] * file)
    print(f"Adding {file} of file {i} to compact storage")
    if i < len(space_blocks):
        space = space_blocks[i]
        
        while space > 0:
            moved_file = False
            
            # Iterate over file_blocks in reverse
            for j in range(len(file_blocks) - 1, -1, -1):
                moving_file = file_blocks[j]
                if moving_file <= space and not used_files[j]:
                    # Move the file to compact storage
                    print(f"Moving {moving_file} of file {j} to compact storage")
                    whole_compact_storage.extend([j] * moving_file)
                    space -= moving_file
                    used_files[j] = True
                    moved_file = True
                    break  # Stop checking after moving one file
            
            # If no file fits, stop trying to fill the space
            if not moved_file:
                break

# Calculate checksum
checksum2 = 0
for i in range(len(whole_compact_storage)):
    checksum2 += whole_compact_storage[i] * i

print(checksum2)


print(whole_compact_storage)
print(file_blocks)
print(space_blocks)



whole_compact_storage = []
for i, file in enumerate(file_blocks):
    whole_compact_storage.extend([i] * file)
    if i < len(space_blocks):
        whole_compact_storage.extend([-1] * space_blocks[i])

# Process files in decreasing order of file ID
for file_id in range(len(file_blocks) - 1, -1, -1):
    file_size = file_blocks[file_id]
    # Look for the leftmost span of free space blocks that can fit the file
    for start in range(len(whole_compact_storage)):
        # Check if this span can fit the file
        if all(whole_compact_storage[start + k] == -1 for k in range(file_size) if start + k < len(whole_compact_storage)):
            # Ensure the file is currently not already in the leftmost position
            if file_id in whole_compact_storage[start:start + file_size]:
                break  # File is already here
            # Move the file to this span
            for _ in range(file_size):
                whole_compact_storage[start] = file_id
                start += 1
            # Remove the file from its previous location
            for idx in range(len(whole_compact_storage)):
                if whole_compact_storage[idx] == file_id:
                    whole_compact_storage[idx] = 1
                    continue

checksum2 = 0
for i in range(len(whole_compact_storage)):
    if i != -1:
        checksum2 += whole_compact_storage[i] * i
print(checksum2)