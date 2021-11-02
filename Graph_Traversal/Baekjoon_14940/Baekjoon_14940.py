##### My code #####
##### Runtime 720ms, Memory 40216KB #####

import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
visited = [[0] * m for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
q = deque()

def bfs(x, y):
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]             
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] != 0 and not visited[nx][ny]:
                graph[nx][ny] = graph[x][y] + 1
                visited[nx][ny] = 1
                q.append((nx, ny))
     
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if graph[i][j] == 2:
                visited[i][j] = 1
                graph[i][j] = 0
                q.append((i, j))
                bfs(i, j)
            elif graph[i][j] == 1:
                graph[i][j] = -1

for i in range(n):
    print(' '.join(map(str, graph[i])))