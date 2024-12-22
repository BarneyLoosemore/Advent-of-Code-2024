from collections import deque
from typing import Deque, List, Tuple


bytePositions = [
    tuple(map(int, b.split(","))) for b in open("input.txt").read().splitlines()
]


WIDTH = 71
HEIGHT = 71

grid = [
    ["#" if (c, r) in bytePositions[:1024] else "." for c in range(WIDTH)]
    for r in range(HEIGHT)
]


print("\n".join(["".join(row) for row in grid]))


DIRS: List[Tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def bfs(grid: List[List[str]]) -> int:
    queue: Deque[Tuple[int, int]] = deque([(0, 0)])
    distances = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
    visited = [[False for _ in range(WIDTH)] for _ in range(HEIGHT)]

    while queue:
        r, c = queue.popleft()

        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            isValidNeighbour = (
                0 <= nr < HEIGHT
                and 0 <= nc < WIDTH
                and grid[nr][nc] == "."
                and not visited[nr][nc]
            )
            if isValidNeighbour:
                queue.append((nr, nc))
                visited[nr][nc] = True
                distances[nr][nc] = distances[r][c] + 1
    return distances[-1][-1]


# ugly brute force, but it works
def findFirstByte():
    byteCount = 1024
    while True:
        grid = [
            [
                "#" if (c, r) in bytePositions[: byteCount + 1] else "."
                for c in range(WIDTH)
            ]
            for r in range(HEIGHT)
        ]
        if bfs(grid) == 0:
            return bytePositions[byteCount]
        byteCount += 1


print("pt1:", bfs(grid))
print("pt2:", findFirstByte())
