import re

results = []
total = 0
regex = r"mul\(\d+,\d+\)"

def mul(a, b):
    return a * b

with open("day3.txt", "r") as file:
    for line in file.readlines():
        results.extend(re.findall(regex, line))

for result in results:
    total += eval(result)

print(total)