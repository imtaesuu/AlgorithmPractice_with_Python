##### My code #####
##### Runtime 84ms, Memory 29820KB #####

import sys
input = sys.stdin.readline
N = int(input())
graph = [list(map(int,input().rstrip())) for _ in range(N)]

def dfs(x, y):
    if x < 0 or x >= N or \
        y < 0 or y >= N or \
        graph[x][y] == 0:
            return 0
    
    graph[x][y] = 0
    cnt = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
         
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i] 
        cnt += dfs(nx, ny)    
    return cnt

res = []
for x in range(N):
    for y in range(N):
        if graph[x][y] == 1:
            res.append(dfs(x, y))
            
print(len(res))
print(*sorted(res), sep = '\n')