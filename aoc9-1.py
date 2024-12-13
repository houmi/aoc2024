IDnumber = 0
disk= []
map = {}

with open('aoc9.txt', 'r') as file:
    while True:
        c = file.read(1)
        if not c:
            break
        for i in range(int(c)):
            disk.append(IDnumber)
        IDnumber += 1
        c = file.read(1)
        if not c:
            break
        for i in range(int(c)):
            disk += "."

#compact
left, right = 0, len(disk)-1
while left < right:
    while (left < right and disk[right]== "."):
        right -=1
    while (left < right and disk[left] != "."):
        left +=1
    disk[left]=disk[right]
    disk[right]="."
    left += 1
    right -=1

#checksum
left, right = 0, len(disk)-1
sum = 0
while left < right:
    if (disk[left] == "."):
        break
    sum += (int(disk[left])*left)
    left +=1
print(sum)