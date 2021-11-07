##### My code #####
##### Runtime 700ms, Memory 163688KB #####

import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

K = int(input())
W, H = map(int, input().split())
graph = []
for _ in range(H):
    graph.append(list(map(int, input().split())))
visited = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
hdx, hdy = [-2, -1, -2, -1, 2, 1, 2, 1], [-1, -2, 1, 2, -1, -2, 1, 2]

def bfs():
    q = deque([(0, 0, 0)])
    while q:
        x, y, z = q.popleft()        
        for i in range(8):
            hx, hy = x + hdx[i], y + hdy[i]
            if z+1>K: break
            if 0<=hx<H and 0<=hy<W and graph[hx][hy] == 0 and visited[hx][hy][z+1] == 0:
                visited[hx][hy][z+1] = visited[x][y][z] + 1
                if hx == H-1 and hy == W-1:
                    return visited[hx][hy][z+1]
                q.append((hx, hy, z+1))
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]         
            if 0<=nx<H and 0<=ny<W and graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                if nx == H-1 and ny == W-1:
                    return visited[nx][ny][z]
                q.append((nx, ny, z))
    return -1

if H == 1 and W == 1:
    print(0)
else:
    print(bfs())