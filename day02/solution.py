from aocd import get_data
import os
import json

#load_dotenv()
session = os.getenv("SESSION_COOKIE")
data = get_data(day=2, year=2024, session=session)
print(data)

# Part 1

data2 = data.split("\n")
print(data2)

def convert_to_int_if_needed(array):
    # Check if all elements are already integers
    if all(isinstance(x, int) for x in array):
        return array  # Return as-is if they are already integers
    
    # Otherwise, check if they are strings that can be converted to integers
    if all(isinstance(x, str) and x.isdigit() for x in array):
        return [int(x) for x in array]  # Convert to integers
    
    # Raise an error if the array contains invalid elements
    raise ValueError("Array contains non-integer or non-convertible elements")

def safety(array):
    array = convert_to_int_if_needed(array)
    if len(array) == 1 or len(array) == 0:
        return 1
    increasing = (array[0] <= array[1])

    for i in range(1,len(array)):
        increasing_check = (array[i] >= array[i-1])
        if abs(array[i] - array[i-1]) > 3 or array[i] == array[i-1] or (increasing != increasing_check):
            return 0
    return 1
        
safe_reports = 0
for i in range(len(data2)):
    report = data2[i].split()
    safe_reports += safety(report)

print(safe_reports)

# Part 2
safe_reports_dampened = 0
for i in range(len(data2)):
    report = data2[i].split()
    if safety(report) == 1:
        safe_reports_dampened += 1
    else:
        any_dampened_safe = False
        for i in range(len(report)):
            report_removed = report[:i] + report[i+1:]
            if safety(report_removed) == 1:
                any_dampened_safe = True
                break
        if any_dampened_safe:
            safe_reports_dampened += 1
print(safe_reports_dampened)
