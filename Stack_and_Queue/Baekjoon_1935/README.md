## - Baekjoon 1935 후위 표기식 문제 - [Link](https://www.acmicpc.net/problem/1935)
● 입력  
> 5  
ABC*+DE/-  
1  
2  
3  
4  
5

● 출력
> 6.20
## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Stack_and_Queue/Baekjoon_1935/Baekjoon_1935.py)

```python
import sys

def input():
  return sys.stdin.readline().rstrip()

alphabet, table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', {}
cnt = int(input())
line = input()

for _ in range(cnt):
  num = int(input())
  table[alphabet[_]] = num 

stack, rlt = [], 0

for s in line:
  if s.isalpha():
    stack.append(table[s])
  else:
    num1 = stack.pop()
    num2 = stack.pop()
    if s == '+':
      stack.append(num2 + num1)
    elif s == '-':
      stack.append(num2 - num1)
    elif s == '*':
      stack.append(num2 * num1)
    elif s == '/':
      stack.append(num2 / num1)

print(f'{stack[0]:.2f}')
	
##### My code #####
##### Runtime 68ms, Memory 29200KB #####
```

## - **How To Solve**
- 후위 표기식을 정확히 이해하지 못하면 꽤 까다로운 문제로 다가올 수 있다.
- 알파벳 순서대로 입력값과 함께 **딕셔너리**에 저장했다.
- 이제 **스택**을 이용하였는데, **스택**에 담겨진 후방으로부터 두번째까지 숫자를 **pop**하여 계산후 다시 **스택**에 넣었다.