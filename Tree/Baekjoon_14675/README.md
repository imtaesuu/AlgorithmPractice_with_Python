## - Baekjoon 14675 단절점과 단절선 - [Link](https://www.acmicpc.net/problem/14675)
● 입력  
> 5  
1 2  
2 3  
3 4  
4 5  
4  
1 1  
1 2  
2 1  
2 2  

● 출력
> no  
yes  
yes   
yes    

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Tree/Baekjoon_14675/Baekjoon_14675.py)

```python
import sys
input = sys.stdin.readline

N = int(input())
# 최대 크기로 리스트 만듦
table = [0]*100001
# 연결된 노드의 수, 해당 노드가 루트일 때 자식의 수를 구하는 거
for _ in range(N-1):
    a, b = map(int, input().split())
    table[a] += 1
    table[b] += 1

Q = int(input())
for _ in range(Q):
    args = list(map(int, input().split()))
    
    # 입력값들이 무조건 트리라는 가정하에 모든 간선은 단절선
    # 질의에 주어진 노드가 루트일 때 자식의 수가 2개 미만이라면 단절점이 아님
    if args[0] == 1:
        print('no' if table[args[1]] < 2 else 'yes')
    else:
        print('yes')

##### Python 3 #####
##### Runtime 300ms, Memory 29980KB #####
```

## - **How To Solve**
- 단절점과 단절선이 어떤 경우에 가능한 지 생각하면 꽤 쉬운 문제
- 처음에는 **dfs**로 순회하면서 자식 개수 파악했는데, 결론적으로 그냥 트리 만들고 주어진 노드 자식 개수 파악하면 되는 거였음