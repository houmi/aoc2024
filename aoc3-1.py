import re

result = 0
with open('aoc3.txt', 'r') as file:
    buffer = file.read()

pattern = r'mul\((\d+,\d+)\)'
buffer = re.findall(pattern, buffer)
for l in buffer:
   x, y = l.split(',')
   x = int(x)
   y = int(y)
   result += x*y

print(result)

