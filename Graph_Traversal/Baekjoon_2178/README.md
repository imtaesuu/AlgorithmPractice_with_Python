## - Baekjoon 2178 미로 탐색 문제 - [Link](https://www.acmicpc.net/problem/2178)
● 입력  
> 4 6  
101111  
101010  
101011  
111011

● 출력
> 15

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Graph_Traversal/Baekjoon_1325/Baekjoon_1325.py)

```python
##### My code #####
##### Runtime 108ms, Memory 31900KB #####

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
graph = []

for _ in range(N):
    graph.append(list(input().rstrip()))

def bfs(x, y):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or \
              ny < 0 or ny >= M:
                continue

            if graph[nx][ny] == '1':
                graph[nx][ny] = int(graph[x][y]) + 1
                q.append((nx, ny))

                return graph[N - 1][M - 1]

print(bfs(0, 0))
	
##### My code #####
##### Runtime 108ms, Memory 31900KB #####
```

## - **How To Solve**
- **bfs**를 이용하는 최단거리 구하기 문제
- 현재 위치에서 상하좌우로 탐색한 다음, 그곳이 길이라면 그 인덱스에 현재거리 + 1을 넣어준다.
- 최단거리를 처음 맞본다면 생각보다 까다로운 문제