from collections import defaultdict, deque
import string

maze = []

def colorize(x, y, plant):
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    queue = deque([(x, y)])
    maze[x][y]=plant.lower()
    perimeter = 0
    area = 0

    while queue:
        x, y = queue.popleft()
        area += 1
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # permieter update
            if (nx < 0 or nx == rows): perimeter += 1
            if (ny < 0 or ny == cols): perimeter += 1
            if (0 <= nx < rows and 0 <= ny < cols):
                if (maze[nx][ny] == plant.lower()):
                    continue
                if (maze[nx][ny] == plant): 
                    queue.append((nx, ny))
                    maze[nx][ny]=plant.lower()
                else:
                    perimeter += 1

    #print(plant, perimeter, area)
    gardens_cost[plant] += area*perimeter
    return 
    

with open('aoc12.txt', 'r') as file:
    for line in file:
        row = list(line.strip())
        maze.append(row)
        
gardens_cost = defaultdict(int)
rows = len(maze)
cols = len(maze[0])

for i in range(rows):
    for j in range(cols):
        if (maze[i][j] not in string.ascii_lowercase):
            colorize(i, j, maze[i][j])

#print(gardens_cost)
print(sum(gardens_cost.values()))
