left = []
right = []
for line in open(0).readlines():
    leftNum, rightNum = [int(num) for num in line.split()]
    left.append(int(leftNum))
    right.append(int(rightNum))

left.sort()
right.sort()

distance = sum(abs(leftNum - rightNum) for leftNum, rightNum in zip(left, right))
score = sum(right.count(leftNum) * leftNum for leftNum in left)

print(distance)
print(score)
