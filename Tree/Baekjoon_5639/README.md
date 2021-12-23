## - Baekjoon 5639 이진 검색 트리 - [Link](https://www.acmicpc.net/problem/5639)
● 입력  
> 50  
30  
24  
5  
28  
45  
98  
52  
60 

● 출력
> 5  
28  
24  
45  
30  
60  
52  
98  
50  

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Tree/Baekjoon_5639/Baekjoon_5639.py)

```python
import sys  
input = sys.stdin.readline
# 재귀의 깊이 제한을 늘려준다
sys.setrecursionlimit(10 ** 9)

nodes = []
while True:
    try:
        node = int(input())
    except:
        break
    nodes.append(node)

def pre_to_post(left, right):
    # 왼쪽 포인터가 오른쪽 포인터보다 크거나 같으면 재귀 종료
    # 슬라이싱으로 불러올 수 없기때문임
    if left >= right:
        return
    
    # 가장 왼쪽 노드를 루트로 지정
    root = nodes[left]
    
    # 만약 루트가 맨 끝 노드보다 크다면 한칸씩 땡겨서 바로 재귀
    # 어차피 자식이 하나인 경우 이며, 재귀를 두번 돌리지 않게 하기 위함
    if nodes[right-1] < root:
        pre_to_post(left+1, right)
        print(root)
        return

    idx = None
    
    # 처음으로 루트보다 큰 노드의 위치를 반환
    for i in range(left+1, right):
        if root < nodes[i]:
            idx = i
            break
    
    # 루트보다 큰 노드가 없을경우 가장 끝 노드의 위치를 반환
    if idx is None:
        idx = right
    pre_to_post(left+1, idx)
    pre_to_post(idx, right)
    print(root)
    
pre_to_post(0, len(nodes))

##### Python 3 #####
##### Runtime 88ms, Memory 38456KB #####
```

## - **How To Solve**
- 전위순회, 후위순회를 완벽히 이해하고 결과값들을 순서대로 나열하여 규칙을 찾아야 풀 수 있는 문제
- 전위 순회는 root left right 순으로 출력하기 때문에, 포인터를 오른쪽으로 옮겨가며
- 처음으로 root보다 큰 수부터 right 가 됨, 또 자식이 하나일 경우 left right 구분할 필요가 없음
- 따라서 루트가 맨 끝 노드보다 크다면 한칸씩 땡겨서 바로 재귀하여 시간 단축