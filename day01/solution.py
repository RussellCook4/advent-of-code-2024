from aocd import get_data
import os

session = os.getenv("SESSION_COOKIE")
data = get_data(day=1, year=2024, session=session)
print(data)

# split list into a using separator \n
# split each of those using blank space "  "

# Part 1 

data2 = data.split("\n")

print(data2)
list1 = []
list2 = []

for i in range(len(data2)):
        left, right = data2[i].split()
        list1.append(left)
        list2.append(right)

list1.sort()
list2.sort()

total = 0
for i in range(len(list1)):
    total = total + abs(int(list1[i]) - int(list2[i]))
print(total)

# Part 2

similarity_score = 0
for i in range(len(list1)):
    occurences = 0
    for j in range(len(list2)):
        if list1[i] == list2[j]:
            occurences = occurences + 1
    similarity_score += abs(int(list1[i]))*occurences
print(similarity_score)

# v2 - improving runtime with a dict

left_dict = {}
for i in range(len(list1)):
    if list1[i] in left_dict:
        left_dict[list1[i]] += 1
        print(left_dict)
    else:
        left_dict[list1[i]] = 1
similarity_score = 0
for i in range(len(list2)):
    if list2[i] in dict:
        similarity_score += abs(int(list2[i]))*dict[list2[i]]
print(similarity_score)

    



