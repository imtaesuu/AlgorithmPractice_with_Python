## - Baekjoon 9489 사촌 - [Link](https://www.acmicpc.net/problem/9489)
● 입력  
> 10 15  
1 3 4 5 8 9 15 30 31 32  
12 9  
3 5 6 8 9 10 13 15 16 22 23 25  
10 4  
1 3 4 5 8 9 15 30 31 32  
0 0

● 출력
> 5  
1  
0   

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Tree/Baekjoon_9489/Baekjoon_9489.py)

```python
import sys
from collections import defaultdict, deque
input = sys.stdin.readline

# 부모를 찾는 함수
def find_parents(node):
    for parents, child in tree.items():
        if node in child:
            return parents
    return 0

while True:
    N, K = map(int, input().split())
    if N == 0 and K == 0:
        break
    
    elements = list(map(int, input().split()))
    tree = defaultdict(set)
    
    # 부모를 바꿔주기 위해서 부모 큐와 이전 값을 넣어줄 변수를 만들어준다
    parents = deque([elements[0]])
    prev = parents[0]
    parent = 0
    
    for e in elements[1:]:
        # 문제의 조건에 따라 prev + 1 < e 면 부모를 바꿔준다
        if prev + 1 < e:
            parent = parents.popleft()
        
        parents.append(e)
        tree[parent].add(e)
        prev = e

    p1 = find_parents(K)
    if not p1:
        print(0)
        continue
    p2 = find_parents(p1)
    if not p2:
        print(0)
        continue

    # 할아버지가 같은 자식의 수를 다 더해줌
    res = 0
    for t in tree[p2]:
        if t != p1:
            res += len(tree[t])
    print(res)

##### PyPy3 #####
##### Runtime 596ms, Memory 135192KB #####
```

## - **How To Solve**
- 트리를 만들어주고 사촌의 수를 파악하는 단순한 문제
- 처음에 그저 같은 레벨의 노드의 수가 답인 줄 알았는데, 그게 아니고 할어버지 노드가 같은 자식들의 수를 파악하는 거였음
- 본인은 위 처럼 두번의 함수를 통해서 할아버지를 구했지만, 그냥 할아버지 노드가 같은 노드의 수를 바로 파악하는 방법도 있음