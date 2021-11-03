## - Baekjoon 18513 샘터 문제 - [Link](https://www.acmicpc.net/problem/18513)
● 입력  
> 2 5  
0 3

● 출력
> 6

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Graph_Traversal/Baekjoon_18513/Baekjoon_18513.py)

```python
import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

N, K = map(int, input().split())
sprs = deque()
visited = set()

for i in list(map(int, input().split())):
    sprs.append((i, 1))
    visited.add(i)

res, house = 0, 0
while sprs:
    x, num = sprs.popleft()
    for dx in [1, -1]:
        if x+dx in visited:
            continue
        sprs.append((x+dx, num+1))
        visited.add(x+dx)
        res += num
        house += 1
        if house == K:
            sprs = []
            break
print(res)        
	
##### My code #####
##### Runtime 316ms, Memory 60376KB #####
```

## - **How To Solve**
- **bfs**로 풀었던 문제, 최단거리랑 비슷한 유형이다.
- visited에 미리 테이블로 방문값을 만들어 보았는데 크기가 너무 커 타임아웃
- in을 사용하면 **O(n)** 이라 조금 불안했는데 set을 사용하여 중복 해소
- 사실 이렇게 풀릴 줄은 몰랐다, in을 쓰면 당연히 타임아웃 될줄 알았는데...
- 테스트 해보고 안되는 것이 하기전에 스스로 판단하는 것보다 훨 낫다는 걸 느낌