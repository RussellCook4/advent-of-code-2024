from aocd import get_data
import os

session = os.getenv("SESSION_COOKIE")
data = get_data(day=7, year=2024, session=session)

print(data)

# Part 1

equations = data.split("\n")

print(equations)
print(len(equations))   

total_calibration_result = 0
total_correct_equations = 0
for equation in equations:
    answer = int(equation.split(':')[0])
    numbers = [int(num) for num in equation.split(':')[1].split()]
    running_answers = [numbers[0]]
    for i in numbers[1:]:
        new_running_answers = [x + i for x in running_answers]
        new_running_answers.extend([x * i for x in running_answers])
        running_answers = list(set(new_running_answers))
    if answer in running_answers:
        print(equation)
        total_calibration_result += answer
        total_correct_equations += 1

print(total_calibration_result)
print(total_correct_equations)

# Part 2

calibration_result_2 = 0
correct_equations_2 = 0
for equation in equations:
    answer = int(equation.split(':')[0])
    numbers = [int(num) for num in equation.split(':')[1].split()]
    running_answers = [numbers[0]]
    for i in numbers[1:]:
        new_running_answers = [x + i for x in running_answers]
        new_running_answers.extend([x * i for x in running_answers])
        new_running_answers.extend(int(str(x)+str(i)) for x in running_answers)
        running_answers = list(set(new_running_answers))
    if answer in running_answers:
        calibration_result_2 += answer
        correct_equations_2 += 1
print(calibration_result_2)
print(correct_equations_2)


