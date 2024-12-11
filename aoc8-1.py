import itertools
import math
maze=[]
combinations=[]
antinodes=[]
map={}

def inRange(point):
    if(point[0]<0 or point[0]>=len(maze) or 
       point[1]<0 or point[1]>=len(maze[0])):
        return False
    return True

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
    
    prev = (combination[0][0]-dx, combination[0][1]-dy)
    if inRange(prev):
        antinodes.append(prev)
    next = (combination[1][0]+dx, combination[1][1]+dy)
    if inRange(next):
        antinodes.append(next)

# remove duplicates
antinodes = list(set(antinodes))
print(len(antinodes))
