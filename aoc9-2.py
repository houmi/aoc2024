IDnumber = 0
disk= []
index=0
fileIDtoIndexAndSize = {}
freeSpaceIndeces = []

def diskPrint(disk):
    combined_string = ' '.join(map(str, disk))
    print(combined_string)

def moveFiles(fileID, srcFileIndexAndSize, spaceAvailableAtIndex):
    dstdiskOffset = spaceAvailableAtIndex
    filesize = srcFileIndexAndSize[1]
    filesrcIndex = srcFileIndexAndSize[0]
    for idx in range(filesize):
        disk[dstdiskOffset+idx] = fileID
        disk[filesrcIndex+idx] = "."

with open('aoc9.txt', 'r') as file:
    while True:
        c = file.read(1)
        if not c:
            break
        index=len(disk)
        for i in range(int(c)):
            disk.append(IDnumber)
        fileIDtoIndexAndSize[IDnumber] = (index,int(c))
        IDnumber += 1
        index=len(disk)
        c = file.read(1)
        if not c:
            break
        if (c == '0'):
            continue
        for i in range(int(c)):
            disk += "."
        freeSpaceIndeces.append((int(c), index))

#compact
IDnumber -= 1
for fileID in range(IDnumber, 0, -1):
    # find how many space it uses
    srcFileIndexAndSize = fileIDtoIndexAndSize[fileID]
    srcFileSize = srcFileIndexAndSize[1]
    # find if we have space for it
    for i in range(len(freeSpaceIndeces)):
        # we are interested in spaces equal or bigger to what we want to find
        spaceAvailable = freeSpaceIndeces[i][0]
        spaceAvailableAtIndex = freeSpaceIndeces[i][1]
        # we won't write to the file's right
        if (spaceAvailableAtIndex > srcFileIndexAndSize[0]):
            break
        if (spaceAvailable >= srcFileSize):
            moveFiles(fileID, srcFileIndexAndSize, spaceAvailableAtIndex)
            newSpace = spaceAvailable-srcFileSize
            if (newSpace == 0):
                freeSpaceIndeces.pop(i)
            else:
                freeSpaceIndeces[i] = (newSpace, spaceAvailableAtIndex+srcFileSize)
            break

#checksum
left, right = 0, len(disk)-1
sum = 0
while left < right:
    if (disk[left] != "."):
        sum += (int(disk[left])*left)
    left +=1

print(sum)         

