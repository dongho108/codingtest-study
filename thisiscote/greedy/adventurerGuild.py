n = int(input())
fears = list(map(int, input().split()))
fears.sort()

result = 0
group = []
for fear in fears:
    group.append(fear)
    if fear <= len(group):
        result += 1
        maxFear = 0
        group = []

print(result)