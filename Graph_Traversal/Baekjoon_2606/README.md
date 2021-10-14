## - Baekjoon 2606 바이러스 문제 - [Link](https://www.acmicpc.net/problem/2606)
● 입력  
> 7  
6  
1 2  
2 3  
1 5  
5 2  
5 6  
4 7

● 출력
> 4  

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Graph_Traversal/Baekjoon_2606/Baekjoon_2606.py)

```python
import sys

def input():
  return sys.stdin.readline().rstrip()

cpts = int(input())
pairs = int(input())

graph = {cpt + 1: [] for cpt in range(cpts)}

for _ in range(pairs):
  cpt1, cpt2 = map(int, input().split())
  if cpt2 not in graph[cpt1]: 
     graph[cpt1] += [cpt2]
     graph[cpt2] += [cpt1]

def dps(start = 1, arrived = []):
  arrived.append(start)
  for cpt in graph[start]:
    if cpt not in arrived:
      arrived = dps(cpt, arrived)
  return arrived

print(len(dps()) - 1)
	
##### My code #####
##### Runtime 68ms, Memory 29200KB #####
```

## - **How To Solve**
- 간단한 **dps** 문제이며, 입력값을 **dic** 을 이용한 그래프를 만들어 풀이했다.
- 1 컴퓨터와 연결된 컴퓨터들의 개수만 구하면 되기때문에 **dps**를 사용하면 편하다.