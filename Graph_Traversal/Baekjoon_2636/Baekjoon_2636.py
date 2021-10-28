##### My code #####
##### Runtime 132ms, Memory 33008KB #####

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
res, num = 0, 0
graph = []
for _ in range(N):
    temp = list(map(int, input().split()))
    graph.append(temp)

def bfs(x, y, graph, visited):
    q = deque()
    q.append((x, y))
    dx, dy = [-1, 1, 0, 0], [0, 0, -1 ,1]
    visited[x][y] = True
    trapped = True
    ls = []
    cnt = 0
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
    
            if nx < 0 or nx >= N or \
                ny < 0 or ny >= M:
                    trapped = False
                    continue
            
            if visited[nx][ny]: continue
            
            if graph[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = True
            elif graph[nx][ny] == 1:
                ls.append((nx, ny))
                cnt += 1
                visited[nx][ny] = True
    if not trapped:
        for i, j in ls:
            graph[i][j] = 0
    return cnt

while True:
    visited = [[False] * M for _ in range(N)]
    temp = bfs(0, 0, graph, visited)
    num += 1
    if temp == 0:
        print(num - 1, res, sep='\n')
        break
    res = temp