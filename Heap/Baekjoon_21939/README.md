## - Baekjoon 21939 문제 추천 시스템 Version 1 - [Link](https://www.acmicpc.net/problem/21939)
● 입력  
> 5  
1000 1  
1001 2  
19998 78  
2667 37  
2042 55  
8  
add 1402 59  
recommend 1  
solved 1000  
solved 19998  
recommend 1  
recommend -1  
solved 1001  
recommend -1  

● 출력
> 19998  
1402  
1001  
2667

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Heap/Baekjoon_21939/Baekjoon_21939.py)

```python
import sys, heapq    
input = sys.stdin.readline
maxh, minh = [], []
solved = set()

def rmv(heap):
    while heap and heap[0][1] in solved:
        heapq.heappop(heap)
        
N = int(input())
for _ in range(N):
    P, L = map(int, input().split())
    heapq.heappush(maxh, ((-L, -P), P))
    heapq.heappush(minh, ((L, P), P ))

M = int(input())
for _ in range(M):
    cmd = input().split()
    P = int(cmd[1])
    if cmd[0] == 'add':
        if P in solved:
            rmv(maxh)
            rmv(minh)
            solved.remove(P)
        L = int(cmd[2])
        heapq.heappush(maxh, ((-L, -P), P))
        heapq.heappush(minh, ((L, P), P ))
    elif cmd[0] == 'solved':
        solved.add(P)
    else:
        rmv(maxh)
        rmv(minh)
        if P == 1: print(maxh[0][1])
        else: print(minh[0][1])
	
##### PyPy3 #####
##### Runtime 348ms, Memory 153080KB #####
```

## - **How To Solve**
- 이중 우선순위 큐 문제와 같이 풀이하면 됨
- 단 solved후 바로 add할 때 최근값이 전값보다 먼저 삭제되는 경우를 주의해야함
- solved를 set, dict, list 등 무엇으로 구현해도 상관없음