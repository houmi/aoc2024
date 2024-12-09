import sys
sys.setrecursionlimit(15000)

maze = []
result = 0

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dirIdx = 0

def traverse(x, y, dirIdx, count):
    if(x == 0 or y == 0 or x == rows-1 or y == cols-1):
        maze[x][y] = 'X'
        count += 1
        return count
    if (maze[x][y] != 'X'):
        maze[x][y] = 'X'
        count += 1
    newX = x+direction[dirIdx][0]
    newY = y+direction[dirIdx][1]
    print(x, y, maze[x][y], newX, newY, maze[newX][newY], count)
    if (maze[newX][newY] == '#'):
        dirIdx += 1
        if (dirIdx == 4):
            dirIdx = 0
        newX = x+direction[dirIdx][0]
        newY = y+direction[dirIdx][1]
    return traverse(newX, newY, dirIdx, count)

with open('aoc6-1.txt', 'r') as file:
    for line in file:
        row = list(line.strip())
        maze.append(row)

rows = len(maze)
cols = len(maze[0])
startX=0
startY=0

for i in range(rows):
    for j in range(cols):
        if (maze[i][j] == '^'):
            startX=i
            startY=j
            break

result = traverse(startX, startY, dirIdx, 0)
print(result)




