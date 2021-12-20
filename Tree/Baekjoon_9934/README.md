## - Baekjoon 9934 완전 이진 트리 - [Link](https://www.acmicpc.net/problem/9934)
● 입력  
> 3 
1 6 4 3 5 2 7     

● 출력
> 3  
6 2  
1 4 5 7   

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Tree/Baekjoon_9934/Baekjoon_9934.py)

```python
import sys
input = sys.stdin.readline

K = int(input())
nodes = list(input().split())

# 각 레벨에 맞는 노드를 넣을 수 있도록 2차원 배열 생성
res = [[] for _ in range(K)]

def make_tree(elements, level):
    # 중앙값을 구한뒤 res에 해당 레벨에 맞게 값을 넣음
    # 만약 중앙값만 남아있는 경우에는 return 
    mid = int(len(elements)/2)
    res[level].append(elements[mid])
    if mid == 0:
        return
    
    # 중위 순회이기에 중앙값으로 부터 왼쪽 노드를 먼저 재귀 시킨 후 오른쪽 노드들을 재귀
    make_tree(elements[:mid], level+1)
    make_tree(elements[mid+1:], level+1)

make_tree(nodes, 0)
for i in res: print(' '.join(i))
	
##### Python 3 #####
##### Runtime 68ms, Memory 29200KB #####
```

## - **How To Solve**
- 트리를 중위 순회할 때의 값을 입력값으로 받아 트리를 만들어야하는 생각보다 난감했던 문제
- 중위 순회 값의 가운데 값을 root로 하고 양 사이드를 재귀로 넘겨서 풀이
- 완전 이진 트리가 중위 순회와 연관성이 있는걸 깨달음, 트리의 종류와 순회 방법들을 전보다 알게됨