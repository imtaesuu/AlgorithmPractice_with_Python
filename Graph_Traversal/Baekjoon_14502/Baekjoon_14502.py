##### My code #####
##### Runtime 4912ms, Memory 34320KB #####

import sys, copy, itertools
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
empty, queue = [], deque()
res, graph = 0, []
        
def bfs(table, q):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]   
    while q:
        x, y = q.popleft()
        table[x][y] = -1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny<M and table[nx][ny] == 0:
                q.append((nx, ny))
                table[nx][ny] = -1
    cnt = 0
    for i in table:
        for j in i:
            if j == 0:
                cnt += 1
    return cnt
    
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(M):
        if graph[i][j] == 2:
            queue.append((i, j))
        elif graph[i][j] == 0:
            empty.append((i, j))   
    
case = list(itertools.combinations(empty, 3))
for l in case:
    table, q = copy.deepcopy(graph), copy.deepcopy(queue)
    for x, y in l:
        table[x][y] = 1  
    res = max(res, bfs(table, q))
print(res)