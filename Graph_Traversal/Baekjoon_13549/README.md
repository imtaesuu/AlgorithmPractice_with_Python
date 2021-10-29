## - Baekjoon 13549 숨바꼭질 3 문제 - [Link](https://www.acmicpc.net/problem/13549)
● 입력  
>5 17

● 출력
>2

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Graph_Traversal/Baekjoon_13549/Baekjoon_13549.py)

```python
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [-1] * 100001
visited[N] = 0
q = deque()
q.append(N)

while q:
    x = q.popleft()
    if x == K:
        print(visited[x])
        break
    if x * 2 <= 100000 and visited[x*2] == -1:
        visited[x*2] = visited[x]
        q.appendleft(x*2)
    if x + 1 <= 100000 and visited[x+1] == -1:
        visited[x+1] = visited[x] + 1
        q.append(x+1)
    if x - 1 >= 0 and visited[x-1] == -1:
        visited[x-1] = visited[x] + 1
        q.append(x-1)
	
##### My code #####
##### Runtime 160ms, Memory 35492KB #####
```

## - **How To Solve**
- **bfs**를 사용하여 x*2, x+1, x-1 위치에 시간정보를 대입하여 탐색
- 특히 x*2는 시간 딜레마가 없는 즉, 0초만에 이루어지기 때문에 가중치를 둬 큐 맨 앞에 추가
- 단순하지만 처음 문제를 접했을 때 꽤 난이도가 있는 문제