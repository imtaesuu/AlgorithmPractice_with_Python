import sys
from collections import deque
from pprint import pprint
#sys.setrecursionlimit()
input = sys.stdin.readline

R, C, N = map(int, input().split())
graph = []
res = []
queue = deque()

for i in range(R):
    graph.append(list(map(str, input().split())))
    if j in range(C):
        if graph[i][j] == 'O':
            queue.append((i, j))
            
def bfs():
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0<=nx< R and 0<=ny < C and \
                graph[nx][ny] != 'O':
                    graph[nx][ny] = 0

        