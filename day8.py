from typing import List


matrix = [[cell for cell in row] for row in open("input.txt").read().splitlines()]


ROWS = len(matrix)
COLS = len(matrix[0])
SIZE = ROWS

frequencies = {}
antinodes = set()
resonantAntinodes = set()


for r in range(ROWS):
    for c in range(COLS):
        cell = matrix[r][c]
        if cell == ".":
            continue
        if cell in frequencies:
            frequencies[cell].append((r, c))
        else:
            frequencies[cell] = [(r, c)]


def inBounds(antinode: tuple):
    return all(0 <= coord < SIZE for coord in antinode)


def countAntinodes(testAntennas: List[tuple]):
    for (r1, c1), (r2, c2) in testAntennas:
        rDiff, cDiff = r2 - r1, c2 - c1
        for antinode in [(r1 - rDiff, c1 - cDiff), (r2 + rDiff, c2 + cDiff)]:
            if inBounds(antinode):
                antinodes.add(antinode)


def countResonantAntinodes(testAntennas: List[tuple]):
    for antennas in testAntennas:
        resonantAntinodes.update(antennas)

        (r1, c1), (r2, c2) = antennas
        rDiff, cDiff = r2 - r1, c2 - c1

        antinode1 = r1 - rDiff, c1 - cDiff
        while inBounds(antinode1):
            resonantAntinodes.add(antinode1)
            r, c = antinode1
            antinode1 = r - rDiff, c - cDiff

        antinode2 = r2 + rDiff, c2 + cDiff
        while inBounds(antinode2):
            resonantAntinodes.add(antinode2)
            r, c = antinode2
            antinode2 = r + rDiff, c + cDiff


for frequency in frequencies.keys():
    antennas = frequencies[frequency]
    testAntennas = [
        (antennas[x], antennas[y])
        for x in range(len(antennas) - 1)
        for y in range(1, len(antennas))
        if x != y
    ]
    countAntinodes(testAntennas)
    countResonantAntinodes(testAntennas)


print("pt1: ", len(antinodes))
print("pt2: ", len(resonantAntinodes))
