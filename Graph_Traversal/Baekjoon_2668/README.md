## - Baekjoon 2668 숫자고르기 문제 - [Link](https://www.acmicpc.net/problem/2668)
● 입력  
>7  
3  
1  
1  
5  
5  
4  
6

● 출력
>3  
1  
3  
5

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Graph_Traversal/Baekjoon_2668/Baekjoon_2668.py)

```python
import sys
input = lambda : sys.stdin.readline().rstrip()
N = int(input())
graph, res = {}, set()
for i in range(1, N+1): graph[i] = int(input())

def dfs(node):
    stack = [node]
    a_set, b_set = set(), set()
    a_set.add(node)
    visited = [node]   
    while stack:
        node = stack.pop()    
        b_set.add(graph[node]) 
    
        if graph[node] not in visited:
            stack.append(graph[node])
            a_set.add(graph[node])
            visited.append(graph[node])
    
    if a_set == b_set:
        return a_set
    return {}

for key in graph: res.update(dfs(key))
res = sorted(res)
print(len(res), *res, sep = '\n')
	
##### My code #####
##### Runtime 92ms, Memory 31848KB #####
```

## - **How To Solve**
- 오랜만에 **dfs**를 사용하여 푼 문제, set를 이용하면 문제가 꽤 쉬워진다.
- 두개의 set를 만들어 dfs 진행 후 비교후 같으면 한 set를 다르면 {}를 반환한다.
- for문으로 graph를 모두 돌아 res에 결과값을 update 해줬다.
- 따로 예외조건도 없어서 굉장히 쉽고, N 값도 상당히 작아서 **in**을 사용해도 통과다.
- **in** 대신에 [False]로 미리 초기화된 visited를 사용하면 더 빠를 수도 있겠다.