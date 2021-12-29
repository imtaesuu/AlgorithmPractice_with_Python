## - Baekjoon 3584 가장 가까운 공통 조상 - [Link](https://www.acmicpc.net/problem/3584)
● 입력  
> 5  
2 3  
3 4  
3 1  
1 5  
3 5  

● 출력
> 3    

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Tree/Baekjoon_3584/Baekjoon_3584.py)

```python
import sys
input = sys.stdin.readline

def find_node(node):
    # 루트 노드 포함
    res = [node]
    # 부모가 없을 때까지 경로를 추가하면서 반복 
    while tree[node] != 0:
        res.append(tree[node])
        node = tree[node]
    return res
                        
T = int(input())
for _ in range(T):    
    N = int(input())
    tree = [0]*(N+1)
    # 리스트에 자식 index에 부모를 넣음
    for _ in range(N-1):
        p, c = map(int, input().split())
        tree[c] = p
    
    n1, n2 = map(int, input().split())
    # 하나는 순서가 있는 경로용 list, 다른 하나는 포함 확인용 set
    # set은 list와는 다르게 해쉬값을 이용하여 순서가 없고 in을 이용할 때 훨씬 빠름
    path1 = find_node(n1)
    path2 = set(find_node(n2))
    
    for i in path1:
        if i in path2:
            print(i)
            break
    
##### Python 3 #####
##### Runtime 104ms, Memory 29968KB #####
```

## - **How To Solve**
- 처음 풀었던 풀이는 온전한 tree를 만들고 풀이했던 것이라 path를 사용하는 과정에서 조금 지저분 했음
- 하지만 단지 부모를 확인하는 문제이므로 자식 index에 부모값을 넣고 while문으로만 탐색하면 훨씬 간결해짐
- 또한 어차피 가장 가까운 공통 부모이기에 순서가 있는 경로는 하나로 충분하고 나머지는 set으로 바꾸어 in 시간 단축