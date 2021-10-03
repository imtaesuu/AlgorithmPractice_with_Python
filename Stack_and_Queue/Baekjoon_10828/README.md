## - Baekjoon 10828 스택 구현 문제 - [Link](https://www.acmicpc.net/problem/10828)
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
> 2  
2  
0  
2  
1  
-1  
0  
1  
-1  
0  
3

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Stack_and_Queue/Baekjoon_10828/Baekjoon_10828.py)

```python
import sys

def input():
  return sys.stdin.readline().rstrip()

cnt = int(input())
stack = []

while cnt != 0:
  cmd = input().split()
  cnt -= 1

  if cmd[0] == 'push':
    stack.append(int(cmd[1]))
  elif cmd[0] == 'pop':
    if stack:
      print(stack.pop())
    else:
      print(-1)
  elif cmd[0] == 'size':
    print(len(stack))
  elif cmd[0] == 'empty':
    if stack:
      print(0)
    else:
      print(1)
  elif cmd[0] == 'top':
    if len(stack) == 0:
      print(-1)
    else:
      print(stack[-1])
	
##### My code #####
##### Runtime 92ms, Memory 29200KB #####
```

## - **How To Solve**
- 기본적인 구현 문제이며, **스택**의 구조를 이해하고 있으면 구현하기 쉽다.
- 내 코드에서는 **while**을 썼지만 **for**을 이용해도 된다.