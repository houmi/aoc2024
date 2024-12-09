list1 = []
list2 = []

with open('aoc1.txt', 'r') as file:
    for line in file:
        num1, num2 = line.split()
        list1.append(int(num1))
        list1.sort()
        list2.append(int(num2))
        list2.sort()

result = 0
for i,j in zip(list1, list2):
 result += abs(i-j)

print (result)
