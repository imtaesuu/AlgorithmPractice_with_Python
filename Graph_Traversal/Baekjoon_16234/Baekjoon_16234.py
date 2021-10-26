##### My code #####
##### Runtime 2032ms, Memory 141920KB #####

import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
move = False

def open_graph(x, y, visited, table):    
    global move
    q = deque()
    q.append((x, y))
    country = table[x][y]
    cnt = 1
    visited[x][y] = True
    temp = []
    temp.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]:
                continue
            
            if 0<=nx<N and 0<=ny<N and \
               L<=abs(table[x][y] - table[nx][ny])<=R:         
                    temp.append((nx, ny))
                    cnt += 1
                    country += table[nx][ny]
                    q.append((nx, ny))
                    visited[nx][ny] = True
    
    if cnt > 1:
        move = True
        num = int(country / cnt)
        for i, j in temp:
            table[i][j] = num
          
res = 0
while True:
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                open_graph(i, j, visited, graph)
    if move:
        res += 1
        move = False
    else:
        break
print(res)