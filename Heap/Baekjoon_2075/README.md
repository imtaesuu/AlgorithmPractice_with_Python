## - Baekjoon 2075 N번째 큰 수 문제 - [Link](https://www.acmicpc.net/problem/2075)
● 입력  
> 5  
12 7 9 15 5  
13 8 11 19 6  
21 10 26 31 16  
48 14 28 35 25  
52 20 32 41 49

● 출력
> 35  

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Heap/Baekjoon_2075/Baekjoon_2075.py)

```python
import sys, heapq 
input = sys.stdin.readline

N = int(input())
table = list(map(int, input().split()))
heapq.heapify(table)

for _ in range(N-1):
    elements = map(int, input().split())    
    for e in elements:
        if table[0] < e:
            heapq.heappushpop(table, e)
print(table[0])
	
##### Python 3 #####
##### Runtime 876ms, Memory 31268KB #####
```

## - **How To Solve**
- 힙으로 풀 수 있는 문제인걸 알면서도, 모든 수는 자신의 한칸 위에 있는 수보다 크다라는 규칙에 매몰됨
- 문제의 조건에 정답이 나와있었음, 타 문제들과 달리 메모리 제한이 깐깐하고 N번째 큰수를 찾는 문제임
- 따라서 모두 힙에 넣은 후 N번 수를 뽑아내는 maxheap 방식은 무조건 메모리 초과
- 힙의 크기를 애초에 N으로 제한하고 가장 작은 수가 다음 들어올 수보다 작을 때만 힙을 넣어주고 빼는 minheap 방식이 정답
- 메모리 제한이 깐깐할 때는 항상 일정한 크기 안에서 이루어 지면 해결할 수 있다는 걸 기억해야함
- 쉽게 말해 그래프를 만든다 하면, 전체를 만들 필요없이 처음부터 제한된 그래프를 만들어 메모리를 아껴야함