from typing import List


grid = [
    ["."] + [cell for cell in row] + ["."]
    for row in open("input.txt").read().splitlines()
]

grid = (
    [["." for _ in range(len(grid[0]))]] + grid + [["." for _ in range(len(grid[0]))]]
)
ROWS = len(grid)
COLS = len(grid[0])

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


flooded = set()


def inBounds(r: int, c: int) -> bool:
    return 0 <= r < ROWS and 0 <= c < COLS


def isEdge(r: int, c: int, plot: List[tuple[int, int]]) -> bool:
    return not inBounds(r, c) or (r, c) not in plot


def flood(node: tuple[int, int], plot: set[tuple[int, int]]) -> List[tuple[int, int]]:
    if node in plot:
        return

    plot.add(node)

    r, c = node
    neighbours = [
        (r + rd, c + cd)
        for rd, cd, in DIRS
        if inBounds(r + rd, c + cd) and grid[r + rd][c + cd] == grid[r][c]
    ]
    if neighbours == []:
        return
    for n in neighbours:
        flood(n, plot)
    return


def countEdges(node: tuple[int, int], plot: List[tuple[int, int]]) -> int:
    r, c = node
    toCheck = [(r + rd, c + cd) for rd, cd in DIRS]
    return len([(r, c) for r, c in toCheck if isEdge(r, c, plot)])


def calcPerimeter(plot: List[tuple[int, int]]) -> int:
    return sum(countEdges(node, plot) for node in plot)


def calcSides(plot: List[tuple[int, int]]) -> int:
    edgeTypes = [
        [False, False, False, True],
        [False, False, True, False],
        [False, True, False, False],
        [True, False, False, False],
    ]

    cornerTypes = [
        [False, True, True, True],
        [True, False, True, True],
        [True, True, False, True],
        [True, True, True, False],
    ]

    doubleCornerTypes = [
        [False, True, True, False],
        [True, False, False, True],
    ]

    edges = 0
    corners = 0
    for r in range(ROWS - 1):
        for c in range(COLS - 1):
            block = [
                (r, c),
                (r, c + 1),
                (r + 1, c),
                (r + 1, c + 1),
            ]
            inPlot = [node in plot for node in block]

            if any(edgeTypes == inPlot for edgeTypes in edgeTypes):
                edges += 1
            if any(cornerTypes == inPlot for cornerTypes in cornerTypes):
                corners += 1
            if any(
                doubleCornerTypes == inPlot for doubleCornerTypes in doubleCornerTypes
            ):
                corners += 2

    return edges + corners


totalWithArea = 0
totalWithSides = 0

for r in range(ROWS):
    for c in range(COLS):
        node = (r, c)
        if node in flooded or grid[r][c] == ".":
            continue
        plot = set()
        flood(node, plot)
        flooded.update(plot)

        perimeter = calcPerimeter(plot)
        area = len(plot)
        sides = calcSides(plot)

        totalWithArea += perimeter * area
        totalWithSides += area * sides


print("pt1:", totalWithArea)
print("pt2:", totalWithSides)
