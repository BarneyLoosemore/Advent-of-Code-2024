from typing import List


matrix = [[cell for cell in row] for row in open(0).splitlines()]


def countXmases(cell: tuple) -> bool:
    r, c = cell

    top = [(r - 1, c), (r - 2, c), (r - 3, c)]
    topRight = [(r - 1, c + 1), (r - 2, c + 2), (r - 3, c + 3)]
    right = [(r, c + 1), (r, c + 2), (r, c + 3)]
    bottomRight = [(r + 1, c + 1), (r + 2, c + 2), (r + 3, c + 3)]
    bottom = [(r + 1, c), (r + 2, c), (r + 3, c)]
    bottomLeft = [(r + 1, c - 1), (r + 2, c - 2), (r + 3, c - 3)]
    left = [(r, c - 1), (r, c - 2), (r, c - 3)]
    topLeft = [(r - 1, c - 1), (r - 2, c - 2), (r - 3, c - 3)]
    checks = [top, topRight, right, bottomRight, bottom, bottomLeft, left, topLeft]

    words = [
        matrix[r1][c1] + matrix[r2][c2] + matrix[r3][c3]
        for (r1, c1), (r2, c2), (r3, c3) in checks
        if all(0 <= r < len(matrix) for r in [r1, r2, r3])  # within bounds
        and all(0 <= c < len(matrix[0]) for c in [c1, c2, c3])
    ]

    return len([word for word in words if word == "MAS" or reversed(word) == "MAS"])


xs = [
    (r, c) for r, row in enumerate(matrix) for c, cell in enumerate(row) if cell == "X"
]

xmasCount = sum(countXmases(x) for x in xs)
print("pt1:", xmasCount)


def checkForMas(grid: List[List[int]]) -> True:
    d1 = grid[0][0] + grid[1][1] + grid[2][2]
    d2 = grid[2][0] + grid[1][1] + grid[0][2]
    return all(d == "MAS" or d == "SAM" for d in [d1, d2])


grids = [
    [row[colStart : colStart + 3] for row in matrix[rowStart : rowStart + 3]]
    for rowStart in range(len(matrix) - 2)
    for colStart in range(len(matrix[0]) - 2)
]

masXs = len([grid for grid in grids if checkForMas(grid)])
print("pt2:", masXs)
