## - Baekjoon 1918 후위표기식 문제 - [Link](https://www.acmicpc.net/problem/1918)
● 입력  
> A+B*C-D/E 

● 출력
> ABC*+DE/-

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Stack_and_Queue/Baekjoon_1918/Baekjoon_1918.py)

```python
elements = list(input()) 
stack, res = [], []
table = {'*' : 2, '/' : 2, '+' : 1, '-' : 1, '(' : 0}

for e in elements:
    if e.isalpha():
        res.append(e)
    elif e == '(':
        stack.append(e)
    elif e == ')':
        while True:
            tmp = stack.pop()    
            if tmp == '(':
                break
            res.append(tmp)
    else:
        while stack and table[stack[-1]] >= table[e]:
            res.append(stack.pop())
        stack.append(e)

while stack:
    res.append(stack.pop())

print(''.join(res))  

##### Python 3 #####
##### Runtime 88ms, Memory 29200KB #####
```

## - **How To Solve**
- 문제는 이해했지만 구현에서 시간을 많이 나간 문제, 괄호를 만났을 때 상황에서 애먹었다.
- 먼저 괄호와 연산자의 우선순위가 중요하다, '* /' > '+ -' > '(' 
- 현재의 연산자가 스택 맨위에 쌓여있는 연산자보다 작거나 같으면 res에 연산자를 더해준다.
- ( 를 만나면 스택에 쌓여있는 모든 연산자를 res에 더해준다.
- 위 경우가 가장 헷갈렸는데, 후위 표기식 방식이 ) 바로 오른쪽에 ()로 쌓여있는 모든 연산자를 두는 것이다.
- 그렇기에 시작되는 괄호를 만나면 그 전 연산자들은 스택에서 바로 다 풀어준다.
- 또한 왼쪽부터 순서대로 계산하는 것이기에 a-b-c-d-e-f-g 가 입력값이면 ab-c-d-e-f-g- 가 답이다.