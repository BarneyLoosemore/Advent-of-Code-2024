from typing import List


lines = [line.split(":") for line in open("input.txt").read().splitlines()]
equations = [(int(test), list(map(int, nums.split()))) for test, nums in lines]

ADD = "ADD"
MULTIPLY = "MULTIPLY"


def calculate(nums: List[int], operator: str, curr: int, target: int):
    if len(nums) == 1:
        [num] = nums
        return curr * num == target or curr + num == target
    num, *nums = nums
    match operator:
        case "ADD":
            curr += num
        case "MULTIPLY":
            curr = curr * num
        case _:
            curr = num  # for initial call, when no operator set

    return calculate(nums, ADD, curr, target) or calculate(nums, MULTIPLY, curr, target)


calibration = sum(
    [target if calculate(nums, None, 0, target) else 0 for target, nums in equations]
)


CONCATENATE = "CONCATENATE"


def calculateWithConcat(nums: List[int], operator: str, curr: int, target: int):
    if len(nums) == 1:
        [num] = nums
        return (
            curr * num == target
            or curr + num == target
            or int(str(curr) + str(num)) == target
        )
    num, *nums = nums
    match operator:
        case "ADD":
            curr += num
        case "MULTIPLY":
            curr = curr * num
        case "CONCATENATE":
            curr = int(str(curr) + str(num))
        case _:
            curr = num  # for initial call, when no operator set

    return (
        calculateWithConcat(nums, ADD, curr, target)
        or calculateWithConcat(nums, MULTIPLY, curr, target)
        or calculateWithConcat(nums, CONCATENATE, curr, target)
    )


calibrationWithConcat = sum(
    [
        target if calculateWithConcat(nums, None, 0, target) else 0
        for target, nums in equations
    ]
)


print("pt1: ", calibration)
print("pt2: ", calibrationWithConcat)
