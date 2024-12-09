orderList = {}
docs = []

def topSort(values):
    def dfs(node):
        visited.add(node)
        tempStack.add(node)
        try:
            intersection = list(set(values) & set(orderList[node]))
            for next in intersection:
                if next not in visited:
                    if not dfs(next):
                        return False
                elif next in tempStack:
                    return False
        except:
            pass
        tempStack.remove(node)
        stack.append(node)
        return True
       
    visited = set()
    tempStack = set()
    stack = []

    for node in values:
        if node not in visited:
            if (dfs(node) == False):
                stack.append(node)

    return stack[::-1]

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
    if (error == -1):
        newVals = topSort(docs[i])
        result += newVals[len(newVals) //2]
        
print(result)