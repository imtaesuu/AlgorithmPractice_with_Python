import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())

# graph = [[list(map(int, input().split()))] for _ in range(N)]
graph = [[0, 0, 0, 0, 0, 0, 0],
         [0, 2, 4, 5, 3, 0, 0],
         [0, 3, 0, 2, 5, 2, 0],
         [0, 7, 6, 2, 4, 0, 0],
         [0, 0, 0, 0, 0, 0, 0]]
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y, visited, graph):
    q = deque([(x, y)])
    visited[x][y] = True
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + move[i][0], y + move[i][1]
            
            if 0<=nx<N and 0<=ny<M:
                if graph[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                elif graph[nx][ny] != 0: 
                    graph[nx][ny] -= 1
                    
                    if graph[nx][ny] <= 0:
                        visited[nx][ny] = True
                        graph[nx][ny] = 0
                elif graph[nx][ny] != 0 and not visited[nx][ny]:
                    q.append((nx, ny))

                        
                
        
        

while True:
    t = 0
    visited = [[False]*M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0 and not visited[i][j]:
                bfs(i, j, visited, graph)
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0 and not visited[i][j]:
                
    
    print(*graph, sep = '\n')