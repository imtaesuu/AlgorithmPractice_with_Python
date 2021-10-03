## - Baekjoon 9012 올바른 괄호 문제 - [Link](https://www.acmicpc.net/problem/9012)
● 입력  
> 3  
()  
))  
())(()

● 출력
> YES  
NO  
NO

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Stack_and_Queue/Baekjoon_9012/Baekjoon_9012.py)

```python
import sys

def input():
    return sys.stdin.readline().rstrip()

def findVPS(PS):
	stack = []
	
	if not PS:
		return False

	for i in PS:
		if i == '(':
			stack.append('(')
		elif i == ')' and stack:
			stack.pop()
		else:
			return False
	
	return not stack

cnt = int(input())

for _ in range(cnt):
	s = input()

	if findVPS(s):
		print('YES')
	else:
		print('NO')
	
##### My code #####
##### Runtime 68ms, Memory 29200KB #####
```

## - **How To Solve**
- 괄호의 짝이 잘 지어졌는지 확인하는 문제이며, **스택**의 특성을 활용하면 손쉽게 풀 수 있다.
- 구현은 어렵지 않은 편이나 방식에 따라 코드가 복잡해질 수 있다.
- 괄호가 하나만 사용되어서 **카운팅** 하는 방법으로도 풀 수 있다.