
from collections import defaultdict
lookup = {}

def blink(num):
    if num in lookup:
        return lookup[num]
    if (num == '0'):
        lookup[num] = ['1']
    elif (len(num) % 2 == 0):
        mid = len(num) // 2
        left = num[:mid]
        right = num[mid:]
        lookup[num] = [left, str(int(right))]
    else:
        lookup[num]=[str(int(num)*2024)]

    return lookup[num]

def iterations(line, n):
    current = defaultdict(int)

    for num in line:
        current[num] += 1

    for i in range(n):
        next = defaultdict(int)
        for num, count in current.items():
            children = blink(num)
            for child in children:
                next[child] += count
        current = next
    
    return sum(current.values())

with open('aoc11.txt', 'r') as file:
    for line in file:
        line = line.strip().split()

print(iterations(line, 25))
print(iterations(line, 75))



