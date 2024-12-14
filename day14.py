from functools import reduce
from typing import List


lines = [line.split(" ") for line in open("input.txt").read().splitlines()]
robots = [
    list(
        map(
            int,
            [*points.split("=")[1].split(","), *velocities.split("=")[1].split(",")],
        )
    )
    for points, velocities in lines
]


ROWS = 103
COLS = 101

MID_ROW = ROWS // 2
MID_COL = COLS // 2

SECONDS = 100


def move(robot: List[int]) -> List[int]:
    c, r, cd, rd = robot

    if c + cd > COLS - 1:
        c = c + cd - COLS
    elif c + cd < 0:
        c = c + cd + COLS
    else:
        c = c + cd

    if r + rd > ROWS - 1:
        r = r + rd - ROWS
    elif r + rd < 0:
        r = r + rd + ROWS
    else:
        r = r + rd

    return [c, r, cd, rd]


def moveRecur(robot: List[int], seconds: int) -> List[int]:
    if seconds == 0:
        return robot
    return moveRecur(move(robot), seconds - 1)


totals = 0

quadrants = [0] * 4

for robot in robots:
    c, r, *_ = moveRecur(robot, SECONDS)

    if r < MID_ROW and c < MID_COL:
        quadrants[0] += 1
    elif r < MID_ROW and c > MID_COL:
        quadrants[1] += 1
    elif r > MID_ROW and c < MID_COL:
        quadrants[2] += 1
    elif r > MID_ROW and c > MID_COL:
        quadrants[3] += 1

product = reduce(lambda quadrant, total: quadrant * total, quadrants)

print("pt1:", product)


def xmasTreePresent(robots: List[int]) -> bool:
    diagonals = 0
    robots = [(c, r) for c, r, *_ in robots]
    for c, r in robots:
        if any(
            [
                (c + 1, r + 1) in robots,
                (c - 1, r + 1) in robots,
            ]
        ):
            diagonals += 1
    if diagonals > 200:
        return True
    return False


secs = 0
while True:
    secs += 1
    for i in range(len(robots)):
        robots[i] = move(robots[i])

    if xmasTreePresent(robots):
        print("pt2:", secs)
        break
