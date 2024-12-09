from typing import List

input = open("input.txt").read()


def expand(disk: List[str]) -> List[str]:
    expanded = [
        [str(i // 2)] * int(disk[i]) if i % 2 == 0 else ["."] * int(disk[i])
        for i in range(len(disk))
    ]
    return [char for block in expanded for char in block]


def compactifyBlocks(disk: List[str]) -> List[str]:
    compactDisk = disk.copy()
    l, r = 0, len(compactDisk) - 1
    while l < r:
        if compactDisk[l] == "." and compactDisk[r] != ".":
            compactDisk[l], compactDisk[r] = compactDisk[r], compactDisk[l]
        elif compactDisk[r] == ".":
            r -= 1
        else:
            l += 1
    return compactDisk


def calcChecksum(compactDisk: List[int]) -> int:
    return sum(
        fileId * int(char) for fileId, char in enumerate(compactDisk) if char != "."
    )


disk = expand(input)
compactDisk = compactifyBlocks(disk)
checksum = calcChecksum(compactDisk)


def mapFiles(disk: List[str]) -> tuple[dict, List[tuple]]:
    files = {}
    spaces = []
    position = 0
    for i in range(len(disk)):
        char = int(disk[i])
        if char == 0:
            continue
        if i % 2 == 0:
            files[i // 2] = (position, char)
        else:
            spaces.append((position, char))
        position += char
    return (files, spaces)


files, spaces = mapFiles(input)

for fileId in reversed(files.keys()):
    position, length = files[fileId]
    for i, (start, size) in enumerate(spaces):
        if start >= position:
            break
        if size >= length:
            files[fileId] = start, length
            if size == length:
                spaces.pop(i)
            else:
                newStart = start + length
                newSize = size - length
                spaces[i] = (newStart, newSize)
            break

checksumWholeFiles = sum(
    sum([fileId * i for i in range(position, position + length)])
    for fileId, (position, length) in files.items()
)


print("pt1: ", checksum)
print("pt2: ", checksumWholeFiles)
