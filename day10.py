grid = [list(map(int, row)) for row in open("input.txt").read().splitlines()]


ROWS = len(grid)
COLS = len(grid[0])


dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def traverse(node: tuple[int, int], visited: set, allTrails: bool) -> int:
    r, c = node
    height = grid[r][c]

    if height == 9 and (node not in visited or allTrails):
        visited.add((r, c))
        return 1

    neighbours = [
        (r + rd, c + cd)
        for rd, cd, in dirs
        if 0 <= r + rd < ROWS
        and 0 <= c + cd < COLS
        and grid[r + rd][c + cd] - height == 1
    ]

    return sum(traverse((r, c), visited, allTrails) for r, c in neighbours)


trailheads = [(r, c) for r in range(ROWS) for c in range(COLS) if grid[r][c] == 0]

trailheadsScore = sum(traverse(trailhead, set(), False) for trailhead in trailheads)
trailheadsTrails = sum(traverse(trailhead, set(), True) for trailhead in trailheads)


print("pt1:", trailheadsScore)
print("pt2:", trailheadsTrails)
