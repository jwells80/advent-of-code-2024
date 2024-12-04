import re

results = []
total = 0
pattern = r"mul\(\d+,\d+\)|don't\(\)|do\(\)"
add = True

def mul(a, b):
    return a * b

with open("day3.txt", "r") as file:
    for line in file.readlines():
        results.extend(re.findall(pattern, line))

for result in results:
    print(result)
    print(re.match(r"do\(\)", result))
    if re.match(r"do\(\)", result):
        add = True
    elif re.match(r"don't\(\)", result):
        add = False
    elif re.match(r"mul\(\d+,\d+\)", result):
        if add:
            total += eval(result)

print(total)