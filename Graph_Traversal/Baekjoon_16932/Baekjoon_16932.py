##### My code #####
##### Runtime 3976ms, Memory 254516KB #####

import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()
N, M = map(int, input().split())
graph, zero = [], []
move = [(-1 ,0), (1, 0), (0, -1), (0, 1)]
group = [[[0]*2 for _ in range(M)] for _ in range(N)]

for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(M):
        if graph[i][j] == 0:
            zero.append((i, j))
            
def set_group(x, y, visited, g):
    q = deque([(x, y)])
    visited[x][y] = True
    tmp = [(x, y)]
    cnt = 1
    
    while q:
        x, y = q.popleft()
        for n in move:
            nx, ny = x + n[0], y + n[1]    
            if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 1 and not visited[nx][ny]:
                q.append((nx, ny))
                tmp.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1
                
    for i, j in tmp: 
        group[i][j][0] = g
        group[i][j][1] = cnt

visited, g = [[False]*M for _ in range(N)], 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and not visited[i][j]:
            g += 1
            visited[i][j] = True
            set_group(i, j, visited, g)

res = 1
for x, y in zero:
    num, v_group = 1, []
    for n in move:
        nx, ny = x + n[0], y + n[1]   
        if 0<=nx<N and 0<=ny<M and group[nx][ny][0] not in v_group:
            v_group.append(group[nx][ny][0])
            num += group[nx][ny][1]
    res = max(res, num)
print(res)