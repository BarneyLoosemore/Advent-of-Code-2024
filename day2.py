from typing import List


file = open("input.txt")
reports = [list(map(int, line.split())) for line in file.read().splitlines()]


def isSafe(report: List[int]) -> bool:
    changes = [level - report[i - 1] for i, level in enumerate(report) if i != 0]
    increasing = all(change > 0 for change in changes)
    decreasing = all(change < 0 for change in changes)
    changesValid = all(1 <= abs(change) <= 3 for change in changes)
    return changesValid and (increasing or decreasing)


def isSafeWithDampener(report: List[int]) -> bool:
    return any([isSafe(report[:i] + report[i + 1 :]) for i in range(len(report))])


safeReportCount = len([report for report in reports if isSafe(report)])
safeReportCountWithDampener = len(
    [report for report in reports if isSafeWithDampener(report)]
)

print(safeReportCount)
print(safeReportCountWithDampener)


file.close()
