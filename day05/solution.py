from aocd import get_data
import os

session = os.getenv("SESSION_COOKIE")
data = get_data(day=5, year=2024, session=session)
print(data)

print(data[-100:])
# Part 1

# rules :
# X|Y means that if both pages X and Y are to be produced for an update,
# page X must be printed at some point before page Y


ordering_rules = data.split("\n\n")[0].split("\n")
pages_to_update_string = data.split("\n\n")[1].split("\n")
print(pages_to_update_string)
pages_to_update = []
for i in pages_to_update_string:
    pages_to_update.append(i.split(","))
print(pages_to_update)

print(f"total updates: {len(pages_to_update)}")

# start by identifying which updates are already in the right order
# then add up the middle page number of those correctly-ordered updates

order_rule_dict = {}
for i in ordering_rules:
    left, right = i.split("|")
    if right in order_rule_dict:
        order_rule_dict[right].append(left)
    else:
        order_rule_dict[right] = [left]
print(order_rule_dict)
# these are the pages that must come before each page

def is_valid_update(update, ordering_rules_dict):
    for j in range(0,len(update)):
        for k in update[j:]:
            if update[j] in ordering_rules_dict and k in ordering_rules_dict[update[j]]:
                print(f"page {k} must come before page {i[j]}")
                return False
    return True



answer = 0
correct_updates = 0
for i in pages_to_update:
    print(i)
    if is_valid_update(i, order_rule_dict):
        print(is_valid_update(i, order_rule_dict))
        answer += int(i[len(i)//2])
        correct_updates += 1
print(answer)
print(correct_updates)

    
# Part 2

incorrect_updates = []
for i in pages_to_update:
    if not is_valid_update(i, order_rule_dict):
        incorrect_updates.append(i)

print(incorrect_updates)

def is_valid_position(position, update, ordering_rules_dict):
    for k in update[position:]:
        if update[position] in ordering_rules_dict and k in ordering_rules_dict[update[position]]:
            print(f"page {k} must come before page {i[position]}")
            return False
    return True

counter = 0
for idx in range(len(incorrect_updates)): 
    i = incorrect_updates[idx]  # Work with the actual list element
    while not is_valid_update(i, order_rule_dict):
        print(i)
        for j in range(len(i)):
            if not is_valid_position(j, i, order_rule_dict):
        
                i = i[:j] + i[j+1:] + [i[j]]
                print(i)
                counter += 1
        print(is_valid_update(i, order_rule_dict))
    incorrect_updates[idx] = i 
print(counter)

# learning here: 
# You're iterating over copies of elements from incorrect_updates if you write "for i in incorrect_updates:"", 
# so updating i won't alter the original list. Hence need to use loop over the index instead


answer2 = 0
correct_updates2 = 0
for i in incorrect_updates:
    print(i)
    if is_valid_update(i, order_rule_dict):
        print(is_valid_update(i, order_rule_dict))
        answer2 += int(i[len(i)//2])
        correct_updates2 += 1
print(answer2)
print(correct_updates2)


            
