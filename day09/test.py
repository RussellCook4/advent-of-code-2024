from aocd import get_data
import os

#load_dotenv()
session = os.getenv("SESSION_COOKIE")
data = get_data(day=9, year=2024, session=session)

def compactify(data):
    file_blocks = [int(data[i]) for i in range(len(data)) if i % 2 == 0]
    space_blocks = [int(data[i]) for i in range(len(data)) if i % 2 == 1]
    print(f"File blocks: {file_blocks}")

    file_storage = []
    for i in range(len(file_blocks)):
        file = file_blocks[i]
        if i < len(space_blocks):
            space = space_blocks[i]
        for j in range(file):
            file_storage.append(i)
        for k in range(space):
            file_storage.append(-1)
    
    print(f"File storage: {file_storage}")
    file_storage.count(-1)

    len(file_storage)
    working_file_storage = file_storage.copy()
    for i in range(30):
        working_file_storage.append(-1)
    compact_file_storage = []
    for i in range(len(working_file_storage)):
        print(f"Step: {i}")
        print(f"Working file storage: {working_file_storage}")
        print(f"Compact file storage: {compact_file_storage}")
        if working_file_storage[i] != -1:
            compact_file_storage.append(working_file_storage[i])
            working_file_storage[i] = -1
        else:
            compact_file_storage.append(max(working_file_storage))
            working_file_storage.remove(max(working_file_storage))
        if working_file_storage.count(-1) == 0 or working_file_storage.count(-1) == len(working_file_storage):
            break
    checksum = 0
    for i in range(len(compact_file_storage)):
        if compact_file_storage[i] != -1:
            checksum += compact_file_storage[i] * (i)
    print(checksum)
    return checksum

test_data = "2333133121414131402"
compactify(test_data)
