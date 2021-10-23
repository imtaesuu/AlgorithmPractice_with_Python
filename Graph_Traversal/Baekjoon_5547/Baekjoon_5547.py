##### My code #####
##### Runtime 132ms, Memory 32036KB #####

import sys
from collections import deque
input = sys.stdin.readline

W, H = map(int, input().split())
q =  deque()
graph = [list(map(int, input().split())) for _ in range(H)]
dx = [[0, 0, 1, 1, -1, -1], [0, 0, 1, 1, -1, -1]]
dy = [[-1, 1, 0, 1, 0, 1], [-1 ,1, 0, -1, 0, -1]]
res = 0
def cnt_wall(x, y):
    global res
    q.append((x, y))
    while q:
        x, y = q.popleft()
        d = x%2
        for i in range(6):
            nx, ny = x + dx[d][i], y + dy[d][i] 
            if nx < 0 or nx >= H or \
                ny < 0 or ny >= W or graph[nx][ny] == -1:
                    res += 1
            elif 0<=nx<H and 0<=ny<W and \
                graph[nx][ny] == 1:
                    graph[nx][ny] = '1'
                    q.append((nx, ny))

def change_wall(x, y):
    trapped = True
    l = []
    q.append((x, y))
    while q:
        x, y = q.popleft()
        l.append((x, y))
        d = x%2
        for i in range(6):
            nx, ny = x + dx[d][i], y + dy[d][i] 
            if nx < 0 or nx >= H or \
                ny < 0 or ny >= W:
                    trapped = False
            elif 0<=nx<H and 0<=ny<W and \
                graph[nx][ny] == 0:
                    graph[nx][ny] = '0'
                    q.append((nx, ny))
    if not trapped:
        for i, j in l:
            graph[i][j] = -1                   

for i in range(H):
    for j in range(W):
        if graph[i][j] == 0:
            graph[i][j] = '0'
            change_wall(i, j)
for i in range(H):
    for j in range(W):
        if graph[i][j] == 1:
            graph[i][j] = '1'
            cnt_wall(i, j)
print(res)