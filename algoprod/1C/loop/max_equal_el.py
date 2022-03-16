x = int(input())
maxElem = x
maxNum = 0
while x != 0:
    if x == maxElem:
        maxNum += 1
    elif x > maxElem:
        maxElem = x
        maxNum = 1
    x = int(input())

print(maxNum)