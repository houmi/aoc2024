maze = []

result=0
sol = "XMAS"

directions = [(1,0), (-1, 0), (0,1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]

def brutforce(i, j, word_index, word, dir_idx):
    i = i + directions[dir_idx][0]
    j = j + directions[dir_idx][1]
    if (i<0 or j<0 or i==rows or j==cols or word_index==4):
        return 0
    if (maze[i][j] != sol[word_index]):
        return 0
    word += maze[i][j]
    if (word == 'XMAS'):
        print(i, j, word)
        return 1
    return brutforce(i, j, word_index+1, word, dir_idx)

with open('aoc4.txt', 'r') as file:
    for line in file:
        row = list(line.strip())
        maze.append(row)

rows = len(maze)
cols = len(maze[0])

for i in range(rows):
    for j in range(cols):
        if (maze[i][j] == 'X'):
            word = 'X'
            print(i, j, 'X')
            for x in range(8):
                result += brutforce(i, j, 1, word, x)

print(result)
