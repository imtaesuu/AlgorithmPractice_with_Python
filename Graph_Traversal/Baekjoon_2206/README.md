## - Baekjoon 2206 벽 부수고 이동하기 문제 - [Link](https://www.acmicpc.net/problem/2206)
● 입력  
>6 4  
0100  
1110  
1000  
0000  
0111  
0000

● 출력
> 15

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Graph_Traversal/Baekjoon_2206/Baekjoon_2206.py)

```python
import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs():    
    visited[0][0][0] =  1
    q = deque([(0, 0, 0)])
    while q:
        x, y, case = q.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][case]
        for i in range(4):
            nx, ny = x + move[i][0], y + move[i][1]
            if 0<=nx<N and 0<=ny<M:
                if case == 0 and graph[nx][ny] == 1:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    q.append((nx, ny, 1))
                elif graph[nx][ny] == 0 and visited[nx][ny][case] == 0:
                    visited[nx][ny][case] = visited[x][y][case] + 1
                    q.append((nx, ny, case))
    return -1
print(bfs())

##### My code #####
##### Runtime 6084ms, Memory 174472KB #####
```

## - **How To Solve**
- 벽은 한번만 부술 수 있고, 부수지 않아도 되기때문에 visited를 3차원으로 만들어서 풀어야 되는 문제
- 솔직히 문제는 간단하고 구현 자체가 어려운 문제는 아니지만, 너무 깊게 생각하는 바람에 꽤 시간쓴 문제
- 처음에는 벽을 만날 때마다 이전 거리값, 새 visited값을 deepcopy하여 큐에 넘겼는데 당연히 시간초과
- 두번째는 벽을 부수지 않는 상태에서 벽을 만날경우 그 벽의 좌표와 거리값을 넘기고 나중에 for문으로 다시 bfs 돌림
- 하지만 벽이 굉장히 많을 경우에는 너무 많은 값을 받아 시간초과
- 그냥 visited를 3차원 배열로 벽을 부쉈을 때, 벽을 부수지 않을 때를 나눠서 q에 좌표와 상태를 넘김
- 처음에는 visited를 초기화 시키지 않으면 분명 문제가 생길 수 있을거라 생각했는데
- 사실 case가 1인것과 0인것이 각각 번갈아 가면서 bfs를 돌기 때문에 최단거리상 전혀 문제가 없었음