count = 0

def check_decreasing(num1, num2):
    if num1 > num2:
        return True if num1 - num2 <= 3 else False

    
def check_increasing(num1, num2):
    if num1 < num2:
        return True if num2 - num1 >= 3 else False 

with open("day2.txt", "r") as file:
    for line in file.readlines():
        increasing = False
        decreasing = False
        valid = False
        line = [int(num) for num in line.split(" ")]
        for i in range(len(line) -1):
            if line[i] == line[i+1]:
                if line[i] == [i+2]:
                    valid = False
                    break
                if not valid:
                    decreasing = check_decreasing(line[i], line[i+2])
                    increasing = check_increasing(line[i], line[i+2])
            if line[i] > line[i+1]:
                valid += True if not increasing and line[i] - line[i+1] <= 3 else False
                if valid: decreasing = True
                if not valid:
                    decreasing = check_decreasing(line[i], line[i+2])
                    increasing = check_increasing(line[i], line[i+2])
                
            if line[i] < line[i+1] :
                valid += True if not decreasing and line[i+1] - line[i] <= 3 else False
                if valid: increasing = True
        if valid: count += 1  


print(count)