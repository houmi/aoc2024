maze = []

result=0

def xmas(i, j):
    topleft = maze[i-1][j-1]
    topright = maze[i-1][j+1]
    botleft = maze[i+1][j-1]
    botright = maze[i+1][j+1]
    if (topleft == 'M' and topright == 'S' and botleft == 'M' and botright == 'S'):
        return 1
    if (topleft == 'M' and topright == 'M' and botleft == 'S' and botright == 'S'):
        return 1
    if (topleft == 'S' and topright == 'S' and botleft == 'M' and botright == 'M'):
        return 1
    if (topleft == 'S' and topright == 'M' and botleft == 'S' and botright == 'M'):
        return 1
    return 0

with open('aoc4.txt', 'r') as file:
    for line in file:
        row = list(line.strip())
        maze.append(row)
        print(row)

for i in range(1, len(maze)-1):
    for j in range(1, len(maze[0])-1):
        if (maze[i][j] == 'A'):
           print(i, j, 'A')
           result += xmas(i, j)

print(result)
