##### My code #####
##### Runtime 808ms, Memory 92448KB #####

import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()
graph, block = [], deque()
dx = [-1 ,1 ,0, 0, -1, -1, 1, 1, 0]
dy = [0, 0, -1, 1, 1, -1, 1, -1, 0]
visited = [[False]*8 for _ in range(8)]

for i in range(8):
    graph.append(list(input()))
    for j in range(8):
        if graph[i][j] == '#':
            block.append((i, j))

# 벽이 한칸씩 내려오게 함
def move_block():
    tmp = []
    while block:
        x, y = block.pop()
        if x == 7:
            graph[x][y] = '.'
        else:
            graph[x][y] = '.'
            graph[x+1][y] = '#'
            tmp.append((x+1, y))
    for x, y in tmp:
        block.appendleft((x, y))

# 9가지 이동을 bfs로 구현
def bfs():
    q = deque([(7, 0, 0)])
    prev = 0
    while q:
        x, y, t = q.popleft()
        if t > prev and len(block) > 0:
            move_block()
            prev += 1
        elif len(block) == 0:
            visited[x][y] = True
        
        if graph[x][y] == '#':
            continue
        
        for i in range(9):
            nx, ny = x + dx[i], y + dy[i]  
            if 0<=nx<8 and 0<=ny<8 and graph[nx][ny] != '#' and not visited[nx][ny]:
                if nx == 0 and ny == 7:
                    return 1
                graph[x][y] = '.'
                graph[nx][ny] = 1
                q.append((nx, ny, t+1))  
    return 0

print(bfs())    