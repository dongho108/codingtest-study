n, m = list(map(int, input().split()))
frames = [list(map(int, input())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
result = 0


def dfs(x, y):
    if not (0 <= x < n and 0 <= y < m):
        return False
    if frames[x][y] == 0:
        frames[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False
    # visited[x][y] = True
    # dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # for d in dir:
    #     nx = x + d[0]
    #     ny = y + d[1]
    #     if not (0 <= nx < n and 0 <= ny < m):
    #         continue
    #     # print(nx, ny)
    #     if frames[nx][ny] == "0" and not visited[nx][ny]:
    #         dfs(nx, ny)


def print2Arr(arr):
    for row in arr:
        print(row, end=' \n')
    print()



for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
        # if frames[i][j] == "0" and not visited[i][j]:
        #     result += 1
        #     dfs(i, j)

print(result)

"""
4 5
00110
00011
11111
00000
"""

