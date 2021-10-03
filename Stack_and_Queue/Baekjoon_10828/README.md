## - Baekjoon 1158 요세푸스 문제 - [Link](https://www.acmicpc.net/problem/1158)
● 입력  
> 14  
push 1  
push 2  
top  
size  
empty  
pop  
pop  
pop  
size  
empty  
pop  
push 3  
empty  
top

● 출력
> <3, 6, 2, 7, 5, 1, 4>

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Stack_and_Queue/Baekjoon_1158/Baekjoon_1158.py)

```python
from collections import deque

N, K = map(int, input().split())

people = deque([i+1 for i in range(N)])
rlt = []

while people:
  people.rotate(-(K-1))
  rlt.append(people.popleft())

print("<" + ", ".join(map(str, rlt)) + ">")
	
##### My code #####
##### Runtime 100ms, Memory 32120KB #####
```

## - **How To Solve**
- 요세푸스 문제 규칙에 따라 **K번째의 값**을 **결과값**에 넣으면된다.
- 기본적인 **리스트**로 풀려고 하면 구현이 꽤 까다로워 멀리 돌아가는 문제이다.
- **데크**의 **rotate**를 사용하여 **큐**를 거꾸로 순회시킨후 값을 꺼내어 **결과값**에 넣는다.
- **데크** 자료형의 특징을 잘 활용하면 그리 어렵지 않은 문제다.