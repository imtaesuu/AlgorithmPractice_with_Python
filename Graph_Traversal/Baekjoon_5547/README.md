## - Baekjoon 5547 일루미네이션 문제 - [Link](https://www.acmicpc.net/problem/2667)
● 입력  
> 8 4  
0 1 0 1 0 1 1 1  
0 1 1 0 0 1 0 0  
1 0 1 0 1 1 1 1  
0 1 1 0 1 0 1 0

● 출력
> 64

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Graph_Traversal/Baekjoon_5547/Baekjoon_5547.py)

```python
##### My code #####
##### Runtime 108ms, Memory 31900KB #####

import sys
from collections import deque
input = sys.stdin.readline

W, H = map(int, input().split())
q =  deque()
graph = [list(map(int, input().split())) for _ in range(H)]
dx = [[0, 0, 1, 1, -1, -1], [0, 0, 1, 1, -1, -1]]
dy = [[-1, 1, 0, 1, 0, 1], [-1 ,1, 0, -1, 0, -1]]
res = 0
def cnt_wall(x, y):
    global res
    q.append((x, y))
    while q:
        x, y = q.popleft()
        d = x%2
        for i in range(6):
            nx, ny = x + dx[d][i], y + dy[d][i] 
            if nx < 0 or nx >= H or \
                ny < 0 or ny >= W or graph[nx][ny] == -1:
                    res += 1
            elif 0<=nx<H and 0<=ny<W and \
                graph[nx][ny] == 1:
                    graph[nx][ny] = '1'
                    q.append((nx, ny))

def change_wall(x, y):
    trapped = True
    l = []
    q.append((x, y))
    while q:
        x, y = q.popleft()
        l.append((x, y))
        d = x%2
        for i in range(6):
            nx, ny = x + dx[d][i], y + dy[d][i] 
            if nx < 0 or nx >= H or \
                ny < 0 or ny >= W:
                    trapped = False
            elif 0<=nx<H and 0<=ny<W and \
                graph[nx][ny] == 0:
                    graph[nx][ny] = '0'
                    q.append((nx, ny))
    if not trapped:
        for i, j in l:
            graph[i][j] = -1                   

for i in range(H):
    for j in range(W):
        if graph[i][j] == 0:
            graph[i][j] = '0'
            change_wall(i, j)
for i in range(H):
    for j in range(W):
        if graph[i][j] == 1:
            graph[i][j] = '1'
            cnt_wall(i, j)
print(res)
	
##### My code #####
##### Runtime 132ms, Memory 32036KB #####
```

## - **How To Solve**
- **bfs**를 활용하여 무지성으로 구현한 문제
- 내벽은 카운팅 하면 안되기 때문에 생각보다 까다로운 문제
- -1을 카운팅하게 하고, 내벽은 따로 -1이 아니게 하면된다.
- **bfs**로 탈출구 즉, W H 범위 내로 나갈 수 있을 경우 내벽이 아니도록 구현했다
- 조금 무지성으로 구현한 바, 코드가 좀 지저분하다. 나중에 시간 남을 때 최적화 하자