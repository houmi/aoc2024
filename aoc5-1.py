
orderList = {}

docs = []


with open('aoc5.txt', 'r') as file:
    for line in file:
        lineStr = line.strip()
        if "|" in lineStr:
            num1, num2 = lineStr.split('|')
            num1 = int(num1)
            num2 = int(num2)
            orderList.setdefault(num1, []).append(num2)
        elif "," in lineStr:
            number_list = lineStr.split(',')
            numbers = [int(number) for number in number_list]
            docs.append(numbers)

result = 0

for i in range(len(docs)):
    error = 0
    for j in range(1, len(docs[i])):
        prev = docs[i][j-1]
        cur = docs[i][j]
        x = orderList.get(prev)
        if x is None:
            error = -1
            break
        if cur in x:
            continue
        else:
            error = -1
            break
    if (error == 0):
        result += docs[i][len(docs[i]) // 2]

print(result)
