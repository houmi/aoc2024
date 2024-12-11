import itertools
import math
maze=[]
combinations=[]
antinodes=[]
map={}
antennas=0

def inRange(point):
    if(point[0]<0 or point[0]>=len(maze) or 
       point[1]<0 or point[1]>=len(maze[0])):
        return False
    return True

def expandAntiNodes(point, dx, dy):
    point = (point[0]-dx, point[1]-dy)
    while inRange(point):
        antinodes.append(point)
        point = (point[0]-dx, point[1]-dy)

with open('aoc8.txt', 'r') as file:
    for line in file:
        row = list(line.strip())
        maze.append(row)

for i in range(len(maze)):
    for j in range(len(maze[0])):
        if (maze[i][j].isalnum()):
            antennas +=1
            map.setdefault(maze[i][j],[]).append(tuple([i,j]))

for key in map:
    tuples = map[key]
    combinations += list(itertools.combinations(tuples, 2))

for combination in combinations:
    dx=combination[1][0]-combination[0][0]
    dy=combination[1][1]-combination[0][1]
    
    point = (combination[0][0], combination[0][1])
    expandAntiNodes(point, dx, dy)
    expandAntiNodes(point, -dx,-dy)

    point = (combination[1][0], combination[1][1])
    expandAntiNodes(point, dx, dy)
    expandAntiNodes(point, -dx,-dy)

# remove duplicates
antinodes = list(set(antinodes))
print(len(antinodes))