dict = {}

def foo(x, y):
    s = str(x) + str(y)
    return int(s)

def solve(target, equation, curVal, idx):
    if (idx == len(equation)):
        if (target == curVal):
            return 1
        else:
            return 0 
        
    result = 0
    result = solve(target, equation, curVal*equation[idx], idx+1)
    if (result == 1):
        return 1
    
    result = solve(target, equation, curVal+equation[idx], idx+1)
    if (result == 1):
        return 1
    
    result = 0
    result = solve(target, equation, foo(curVal, equation[idx]), idx+1)
    if (result == 1):
        return 1
          
    return 0


with open('aoc7.txt', 'r') as file:
    for line in file:
        key, vals = line.split(':')
        key = int(key.strip())
        vals = list(map(int, vals.strip().split()))
        dict[key] = vals

result = 0
final = 0
for target, equation in dict.items():
    result = solve(target, equation, equation[0], 1)
    if (result == 1):
        final += target

print(final)
        
        

