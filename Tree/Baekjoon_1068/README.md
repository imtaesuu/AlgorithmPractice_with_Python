## - Baekjoon 1068 트리 - [Link](https://www.acmicpc.net/problem/1068)
● 입력  
> 9  
-1 0 0 2 2 4 4 6 6  
4  

● 출력
> 2   

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Tree/Baekjoon_1068/Baekjoon_1068.py)

```python
N = int(input())
parents = list(map(int, input().split()))
del_node = int(input())
graph = [set() for _ in range(N)]

# -1이면 루트로 지정하고, 아니면 그래프 생성
for idx in range(N):
    if parents[idx] == -1:
        root = idx
    else:
        graph[parents[idx]].add(idx)
    
def dfs(node):
    # 자식이 없으면 결과값에 + 1
    if not len(graph[node]):
        return 1
    
    res = 0
    # 자식 전부 dfs 돌림
    for n in graph[node]:
        res += dfs(n)
    
    return res
    
# 제거된 노드가 루트면 0을 출력 아니면, dfs 돌림
if parents[del_node] != -1:
    graph[parents[del_node]].remove(del_node)
    print(dfs(root))
else:
    print(0)

##### Python 3 #####
##### Runtime 64ms, Memory 29200KB #####
```

## - **How To Solve**
- 자식중 제거된 노드가 있다면 제거 해주고 dfs 돌리면 되는 문제
- 난이도에 맞지 않게 굉장히 쉬운 문제 최대한 적은 시간이 나오게끔 코드를 수정하며 시도해 보았지만
- 코드 길이 때문인지 아니면 순서의 문제인지 쨌든 64ms가 최소