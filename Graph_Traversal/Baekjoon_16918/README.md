## - Baekjoon 16918 붐버맨 문제 - [Link](https://www.acmicpc.net/problem/16918)
● 입력  
>6 7 3  
.......  
...O...  
....O..  
.......  
OO.....  
OO.....

● 출력
>OOO.OOO  
OO...OO  
OOO...O  
..OO.OO  
...OOOO  
...OOOO

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Graph_Traversal/Baekjoon_16918/Baekjoon_16918.py)

```python
import sys
from collections import deque
input = sys.stdin.readline
R, C, N = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(R)]
queue = deque()

def fill():
    for i in range(R):
        for j in range(C):
            if graph[i][j] == '.':
                graph[i][j] = 'O'
def find():
    for i in range(R):
        for j in range(C):
            if graph[i][j] == 'O':
                queue.append((i, j))   
def explosion():
    while queue:
        x, y = queue.popleft()
        graph[x][y] = '.'
        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<R and 0<=ny<C:
                graph[nx][ny] = '.'
 
for i in range(N - 1):
    if i % 2 == 1:
        explosion()
    else:
        find()
        fill()
for i in graph:
    for j in i:
        print(j, end = "")
    print()
	
##### My code #####
##### Runtime 3852ms, Memory 34228KB #####
```

## - **How To Solve**
- 문제의 요지를 정확히 파악하지 못해서 꽤 시간이 걸린문제
- 초반에는 시간초과, 나중에는 구현실패로 꽤 애를 먹었다.
- 1초가 지날 때 마다를 각각 구현해보니, 1초마다 폭탄 생성과 터짐만을 반복하다는 걸 알았다.
- 규칙만 알고나면 단순히 생성과 폭발을 반복하면 되는 단순한 문제
- 문제 존재하는 규칙을 알아보는 습관을 가지자