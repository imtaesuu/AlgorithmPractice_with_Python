## - Baekjoon 2493 탑 문제 - [Link](https://www.acmicpc.net/problem/2493)
● 입력  
> 5  
6 9 5 7 4

● 출력
> 0 0 2 2 4

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Stack_and_Queue/Baekjoon_2493/Baekjoon_2493.py)

```python
N = int(input())
towers = list(map(int, input().split()))
table, satck = [0]*N, []

for i in range(N-1, -1, -1):
    while stack and towers[i] >= towers[stack[-1]]:
        table[stack.pop()] = i+1
    stack.append(i)
print(' '.join(map(str, table)))

##### PyPy3 #####
##### Runtime 284ms, Memory 222392KB #####
```

## - **How To Solve**
- 탑의 위치를 stack에 넣어서 거꾸로 순회할 때 마다 while을 반복해주는 구조
- 처음 풀이도 위와 비슷했고 다른점은 처음풀이는 stack에 탑의 위치와 높이를, 위 풀이는 탑의 위치만을 넣음
- 위 풀이가 더 깔끔하고 간결하여 가독성이 매우 높음, 설명이 필요없이 코드를 보면서 문제 이해도 가능
- Asterisk( * )를 이용하여 언패킹한 것보다 join을 사용하는게 속도적으로 앞섬 