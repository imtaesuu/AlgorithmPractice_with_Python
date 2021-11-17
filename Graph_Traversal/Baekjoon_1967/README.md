## - Baekjoon 1967 트리의 지름 문제 - [Link](https://www.acmicpc.net/problem/1967)
● 입력  
> 12  
1 2 3  
1 3 2  
2 4 5  
3 5 11  
3 6 9  
4 7 1  
4 8 7  
5 9 15  
5 10 4  
6 11 6  
6 12 10

● 출력
> 45

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Graph_Traversal/Baekjoon_1967/Baekjoon_1967.py)

```python
import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()
n = int(input())
tree = {i+1 : [] for i in range(n)}
res = 0
for _ in range(n-1):
    parent, child, weight = map(int, input().split())
    if parent not in tree[child]:
        tree[parent] += [(child, weight)]
        tree[child] += [(parent, weight)]

def dfs(node, visited):
    global res
    stack = [(node, 0)]
    length = 0
    while stack:
        node, dstc = stack.pop()
        if not visited[node]:
            visited[node] = True
            for val in tree[node]:
                if visited[val[0]]:
                    res = max(res, dstc)
                    continue
                stack.append((val[0], val[1] + dstc))      

for i in range(n):
    visited = [False]*(n+1)
    dfs(i+1, visited)
print(res)

##### My code #####
##### Runtime 5876ms, Memory 226640KB #####
```

## - **How To Solve**
- 문제는 쉬운데 설명을 조금 부족하게 함, 가중치의 합이 지름이라는 말을 숨겼다.
- 그냥 설명에 현혹되지 말고 임의의 두 노드 사이의 가중치들의 합 중 가장 큰 값을 구하는 문제
- **dfs**로 스택에 노드와 이동할 때마다의 합을 저장한 길이를 넣으면 된다.
- 처음에는 재귀로 돌려보려다 시간초과, 그냥 스택을 사용하였고 pypy로 실행했다.