##### My code #####
##### Runtime 6084ms, Memory 174472KB #####

import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs():    
    visited[0][0][0] =  1
    q = deque([(0, 0, 0)])
    while q:
        x, y, case = q.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][case]
        for i in range(4):
            nx, ny = x + move[i][0], y + move[i][1]
            if 0<=nx<N and 0<=ny<M:
                if case == 0 and graph[nx][ny] == 1:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    q.append((nx, ny, 1))
                elif graph[nx][ny] == 0 and visited[nx][ny][case] == 0:
                    visited[nx][ny][case] = visited[x][y][case] + 1
                    q.append((nx, ny, case))
    return -1
print(bfs())