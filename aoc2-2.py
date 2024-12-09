list_str = []
numbers = []

safe = 0

def solve(numbers):
    increasing = 0
    if (numbers[1]>numbers[0]):
        increasing = 1
    elif (numbers[1]<numbers[0]):
        increasing = -1
    else:
        return -1;
    deltas = []
    for i in range(1, len(numbers)):
       difference = numbers[i] - numbers[i-1]
       deltas.append(difference)
    fail = 0
    for i in deltas:
        if (i>0 and increasing == -1) or (i<0 and increasing == 1):
            return -1
        if (increasing == -1 and (i<-3 or i>-1)):
            return -1
        if (increasing == 1 and (i<1 or i>3)):
            return -1
    return 1

def brutforce(numbers):
    print(numbers)
    result = solve(numbers)
    if (result == 1):
        return 1
    for i in range(len(numbers)):
        numbers_copy = numbers[:]
        numbers_copy.pop(i)
        print(numbers_copy)
        result = solve(numbers_copy)
        if (result ==1):
            print("removed:" + str(numbers[i]))
            return 1
    return 0 

with open('aoc2.txt', 'r') as file:
    for line in file:
        list_str = line.split()
        numbers = [int(num) for num in list_str] 
        safe += brutforce(numbers)

print(safe)
