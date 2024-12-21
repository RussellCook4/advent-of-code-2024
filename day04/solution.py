from aocd import get_data
import os
import json
import re

#load_dotenv()
session = os.getenv("SESSION_COOKIE")
data = get_data(day=4, year=2024, session=session)
print(data)

# Part 1

# Rules for valid XMAS:
# 1) XMAS in the correct order on the same line or col
# 2) XMAS backwards on the same line or col
# 3) XMAS on any diagnonal (x4)


data2 = data.split("\n")  # 140 x 140 array of strings

print(data2)

# let's iterate across all rows and cols and check!

XMASes = 0
for i in range(len(data2[0])):
    for j in range(len(data2)):
        # XMAS in rows or cols forwards or backwards:
        if (i<len(data2[0])-3) and data2[i][j] == "X" and data2[i+1][j] == "M" and data2[i+2][j] == "A" and data2[i+3][j] == "S":
            XMASes += 1
        if (i<len(data2[0])-3) and data2[i][j] == "S" and data2[i+1][j] == "A" and data2[i+2][j] == "M" and data2[i+3][j] == "X":
            XMASes += 1
        if (j<len(data2)-3) and data2[i][j] == "X" and data2[i][j+1] == "M" and data2[i][j+2] == "A" and data2[i][j+3] == "S":
            XMASes += 1
        if (j<len(data2)-3) and data2[i][j] == "S" and data2[i][j+1] == "A" and data2[i][j+2] == "M" and data2[i][j+3] == "X":
            XMASes += 1
        # XMAS in diagonals:
        if (i<len(data2[0])-3 and j<len(data2)-3) and data2[i][j] == "X" and data2[i+1][j+1] == "M" and data2[i+2][j+2] == "A" and data2[i+3][j+3] == "S":
            XMASes += 1
        if (i<len(data2[0])-3 and j<len(data2)-3) and data2[i][j] == "S" and data2[i+1][j+1] == "A" and data2[i+2][j+2] == "M" and data2[i+3][j+3] == "X":
            XMASes += 1
        if (i<len(data2[0])-3 and j>=3) and data2[i][j] == "X" and data2[i+1][j-1] == "M" and data2[i+2][j-2] == "A" and data2[i+3][j-3] == "S":
            XMASes += 1
        if (i<len(data2[0])-3 and j>=3) and data2[i][j] == "S" and data2[i+1][j-1] == "A" and data2[i+2][j-2] == "M" and data2[i+3][j-3] == "X":
            XMASes += 1
print(XMASes)

#Part 2 

# Rules for valid "X-MAS" 🫨: 
# MAS OR SAM in a diagonal
# MAS OR SAM in the opposite diagonal

MASXes = 0
for i in range(len(data2[0])-2):
    for j in range(len(data2)-2):
        if ((data2[i][j] == "M" and data2[i+1][j+1] == "A" and data2[i+2][j+2] == "S") \
        or ((data2[i][j] == "S" and data2[i+1][j+1] == "A" and data2[i+2][j+2] == "M"))) \
        and ((data2[i][j+2] == "M" and data2[i+1][j+1] == "A" and data2[i+2][j] == "S") \
        or ((data2[i][j+2] == "S" and data2[i+1][j+1] == "A" and data2[i+2][j] == "M"))):
            MASXes += 1

print(MASXes)




