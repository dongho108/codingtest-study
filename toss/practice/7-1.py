from collections import deque

area = 0

def dfs(x, y, graph, n, m):
    global area

    # print(x, y)
    graph[x][y] += 1
    area += 1
    dir = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    for d in dir:
        nx = x + d[0]
        ny = y + d[1]
        if (0 <= nx < n and 0 <= ny < m) and graph[nx][ny] == 0:
            dfs(nx, ny, graph, n, m)


def bfs(x, y, graph, n, m):
    global area
    q = deque()
    graph[x][y] += 1
    area += 1
    q.append((x, y))
    while q:
        x, y = q.popleft()
        dir = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for d in dir:
            nx = x + d[0]
            ny = y + d[1]
            if (0 <= nx < n and 0 <= ny < m) and graph[nx][ny] == 0:
                q.append((nx, ny))
                graph[nx][ny] += 1
                area += 1


def solution():
    global area
    m, n, k = map(int, input().split())
    # 그림과는 반대로 본다.
    graph = [[0] * m for _ in range(n)]
    for i in range(k):
        x1, y1, x2, y2 = map(int, input().split())
        for j in range(x1, x2):
            for z in range(y1, y2):
                graph[j][z] += 1
    area_size = 0
    areas = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                area_size += 1
                bfs(i, j, graph, n, m)
                areas.append(area)
                area = 0

    areas.sort()
    print(area_size)
    print(" ".join(map(str, areas)))

solution()
