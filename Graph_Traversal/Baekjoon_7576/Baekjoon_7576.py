##### My code #####
##### Runtime 2480ms, Memory 98900KB #####

import sys
from collections import deque

input = sys.stdin.readline
M, N = map(int, input().split())
graph = []
queue = deque()

for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))

def bfs():
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i] 
            if 0<=nx< N and 0<=ny< M and \
                graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
bfs()
res = 0
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
        res = max(res, j)
print(res - 1)