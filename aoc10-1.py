from collections import deque
result = 0

def traverse(i,j):
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    queue = deque([(i, j, '0')])
    count = 0
    visited = set((0, 0))
    while queue:
        x, y, num = queue.popleft()
        if (num == '9'):
            count += 1
            continue
        for dx, dy in directions:
            nextVal = str(int(num)+1)
            nx, ny = x + dx, y + dy
            if (0 <= nx < rows and 0 <= ny < cols and 
                (nx, ny) not in visited and maze[nx][ny] == nextVal): 
                    visited.add((nx, ny))
                    queue.append((nx, ny, nextVal))
    return count

maze=[]
with open('aoc10.txt', 'r') as file:
    for line in file:
        row = list(line.strip())
        maze.append(row)

rows = len(maze)
cols = len(maze[0])

for i in range(rows):
    for j in range(cols):
        if (maze[i][j] == '0'):
            result += traverse(i,j)

print(result)




