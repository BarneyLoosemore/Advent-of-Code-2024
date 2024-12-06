from multiprocessing import Pool
from typing import List

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

matrix = [
    [position for position in row] for row in open("input.txt").read().splitlines()
]


[startingPos] = [
    (r, c)
    for r in range(len(matrix))
    for c in range(len(matrix[0]))
    if matrix[r][c] == "^"
]


def traverse(matrix: List[List[int]], returnVisited: bool) -> bool:
    visitedObstructions = []
    visited = [startingPos]
    position = startingPos
    direction = DIRECTIONS[0]

    while True:
        if (*position, *direction) in visitedObstructions:
            return True

        rowDiff, colDiff = direction
        row, col = position
        nextRow, nextCol = row + rowDiff, col + colDiff
        outOfBounds = not (0 <= nextRow < len(matrix) and 0 <= nextCol < len(matrix[0]))

        if outOfBounds:
            return visited if returnVisited else False

        if matrix[nextRow][nextCol] == "#":
            visitedObstructions.append((*position, *direction))
            nextDir = DIRECTIONS.index(direction) + 1
            direction = DIRECTIONS[nextDir if nextDir < len(DIRECTIONS) else 0]
        else:
            position = (nextRow, nextCol)
            visited.append(position)


def testIfStuck(testPos: tuple) -> bool:
    r, c = testPos
    matrixCopy = [[position for position in row] for row in matrix]
    matrixCopy[r][c] = "#"
    return traverse(matrixCopy, False)


if __name__ == "__main__":
    visitedPositions = set(traverse(matrix, True))
    print("pt1: ", len(visitedPositions))

    # parallelising the work so brute-force doesn't hurt quite so much
    with Pool(12) as p:
        stuck = p.map(testIfStuck, visitedPositions)
        print("pt2: ", stuck.count(True))
