## - Baekjoon 1874 스택 수열 문제 - [Link](https://www.acmicpc.net/problem/1874)
● 입력  
> 8  
4  
3  
6  
8  
7  
5  
2  
1

● 출력
> push(+)    
push(+)  
push(+)   
push(+)   
pop(-)  
pop(-)  
push(+)   
push(+)  
pop(-)   
push(+)   
push(+)  
pop(-)  
pop(-)  
pop(-)  
pop(-)  
pop(-)
## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Stack_and_Queue/Baekjoon_1874/Baekjoon_1874.py)

```python
import sys

def input():
  return sys.stdin.readline().rstrip()

cnt = int(input())

stack, table = [], []

for _ in range(cnt):
  num = int(input())
  table.append(num)

idx, rlt = 0, []

for n in range(1, cnt + 1):
  stack.append(n)
  rlt.append("+")
  while stack and stack[-1] == table[idx]:
    stack.pop()
    idx += 1
    rlt.append("-")

if stack:
  print("NO")
else:
  for s in rlt:
    print(s)
	
##### My code #####
##### Runtime 264ms, Memory 35152KB #####
```

## - **How To Solve**
- 문제를 정확히 이해하면 **스택**을 이용하여 풀이하기 그렇게 어렵지 않은 형태이다.
- 먼저 입력값으로 **table**을 만든 다음, 오름차순으로 **stack** 쌓는 동시에 해결하도록 한다.
- 만들어진 **table** 의 값을 이용하기 위해 따로 위치포인터 **idx**를 만든다.
- 오름차순으로 **스택**을 쌓는 도중 **stack[-1]** 과 **table[idx]** 를 비교하여 해결한다.
