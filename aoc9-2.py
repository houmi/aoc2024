from collections import OrderedDict
IDnumber = 0
disk= []
index=0
fileIDtoIndexAndSize = {}
sorted_freeSpaceIndeces = {}

def moveFiles(fileID, srcFileIndexAndSize, freeSpaceIndecesAvailableVec):
    dstdiskOffset = freeSpaceIndecesAvailableVec[0]
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
        for i in range(int(c)):
            disk += "."
        sorted_freeSpaceIndeces.setdefault(int(c),[]).append(index)

#compact
sorted_freeSpaceIndeces = OrderedDict(sorted(sorted_freeSpaceIndeces.items()))

IDnumber -= 1
for fileID in range(IDnumber, 1, -1):
    # find how many space it uses
    srcFileIndexAndSize = fileIDtoIndexAndSize[fileID]
    srcFileSize = srcFileIndexAndSize[1]
    # find if we have space for it
    for freeSpaceAvailable in sorted_freeSpaceIndeces:
        # we are interested in spaces equal or bigger to what we want to find
        if (freeSpaceAvailable >= srcFileSize):
            freeSpaceIndecesAvailableVec = sorted_freeSpaceIndeces.get(freeSpaceAvailable)
            if freeSpaceIndecesAvailableVec is not None:
                # found spaces vectors
                # 0th index is the left most
                dstOffset = freeSpaceIndecesAvailableVec[0]
                if (dstOffset >= srcFileIndexAndSize[0]):
                    break
                moveFiles(fileID, srcFileIndexAndSize, freeSpaceIndecesAvailableVec)
                # pop value since it is no longer the same spave available
                freeSpaceIndecesAvailableVec.pop(0)
                #if vector is empty, delete it from the map
                if not freeSpaceIndecesAvailableVec:
                    sorted_freeSpaceIndeces.pop(freeSpaceAvailable, None)
                    break  
                # if we didn't fill the space (i.e. file size was less than free space)                  
                # we want to add the free space value back to the map
                if (srcFileSize < freeSpaceAvailable):
                    freeSpace = freeSpaceAvailable-srcFileSize
                    freeSpaceVec = sorted_freeSpaceIndeces[freeSpace]
                    freeSpaceVec.append(dstOffset+srcFileSize)
                    sorted_freeSpaceIndeces[freeSpace]=(sorted(freeSpaceVec))

#checksum
left, right = 0, len(disk)-1
sum = 0
while left < right:
    if (disk[left] != "."):
        sum += (int(disk[left])*left)
    left +=1

print(sum)         

