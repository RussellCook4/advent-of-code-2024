from aocd import get_data
import os
import json
import re

#load_dotenv()
session = os.getenv("SESSION_COOKIE")
data = get_data(day=3, year=2024, session=session)
print(data)

# Part 1


def find_muls(s):
    matches = re.findall(r"mul\(.*?\)", s, re.DOTALL)
    valid_muls = []
    for i in matches:
        if "," in i:
            if i[4:-1].split(",")[0].isdigit() and i[4:-1].split(",")[1].isdigit():
                valid_muls.append([int(i[4:-1].split(",")[0]),int(i[4:-1].split(",")[1])])
                print([int(i[4:-1].split(",")[0]),int(i[4:-1].split(",")[1])])
            else: 
                nested_muls = find_muls(i[4:])
                valid_muls.extend(nested_muls)
    return valid_muls

print(find_muls(data))

total = 0
for muls in find_muls(data):
    total += muls[0]*muls[1]
print(total)

# Part 2

# need to do the above but get the actual locations this time

def find_mul_locations(s, offset=0):
    mul_locations_iterable = re.finditer(r"mul\(.*?\)", s, re.DOTALL)
    mul_locations =  [(mul.start() + offset,mul.end() + offset) for mul in mul_locations_iterable] # an array of start and end location pairs (x,y) of the potential muls
    valid_mul_locations = []
    for (start, end) in mul_locations:
        local_start = start - offset 
        local_end   = end - offset
        potential_mul = s[local_start : local_end]
        if "," in potential_mul:
            parts = potential_mul[4:-1].split(",")
            if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                valid_mul_locations.append((start, end))
                print(f"VALID direct mul: {potential_mul} => appended location {(start, end)}")
            else: 
                nested_muls = find_mul_locations(potential_mul[4:], start+4)
                valid_mul_locations.extend(nested_muls)
    return valid_mul_locations

find_mul_locations(data)

# get the locations of all the "mul" functions and search for most recent do/dont

def find_conditional_muls(s):
    muls = find_muls(s)
    do_locations = re.finditer(r"do\(\)", s, re.DOTALL)
    dont_locations = re.finditer(r"don't\(\)", s, re.DOTALL)
   
    mul_locations = find_mul_locations(s)  
    do_locations = [do.span() for do in do_locations] 
    dont_locations = [dont.span() for dont in dont_locations]
    # these are arrays of tuples (x,y) of start and end locations of the muls/dos/donts

    valid_results = []
    for i in range(len(muls)):
        # find the closest do or don't to the left of the mul
        closest_do = max((x[0] for x in do_locations if x[0] < mul_locations[i][0]), default=None) # just take the start locations
        closest_dont = max((x[0] for x in dont_locations if x[0] < mul_locations[i][0]), default=None)
        print(f"mul: {muls[i]}, location: {mul_locations[i]}")
        print(f"closest do: {closest_do}, closest dont: {closest_dont}")
        if closest_dont is None:
            print("enabled!")
            valid_results.append(muls[i])
        elif closest_do is None or (closest_do is not None and closest_do > closest_dont):
            print("enabled!")
            valid_results.append(muls[i])
        else: print("not enabled!")
    print(len(muls) == len(mul_locations))
    print(len(valid_results))
    return valid_results

find_conditional_muls(data)

total_part2 = 0
for muls in find_conditional_muls(data.replace("\n", "")):
    total_part2 += muls[0]*muls[1]
print(total_part2)
