import re
from typing import List

xyPattern = re.compile(r"X.(\d+), Y.(\d+)")


def parseLine(button: str) -> List[int]:
    return list(map(int, re.findall(xyPattern, button.split(": ")[1])[0]))


def parseGame(game: List[str]) -> List[List[int]]:
    return [parseLine(line) for line in game]


games = [
    parseGame(game.splitlines()) for game in open("input.txt").read().split("\n\n")
]


def tokensForGame(game: List[List[int]], error: bool) -> int:
    *buttons, target = game
    [x1, y1], [x2, y2] = buttons
    t1, t2 = target

    t1 = t1 + 10000000000000 if error else t1
    t2 = t2 + 10000000000000 if error else t2

    p2 = -((x1 * t2) - (y1 * t1)) / ((y1 * x2) - (x1 * y2))
    p1 = (t2 - (p2 * y2)) / y1

    if p1.is_integer() and p2.is_integer():
        return round((p1 * 3) + p2)
    return 0


print("pt1:", sum(tokensForGame(game, False) for game in games))
print("pt2:", sum(tokensForGame(game, True) for game in games))
