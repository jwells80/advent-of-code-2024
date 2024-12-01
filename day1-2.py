column1, column2 = [], []
diff = 0
with open("day1.txt", "r") as file:
	for line in file.readlines():
		line_split = line.split("   ")
		column1.append(int(line_split[0]))
		column2.append(int(line_split[1]))

total = 0

for num in column1:
	count = column2.count(num)
	total += num * count

print(total)