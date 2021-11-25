## - Baekjoon 2800 괄호 제거 문제 - [Link](https://www.acmicpc.net/problem/2800)
● 입력  
> (1+(2*(3+4))) 

● 출력
> (1+(2*3+4))  
(1+2*(3+4))  
(1+2*3+4)  
1+(2*(3+4))  
1+(2*3+4)  
1+2*(3+4)  
1+2*3+4

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Graph_Traversal/Baekjoon_2800/Baekjoon_2800.py)

```python
import itertools
s = input()
stack, table = [], []
# 괄호쌍을 테이블에 담기
for idx, val in enumerate(s):
    if val == '(':
        stack.append((idx, val))
    elif val == ')':
        tmp = stack.pop()
        table.append((tmp[0], idx))

#itertools의 조합을 이용하여 경우의 수를 구한다음 
#인덱스값이 넘어가지 않도록 하기 위하여 내림차순으로 정렬
res = []
for i in range(1, len(table)+1):
    for j in itertools.combinations(table, i):
        n = sorted([e for each in j for e in each], reverse = True)
        tmp = list(s)
        
        for k in n:
            del tmp[k]
        res.append(''.join(tmp))
print(*sorted(set(res)), sep = '\n')

##### Python 3 #####
##### Runtime 68ms, Memory 29452KB #####
```

## - **How To Solve**
- 스택을 이용하는 것에 빠져 큰 그림을 보지 못하여 오래걸린 문제.
- itertools의 combinations을 이용하여 괄호쌍의 조합을 구함
- 괄호쌍의 인덱스값을 받아 제거하면 되는데 여기서 왼쪽 괄호부터 제거하면 인덱스값이 줄어들기 때문에
- 인덱스값의 리스트를 내림차순으로 정렬한 뒤 del을 이용하여 제거
- 마지막으로 결과값을 사전 순으로 출력해야하기에 res를 정렬함