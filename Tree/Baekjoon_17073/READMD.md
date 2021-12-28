## - Baekjoon 17073 나무 위의 빗물 - [Link](https://www.acmicpc.net/problem/17073)
● 입력  
> 5 20  
5 3  
3 4  
2 1  
1 3

● 출력
> 6.6666666667  

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Tree/Baekjoon_17073/Baekjoon_17073.py)

```python
import sys
input = sys.stdin.readline

N, W = map(int, input().split())
table = [0]*(N+1)
# 노드가 두개만 있을 때를 방지하여 root는 초기값을 1 이상으로 설정해야함
table[1] = 1

# 연결된 노드가 있을 때마다 해당값에 +1 씩 해줌
for _ in range(N-1):
    a, b = map(int, input().split())
    table[a] += 1
    table[b] += 1
    
# count를 모르는 경우, for문으로 체크 
# leaf_nodes = 0
# for i in range(1, N+1):
#     if table[i] == 1:
#         leaf_nodes += 1
print(W/table.count(1))

##### Python 3 #####
##### Runtime 640ms, Memory 33104KB #####
```

## - **How To Solve**
- 문제를 정석대로 풀려면 bfs나 dfs를 이용해 트리를 탐색하고, random을 이용해야함
- 하지만 결론은 총물/리프노드의 개수 이기 때문에 리프 노드만 몇개인지 확인하면됨
- 노드가 두개일 때 root는 리프노드가 되면 안되기 때문에 초기값을 1 이상으로 해야하는게 이 문제의 포인트