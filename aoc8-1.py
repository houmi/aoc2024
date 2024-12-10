import itertools
import math
maze=[]
combinations=[]
antinodes=[]
map={}

with open('aoc8.txt', 'r') as file:
    for line in file:
        row = list(line.strip())
        maze.append(row)

for i in range(len(maze)):
    for j in range(len(maze[0])):
        if (maze[i][j].isalnum()):
            map.setdefault(maze[i][j],[]).append(tuple([i,j]))

for key in map:
    tuples = map[key]
    combinations += list(itertools.combinations(tuples, 2))

for combination in combinations:
    dx=combination[1][0]-combination[0][0]
    dy=combination[1][1]-combination[0][1]
    antinodes.append((combination[0][0]-dx, combination[0][1]-dy))
    antinodes.append((combination[1][0]+dx, combination[1][1]+dy))

# remove duplicates
antinodes = list(set(antinodes))

unique=0
for antinode in antinodes:
    if (antinode[0]<0 or antinode[0]>=len(maze) or
        antinode[1]<0 or antinode[1]>=len(maze[0])):
        continue
    print(antinode)
    unique +=1

print(unique)
