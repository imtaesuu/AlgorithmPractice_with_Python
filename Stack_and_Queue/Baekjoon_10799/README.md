## - Baekjoon 10799 쇠막대기 문제 - [Link](https://www.acmicpc.net/problem/10799)
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

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Stack_and_Queue/Baekjoon_10799/Baekjoon_10799.py)

```python
import sys

def input():
  return sys.stdin.readline().rstrip()

stack = []
arr = input()
prev, res = '', 0

for s in arr:
  if s == '(':
    stack.append(s)
  else:
    if prev == '(':
      stack.pop()
      res += len(stack)
    else:
      stack.pop()
      res += 1
  prev = s

print(res)
	
##### My code #####
##### Runtime 92ms, Memory 29632KB #####
```

## - **How To Solve**
- 스택 문제중에서 꽤 고민을 많이 했던 문제, 막대기를 따로따로 생각하여 풀이하려 하면 쉽게 풀리지 않는다.
- '(' 가 나올 때부터 스택에 담아두고 ')' 가 나오기 전까지는 막대기로 취급하여 풀어야한다.
- '()' 가 완성될 때 스택에서 하나를 **pop**하고 스택의 길이만큼 결과값에 더해준다.
- 단, 막대기 하나가 끝이났을 때는 결과값에 꼭다리 1개만 더해준다.
- 처음에는 좀 오래 막혔지만, '('가 나오자마자 막대기 하나가 추가되었다고 생각하며 풀이하면 편하다.