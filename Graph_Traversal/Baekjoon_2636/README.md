## - Baekjoon 2636 치즈 문제 - [Link](https://www.acmicpc.net/problem/2636)
● 입력  
> 13 12  
0 0 0 0 0 0 0 0 0 0 0 0  
0 0 0 0 0 0 0 0 0 0 0 0  
0 0 0 0 0 0 0 1 1 0 0 0  
0 1 1 1 0 0 0 1 1 0 0 0  
0 1 1 1 1 1 1 0 0 0 0 0  
0 1 1 1 1 1 0 1 1 0 0 0  
0 1 1 1 1 0 0 1 1 0 0 0  
0 0 1 1 0 0 0 1 1 0 0 0  
0 0 1 1 1 1 1 1 1 0 0 0  
0 0 1 1 1 1 1 1 1 0 0 0  
0 0 1 1 1 1 1 1 1 0 0 0  
0 0 1 1 1 1 1 1 1 0 0 0  
0 0 0 0 0 0 0 0 0 0 0 0

● 출력
> 3  
5

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Graph_Traversal/Baekjoon_2636/Baekjoon_2636.py)

```python
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
res, num = 0, 0
graph = []
for _ in range(N):
    temp = list(map(int, input().split()))
    graph.append(temp)

def bfs(x, y, graph, visited):
    q = deque()
    q.append((x, y))
    dx, dy = [-1, 1, 0, 0], [0, 0, -1 ,1]
    visited[x][y] = True
    trapped = True
    ls = []
    cnt = 0
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
    
            if nx < 0 or nx >= N or \
                ny < 0 or ny >= M:
                    trapped = False
                    continue
            
            if visited[nx][ny]: continue
            
            if graph[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = True
            elif graph[nx][ny] == 1:
                ls.append((nx, ny))
                cnt += 1
                visited[nx][ny] = True
    if not trapped:
        for i, j in ls:
            graph[i][j] = 0
    return cnt

while True:
    visited = [[False] * M for _ in range(N)]
    temp = bfs(0, 0, graph, visited)
    num += 1
    if temp == 0:
        print(num - 1, res, sep='\n')
        break
    res = temp
	
##### My code #####
##### Runtime 132ms, Memory 33008KB #####
```

## - **How To Solve**
- **bfs**으로 깔끔하게 풀린 문제, 치즈안에 구멍은 공기로 취급 안하도록 풀었다.
- 치즈가 없는 부분을 **bfs**돌려 밖으로 빠져나갈 수 없으면 구멍취급
- 사실상 가장자리 부분은 치즈가 없기 때문에 그냥 (0, 0) 좌표만 넣고 돌려도 풀리는 문제
- trapped 여부도 사실은 필요가 없다.
- 모두 녹기 전 남아있는 치즈조각의 수를 알아야 하기 때문에 res에 temp를 용하여 전 시간 개수를 저장