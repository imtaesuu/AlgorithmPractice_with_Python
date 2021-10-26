## - Baekjoon 16234 인구 이동 문제 - [Link](https://www.acmicpc.net/problem/16234)
● 입력  
>4 10 50  
10 100 20 90  
80 100 60 70  
70 20 30 40  
50 20 100 10

● 출력
>3

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Graph_Traversal/Baekjoon_16234/Baekjoon_16234.py)

```python
import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
move = False

def open_graph(x, y, visited, table):    
    global move
    q = deque()
    q.append((x, y))
    country = table[x][y]
    cnt = 1
    visited[x][y] = True
    temp = []
    temp.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]:
                continue
            
            if 0<=nx<N and 0<=ny<N and \
               L<=abs(table[x][y] - table[nx][ny])<=R:         
                    temp.append((nx, ny))
                    cnt += 1
                    country += table[nx][ny]
                    q.append((nx, ny))
                    visited[nx][ny] = True
    
    if cnt > 1:
        move = True
        num = int(country / cnt)
        for i, j in temp:
            table[i][j] = num
          
res = 0
while True:
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                open_graph(i, j, visited, graph)
    if move:
        res += 1
        move = False
    else:
        break
print(res)
	
##### My code #####
##### Runtime 2032ms, Memory 141920KB #####
```

## - **How To Solve**
- 멍청하게 **dfs** 풀려다 시간초과로 머리 터진 문제.
- **bfs**로 풀어야지 재귀로 시간초과 안나오고 풀 수 있다.
- 국경이 한번이라도 열렸으면 카운팅 해서 1보다 클 때 결과값에 +1을 반영하기
- visited 리스트를 만들어줘 전체 순환을 막아줬다.
- 딱봐도 시간 많이 잡아먹을 것 같은 문제는 항상 방문 리스트 만들어주기