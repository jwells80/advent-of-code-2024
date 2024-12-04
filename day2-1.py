count = 0

with open("day2.txt", "r") as file:
    for line in file.readlines():
        increasing = False
        decreasing = False
        valid = False
        line = [int(num) for num in line.split(" ")]
        for i in range(len(line) -1):
            if line[i] == line[i+1]:
                valid = False
                break
            if line[i] > line[i+1]: # 3 2
                valid = True if not increasing and line[i] - line[i+1] <= 3 else False
                if valid: decreasing = True
                if not valid: break
            if line[i] < line[i+1] :
                valid = True if not decreasing and line[i+1] - line[i] <= 3 else False
                if valid: increasing = True
                if not valid: break
        if valid: count += 1

print(count)