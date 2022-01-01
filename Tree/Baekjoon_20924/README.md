## - Baekjoon 20924 트리의 기둥과 가지 - [Link](https://www.acmicpc.net/problem/20924)
● 입력  
> 9 1  
1 2 5  
2 3 4  
3 4 2   
2 5 5  
1 6 8  
1 7 6  
7 8 7  
7 9 1  

● 출력
> 0 13   

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Tree/Baekjoon_20924/Baekjoon_20924.py)

```python
import sys
from collections import defaultdict
input = sys.stdin.readline

# tree 만들기
# defaultdict -> dict를 사용하여 방문 따로 등록하지 않아도 되는 단방향 트리 만들 수 있음 
N, R = map(int, input().split())
tree = defaultdict(dict)
for _ in range(N-1):
    a, b, d = map(int, input().split())
    tree[a][b] = d
    tree[b][a] = d

# 가지치기 시작하는 노드를 찾기
gnode, gdstc = R, 0
while len(tree[gnode]) == 1:
    node, dstc = list(tree[gnode].items())[0]
    # del을 이용하여 반대로 향하는 간선을 삭제
    del tree[node][gnode]
    gdstc += dstc
    gnode = node

# dfs를 이용하여 최대값 구함
if not tree[gnode]:
    print(gdstc, 0)
else:
    stack = [(gnode, 0)]
    maxbranch = 0
    while stack:
        node, dstc = stack.pop()
        
        if not tree[node]:
            if maxbranch < dstc:
                maxbranch = dstc
            continue
        
        for n, d in tree[node].items():
            del tree[n][node]
            stack.append((n, dstc+d))
    
    print(gdstc, maxbranch)

##### Python 3 #####
##### Runtime 804ms, Memory 124852KB #####
```

## - **How To Solve**
- 문제만 이해하면 쉬운 구현문제, 양방향으로 트리를 만들 수 밖에 없는 상황에는 트리 최적화가 중요
- 기존 tree에 dict 안에 list를 넣는 방법말고 dict를 넣어 방향이 결정된 간선 외의 다른 간선을 del로 삭제하게 함
- 여기서는 stack을 이용하였지만, 재귀구조로 구현하는 법도 연습해야함