import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

graph = [] 
block = []
dx = [-1 ,1 ,0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]
visited = [[False]*8 for _ in range(8)]

graph = [['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['#', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '#', '#', '#', '#', '#', '#', '#'],
         ['#', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.']]

for i in range(8):
    # graph.append(list(input()))
    for j in range(8):
        if graph[i][j] == '#':
            block.append((i, j))


        
# print(*graph, sep = '\n')
# print(block)

def move_block():
    tmp = []
    while block:
        x, y = block.pop()
        visited[x][y] = False
        if x+1 >= 8:
            graph[x][y] = '.'
        else:
            graph[x][y] = '.'
            graph[x+1][y] = '#'
            tmp.append((x+1, y))
    for x, y in tmp:
        block.append((x, y))
    print(*graph, sep = '\n')

def bfs():
    q = deque([(7, 0, 0)])
    prev = 0
    while q:
        x, y, t = q.popleft()
        
        if t > prev and len(block) > 0:
            print(t, prev)
            move_block()
            prev += 1
        visited[x][y] = True
        
        if graph[x][y] == '#':
            continue
        
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0<=nx<8 and 0<=ny<8 and graph[nx][ny] != '#' and not visited[nx][ny]:
                if nx == 0 and ny == 7:
                    return 1
                graph[nx][ny] = 1
                graph[x][y] = '.'
                q.append((nx, ny, t+1))
    
    return 0

print(bfs())     
        
        
        