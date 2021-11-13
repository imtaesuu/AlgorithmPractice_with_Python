##### My code #####
##### Runtime 2636ms, Memory 48640KB #####

import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

R, C = map(int, input().split())
graph, J, F = [], [], []
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False]*C for _ in range(R)]

for i in range(R):
    graph.append(list(input()))
    for j in range(C):
        if graph[i][j] == 'J': J += [i, j]
        elif graph[i][j] == 'F': F.append((i, j))

def bfs():
    q = deque()
    q.append((J[0], J[1], 'J'))
    graph[J[0]][J[1]] = 1
    
    for i, j in F:
        q.append((i, j, 'F'))
        visited[i][j] = True
    
    while q:
        x, y, check = q.popleft()
        if check == 'J' and graph[x][y] != 'F':
            if (x == 0 or x == R - 1) or (y == 0 or y == C - 1):
                return graph[x][y]
        
        for i in range(4):
            nx, ny = x + move[i][0], y + move[i][1]
            if 0<=nx<R and 0<=ny<C:
                if check == 'J' and graph[x][y] != 'F' and graph[nx][ny] == '.':
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny, 'J'))
                elif check == 'F' and graph[nx][ny] != '#' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    graph[nx][ny] = 'F'
                    q.append((nx, ny, 'F'))
    return 'IMPOSSIBLE'
print(bfs())