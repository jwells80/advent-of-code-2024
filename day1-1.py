column1, column2 = [], []
diff = 0
with open("day1.txt", "r") as file:
	for line in file.readlines():
		line_split = line.split("   ")
		column1.append(int(line_split[0]))
		column2.append(int(line_split[1]))

column1.sort()
column2.sort()

for i in range(len(column1)):
	if column1[i] > column2[i]:
		diff += column1[i] - column2[i]
	else:
		diff += column2[i] - column1[i]
print(diff)