import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
graph = [[0, 0, 0, 0, 0,],
         [0, 0, 1, 0, 0,],
         [0, 0, 0, 0, 0,],
         [0, 0, 0, 0, 0,]]
# graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for i in range(N)]
H, W, Sr, Sc, Fr, Fc = map(int, input().split())

#벽 좌표 미리 담아두기
wall = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1: wall.append((i,j))

#직사각형 배치 가능 여부 확인
def is_set(x, y):
    if x+H-1 >= N or y+W-1 >= M:
        return False
    
    for h, w in wall:
        if x<=h<=x+H-1 and y<=w<=y+W-1:
            return False
    return True

#직사각형 이동
def move():
    q = deque()
    q.append((Sr-1, Sc-1))
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        
        if x == Fr-1 and y == Fc-1:
            return visited[x][y]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]          
            if 0<=nx<N and 0<=ny<M and is_set(nx, ny) and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
                print(*visited, sep = '\n')
                print()
    
    return -1
                        
print(move())