from aocd import get_data
import os
import json
import re

#load_dotenv()
session = os.getenv("SESSION_COOKIE")
data = get_data(day=4, year=2024, session=session)
print(data)

# Part 1