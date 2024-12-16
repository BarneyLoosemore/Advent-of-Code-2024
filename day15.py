from typing import List, Set, Tuple, Literal, cast

rawGrid, rawDirections = [
    block.splitlines() for block in open("input.txt").read().split("\n\n")
]

directions = [char for line in rawDirections for char in line]
grid = [list(row) for row in rawGrid]

ROWS = len(grid)
COLS = len(grid[0])
DIRS = Literal["^", ">", "v", "<"]


def getBoxes(
    grid: List[List[str]], robot: Tuple[int, int], dir: DIRS
) -> List[Tuple[int, int]]:
    r, c = robot
    boxes: List[Tuple[int, int]] = []

    match dir:
        case "^":
            for i in range(r - 1, 0, -1):
                cell = list(zip(*grid))[c][i]
                match cell:
                    case "#":
                        return []
                    case ".":
                        return boxes
                    case _:
                        boxes.append((i, c))
        case "v":
            for i in range(r + 1, ROWS, 1):
                cell = list(zip(*grid))[c][i]
                match cell:
                    case "#":
                        return []
                    case ".":
                        return boxes
                    case _:
                        boxes.append((i, c))
        case "<":
            for i in range(c - 1, 0, -1):
                cell = grid[r][i]
                match cell:
                    case "#":
                        return []
                    case ".":
                        return boxes
                    case _:
                        boxes.append((r, i))
        case ">":
            for i in range(c + 1, COLS, 1):
                cell = grid[r][i]
                match cell:
                    case "#":
                        return []
                    case ".":
                        return boxes
                    case _:
                        boxes.append((r, i))
    return boxes


def move(dir: DIRS, grid: List[List[str]], boxes: List[Tuple[int, int]]):
    match dir:
        case "^":
            boxes.sort(key=lambda x: x[0])
            for rB, cB in boxes:
                toSwap = grid[rB - 1][cB]
                if toSwap != ".":
                    return
                grid[rB - 1][cB] = grid[rB][cB]
                grid[rB][cB] = toSwap
        case "v":
            boxes.sort(key=lambda x: x[0], reverse=True)
            for rB, cB in boxes:
                toSwap = grid[rB + 1][cB]
                if toSwap != ".":
                    return
                grid[rB + 1][cB] = grid[rB][cB]
                grid[rB][cB] = toSwap
        case "<":
            boxes.sort(key=lambda x: x[1])
            for rB, cB in boxes:
                toSwap = grid[rB][cB - 1]
                if toSwap != ".":
                    return
                grid[rB][cB - 1] = grid[rB][cB]
                grid[rB][cB] = toSwap
        case ">":
            boxes.sort(key=lambda x: x[1], reverse=True)
            for rB, cB in boxes:
                toSwap = grid[rB][cB + 1]
                if toSwap != ".":
                    return
                grid[rB][cB + 1] = grid[rB][cB]
                grid[rB][cB] = toSwap


def calc() -> int:
    for direction in directions:
        [robot] = [
            (r, c) for r in range(ROWS) for c in range(COLS) if grid[r][c] == "@"
        ]
        dir = cast(DIRS, direction)
        boxes = getBoxes(grid, robot, dir)
        boxes.append(robot)
        move(dir, grid, boxes)
    boxCords = [
        (100 * r) + c for r in range(ROWS) for c in range(COLS) if grid[r][c] == "O"
    ]
    return sum(boxCords)


def getExpandedBoxes(
    expandedGrid: List[List[str]], robot: Tuple[int, int], dir: DIRS
) -> List[Tuple[int, int]]:
    boxes: Set[Tuple[int, int]] = set()
    queue = [robot]

    match dir:
        case "^":
            while queue:
                r, c = queue.pop(0)
                rowAbove = r - 1
                above = expandedGrid[rowAbove][c]
                match above:
                    case "#":
                        return []
                    case "[":
                        box = [(rowAbove, c), (rowAbove, c + 1)]
                        boxes.update(box)
                        queue.extend(box)
                    case "]":
                        box = [(rowAbove, c), (rowAbove, c - 1)]
                        boxes.update(box)
                        queue.extend(box)
                    case _:
                        pass

        case "v":
            while queue:
                r, c = queue.pop(0)
                rowBelow = r + 1
                below = expandedGrid[rowBelow][c]
                match below:
                    case "#":
                        return []
                    case "[":
                        box = [(rowBelow, c), (rowBelow, c + 1)]
                        boxes.update(box)
                        queue.extend(box)
                    case "]":
                        box = [(rowBelow, c), (rowBelow, c - 1)]
                        boxes.update(box)
                        queue.extend(box)
                    case _:
                        pass

        case ">":
            while queue:
                r, c = queue.pop(0)
                colRight = c + 1
                right = expandedGrid[r][colRight]
                match right:
                    case "#":
                        return []
                    case "[":
                        box = [(r, colRight), (r, colRight + 1)]
                        boxes.update(box)
                        queue.append((r, colRight + 1))
                    case _:
                        pass

        case "<":
            while queue:
                r, c = queue.pop(0)
                colLeft = c - 1
                left = expandedGrid[r][colLeft]
                match left:
                    case "#":
                        return []
                    case "]":
                        box = [(r, colLeft), (r, colLeft - 1)]
                        boxes.update(box)
                        queue.append((r, colLeft - 1))
                    case _:
                        pass
    return list(boxes)


def expandGrid(grid: List[List[str]]) -> List[List[str]]:
    expanded: List[List[str]] = [[] for _ in range(COLS)]
    for r in range(ROWS):
        for c in range(COLS):
            match grid[r][c]:
                case "#":
                    expanded[r].extend(["#", "#"])
                case "O":
                    expanded[r].extend(["[", "]"])
                case ".":
                    expanded[r].extend([".", "."])
                case "@":
                    expanded[r].extend(["@", "."])
                case _:
                    pass
    return expanded


def calcExpanded():
    expandedGrid = expandGrid(grid)
    for direction in directions:
        [robot] = [
            (r, c)
            for r in range(ROWS)
            for c in range(COLS * 2)
            if expandedGrid[r][c] == "@"
        ]
        dir = cast(DIRS, direction)
        boxes = getExpandedBoxes(expandedGrid, robot, dir)
        boxes.append(robot)
        move(dir, expandedGrid, boxes)

    boxCords = [
        (100 * r) + c
        for r in range(ROWS)
        for c in range(COLS * 2)
        if expandedGrid[r][c] == "["
    ]
    return sum(boxCords)


print("pt1:", calc())
print("pt2:", calcExpanded())
