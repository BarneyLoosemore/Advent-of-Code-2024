from typing import List


rules, updates = open("input.txt").read().split("\n\n")
rules = [list(map(int, rule.split("|"))) for rule in rules.splitlines()]
updates = [list(map(int, update.split(","))) for update in updates.splitlines()]


pageRuleMap = {}

for pageX, pageY in rules:
    if pageX in pageRuleMap:
        pageRuleMap[pageX].append(pageY)
    else:
        pageRuleMap[pageX] = [pageY]


def isValid(update: List[int]) -> bool:
    shouldComeAfter = []
    for n in range(len(update) - 1, -1, -1):
        page = update[n]
        if page in shouldComeAfter:
            return False
        if page in pageRuleMap:
            pageRules = pageRuleMap[page]
            shouldComeAfter += pageRules
    return True


def sortInvalid(update: List[int]) -> None:
    for n in range(len(update) - 1):
        for i in range(len(update) - n - 1):
            page = update[i]
            nextPage = update[i + 1]
            nextPageRules = pageRuleMap[nextPage] if nextPage in pageRuleMap else []
            if page in nextPageRules:
                update[i], update[i + 1] = nextPage, page


validSum = 0
invalidSum = 0

for update in updates:
    if isValid(update):
        validSum += update[len(update) // 2]
    else:
        sortInvalid(update)
        invalidSum += update[len(update) // 2]


print("pt1: ", validSum)
print("pt2: ", invalidSum)
