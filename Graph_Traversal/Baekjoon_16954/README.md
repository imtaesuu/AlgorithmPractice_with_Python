## - Baekjoon 16954 움직이는 미로 탈출 문제 - [Link](https://www.acmicpc.net/problem/16954)
● 입력  
>........  
........  
........  
........  
#.......  
.#######  
#.......  
........

● 출력
> 0

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Graph_Traversal/Baekjoon_16954/Baekjoon_16954.py)

```python
import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()
graph, block = [], deque()
dx = [-1 ,1 ,0, 0, -1, -1, 1, 1, 0]
dy = [0, 0, -1, 1, 1, -1, 1, -1, 0]
visited = [[False]*8 for _ in range(8)]

for i in range(8):
    graph.append(list(input()))
    for j in range(8):
        if graph[i][j] == '#':
            block.append((i, j))

# 벽이 한칸씩 내려오게 함
def move_block():
    tmp = []
    while block:
        x, y = block.pop()
        if x == 7:
            graph[x][y] = '.'
        else:
            graph[x][y] = '.'
            graph[x+1][y] = '#'
            tmp.append((x+1, y))
    for x, y in tmp:
        block.appendleft((x, y))

# 9가지 이동을 bfs로 구현
def bfs():
    q = deque([(7, 0, 0)])
    prev = 0
    while q:
        x, y, t = q.popleft()
        if t > prev and len(block) > 0:
            move_block()
            prev += 1
        elif len(block) == 0:
            visited[x][y] = True
        
        if graph[x][y] == '#':
            continue
        
        for i in range(9):
            nx, ny = x + dx[i], y + dy[i]  
            if 0<=nx<8 and 0<=ny<8 and graph[nx][ny] != '#' and not visited[nx][ny]:
                if nx == 0 and ny == 7:
                    return 1
                graph[x][y] = '.'
                graph[nx][ny] = 1
                q.append((nx, ny, t+1))  
    return 0

print(bfs())    
	
##### My code #####
##### Runtime 808ms, Memory 92448KB #####
```

## - **How To Solve**
- 데크에 x, y 좌표 그리고 지나간 시간을 나타내는 t 값을 넣었고, t값이 전 시간값인 prev보다 클때마다 벽이 내려오게 했다.
- 단순히 graph가 . #로 바로 변하게끔 코딩하였고, visited는 벽이 존재하지 않을 때부터 True를 넣게 하도록 했다.
- 초반에 계속 틀렸었는데 문제를 똑바로 읽어보지 못하고 제자리에 있는 경우를 넣지 못하였다.
- 그것 외에는 생각보다 어렵지 않게 구현할 수 있었다. 코드를 좀더 간결하고 우아하게 쓸 수도 있을 것 같다.
- **bfs**를 이용하여 구현하는 단순한 문제였다. 단, 문제 조건을 자세히 보는 습관을 들여야겠다.