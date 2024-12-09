list1 = []
list2 = []

hashtable = {}

with open('aoc1.txt', 'r') as file:
    for line in file:
        num1, num2 = line.split()
        list1.append(int(num1))
        list2.append(int(num2))
        num = int(num2)
        if num in hashtable:
            hashtable[num] += 1
        else:
            hashtable[num] = 1

result = 0
for i in list1:
    if i in hashtable:
        result += (i * hashtable[i])

print (result)
