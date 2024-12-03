import re

mulPattern = re.compile(r"mul\((\d+),(\d+)\)")
mulPatternWithInstructions = re.compile(
    r"mul\((\d+),(\d+)\)|do\(\)|don'(.)\(\)"
)  # Is there a better way to do this? I'm terrible at Regex..


mulSum = sum(
    [int(x) * int(y) for x, y in re.findall(mulPattern, open("input.txt").read())]
)


mulSumWithInstructions = 0
mulEnabled = True
for seq in re.findall(mulPatternWithInstructions, open("input.txt").read()):
    match seq:
        case ("", "", "t"):
            mulEnabled = False
        case ("", "", ""):
            mulEnabled = True
        case (x, y, ""):
            if mulEnabled:
                mulSumWithInstructions += int(x) * int(y)

print(mulSum)
print(mulSumWithInstructions)
