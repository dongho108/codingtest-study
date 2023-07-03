n = int(input())
plans = input().split()

nowX = 1
nowY = 1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
move_types = ['D', 'R', 'U', 'W']

for plan in plans:
    for i, move_type in enumerate(move_types):
        if plan == move_type:
            nx = nowX + dx[i]
            ny = nowY + dy[i]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    nowX, nowY = nx, ny

print(nowY, nowX)