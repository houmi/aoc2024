list_str = []
numbers = []

safe = 0

with open('aoc2.txt', 'r') as file:
    for line in file:
        list_str = line.split()
        numbers = [int(num) for num in list_str] 
        increasing = 0 
        if (numbers[1]>numbers[0]):
            increasing = 1
        elif (numbers[1]<numbers[0]):
            increasing = -1 
        else:
           continue
        deltas = []
        for i in range(1, len(numbers)):
           difference = numbers[i] - numbers[i-1]
           deltas.append(difference)
        fail = 0
        for i in deltas:
            if (i>0 and increasing == -1) or (i<0 and increasing == 1):
                fail = -1
                break
            if (increasing == -1 and (i<-3 or i>-1)):
                fail = -1
                break
            if (increasing == 1 and (i<1 or i>3)):
                fail = -1
                break
        if (fail == -1):
            continue
        safe = safe+1

print(safe)
