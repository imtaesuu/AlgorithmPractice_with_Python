## - Baekjoon 7576 토마토 1 문제 - [Link](https://www.acmicpc.net/problem/7576)
● 입력  
> 6 4  
0 0 0 0 0 0  
0 0 0 0 0 0  
0 0 0 0 0 0  
0 0 0 0 0 1

● 출력
> 8

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Graph_Traversal/Baekjoon_7576/Baekjoon_7576.pyy)

```python
import sys
from collections import deque

input = sys.stdin.readline
M, N = map(int, input().split())
graph = []
queue = deque()

for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))

def bfs():
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i] 
            if 0<=nx< N and 0<=ny< M and \
                graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
bfs()
res = 0
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
        res = max(res, j)
print(res - 1)
	
##### My code #####
##### Runtime 2480ms, Memory 98900KB #####
```

## - **How To Solve**
- 최소 거리를 구하는 문제랑 거의 동일한 **bfs** 문제
- 문제의 조건과 상황을 잘 파악해야한다.
- 간단한 문제였는데 괜히 더 깊게 생각해서 시간을 많이 잡아먹은 문제
- 무지성으로 **bfs**를 사용해도 어차피 미리 큐에 토마토 idx를 넣어주면 동시에 익는다.