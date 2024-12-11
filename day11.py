stones = tuple(map(int, (open("input.txt").read().split())))


def changeStone(stone: int) -> int:
    if stone == 0:
        return [1]
    stone = str(stone)
    digits = len(stone)
    if digits % 2 == 0:
        half = digits // 2
        left, right = int(stone[:half]), int(stone[half:])
        return [left, right]
    else:
        return [int(stone) * 2024]


def calc(stone: int, step: int, steps: int, memo: dict) -> int:
    if step == steps:
        return 1

    key = hash((stone, step))
    if key in memo:
        return memo[key]
    changed = changeStone(stone)
    memo[key] = sum(calc(stone, step + 1, steps, memo) for stone in changed)
    return memo[key]


print("pt1:", sum(calc(stone, 0, 25, {}) for stone in stones))
print("pt2:", sum(calc(stone, 0, 75, {}) for stone in stones))
