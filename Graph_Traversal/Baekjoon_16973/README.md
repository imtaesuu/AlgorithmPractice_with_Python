## - Baekjoon 16973 직사각형 탈출 문제 - [Link](https://www.acmicpc.net/problem/16973)
● 입력  
> 6 7  
0 0 0 0 0 0 0  
0 0 0 1 0 0 0  
0 0 0 0 0 0 0  
0 0 0 0 0 0 1  
0 0 1 0 0 0 0  
0 0 0 0 0 0 0  
2 3 1 1 5 5

● 출력
> 8

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Graph_Traversal/Baekjoon_16973/Baekjoon_16973.py)

```python
import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
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
    graph[Sr-1][Sc-1] = 1
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        if x == Fr-1 and y == Fc-1:
            return graph[x][y]-1
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]          
            if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 0 and is_set(nx, ny):
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
    return -1         
print(move())
	
##### My code #####
##### Runtime 768ms, Memory 147732KB #####
```

## - **How To Solve**
- **bfs**를 이용하는 최단거리 문제, is_set의 최적화에 타임아웃이 걸려있음
- 처음에는 직사각형의 좌표를 for문을 이용하여 일일이 벽이 있는지 체크했는데 타임아웃
- 직사각형의 크기를 알기 때문에 벽의 좌표를 미리 리스트에 담아두기
- 직사각형 좌표의 끝과 끝사이에 벽의 좌표가 존재하는지 체크