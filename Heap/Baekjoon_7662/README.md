## - Baekjoon 7662 이중 우선순위 큐 문제 - [Link](https://www.acmicpc.net/problem/7662)
● 입력  
> 2  
7  
I 16  
I -5643  
D -1  
D 1  
D 1  
I 123  
D -1  
9  
I -45  
I 653  
D 1  
I -642  
I 45  
I 97  
D 1  
D -1  
I 333

● 출력
> EMPTY  
333 -45

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Heap/Baekjoon_7662/Baekjoon_7662.py)

```python
import sys, heapq
input = lambda : sys.stdin.readline().rstrip()

def rmv(heap, visited):
    while heap and visited[heap[0][1]]:
        heapq.heappop(heap)
        
T = int(input())
for _ in range(T):
    k = int(input())
    maxh, minh = [], []
    visited = [0]*k
    for i in range(k):
        args = input().split()
        arg, num = args[0], int(args[1])
        
        if arg == 'I':
            heapq.heappush(maxh, (-num, i))
            heapq.heappush(minh, (num, i))
        elif num == 1:
            rmv(maxh, visited)
            if maxh:
                visited[heapq.heappop(maxh)[1]] = 1
        else:
            rmv(minh, visited)
            if minh:
                visited[heapq.heappop(minh)[1]] = 1
    rmv(maxh, visited)
    rmv(minh, visited)
    if maxh:
        print(-maxh[0][0], minh[0][0])
    else:
        print('EMPTY')
	
##### My code #####
##### Runtime 3312ms, Memory 343816KB #####
```

## - **How To Solve**
- 힙을 이중으로 구성해서 풀이해야 되기 때문에 시간초과에서 잠시 막힌 문제
- 하나는 큰 수를 빼는 힙, 다른 하나는 작은 수를 빼는 힙으로 구성함
- 둘은 같은 수를 담은 힙이기 때문에 빠진 수는 서로 동기화 해줘야함
- 좀 더 최적화 하는 방법을 찾아보고 습득해야지 나중에 당황하지 않을듯
