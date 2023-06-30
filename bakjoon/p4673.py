def solution():
    selfNumbers = [[False] for _ in range(10001)]
    selfNumbers[0][0] = True
    while True:
        selfNumber = findNextSelfNumber(selfNumbers)
        if selfNumber == 0:
            break
        j = selfNumber
        print(selfNumber)
        while j <= 10000:
            selfNumbers[j][0] = True
            j = computeSelfNumber(j)


def computeSelfNumber(j):
    total = 0
    total += j
    for c in str(j):
        total += int(c)
    return total


def findNextSelfNumber(selfNumbers):
    for i, val in enumerate(selfNumbers):
        if not selfNumbers[i][0]:
            return i
    return 0


solution()