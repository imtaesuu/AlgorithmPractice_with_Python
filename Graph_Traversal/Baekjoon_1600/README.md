## - Baekjoon 1600 말이 되고픈 원숭이 문제 - [Link](https://www.acmicpc.net/problem/1600)
● 입력  
> 1  
4 4  
0 0 0 0  
1 0 0 0  
0 0 1 0  
0 1 0 0

● 출력
> 4

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Graph_Traversal/Baekjoon_1600/Baekjoon_1600.py)

```python
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
	
##### My code #####
##### Runtime 700ms, Memory 163688KB #####
```

## - **How To Solve**
- 단순히 말의 hdx, hdy 값만 추가해서 **bfs** 돌리면 틀리는 문제
- 원숭이가 말의 움직임을 K번까지 쓸 수 있다면 한번도 안사용했을 때와 최대 K번까지 사용했을 때의 상황을 가정해야함
- 즉 세번 사용할 수 있으면 빵번, 한번, 두번, 세번 각각 사용했을 때의 상황 즉 테이블이 필요함
- 이러한 상황을 visited를 3차원으로 만들어 해결, 안면 큐에 횟수 값을 추가해서 판단해도됨
- 말의 움직임을 사용할 때는 항상 z+1 즉 다음 차원값으로 이동하게 구성
- 마지막 100%에서 실패로 막힌건 H=1, W=1 일때의 예외를 생각하지 못함