## - Baekjoon 22942 데이터 체커 문제 - [Link](https://www.acmicpc.net/problem/22942)
● 입력  
> 4  
3 1  
4 1  
5 1  
6 5

● 출력
> NO

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Stack_and_Queue/Baekjoon_22942/Baekjoon_22942.py)

```python
import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
circles = []

for _ in range(N):
    x, r = map(int, input().split())
    circles.append((x - r, x + r))

circles.sort(key = lambda x : x[0])

for i in range(N-1):
    l1, r1 = circles[i]
    l2, r2 = circles[i+1]
    if l1 == l2 or r1 == r2 or r1 == l1 or l2 < r1 < r2:
        print('NO')
        sys.exit(0)           
print('YES')

##### Python 3 #####
##### Runtime 500ms, Memory 57692KB #####
```

## - **How To Solve**
- 단순히 모든 원들을 각각 비교하면 타임아웃 걸리는 문제
- 원들의 반지름, x좌표, 양 끝 좌표 등을 기준으로 삼아 정렬 후 그에 맞게 한원에서 다음원을 비교하여 풀이해야함
- 위 풀이에서는 원들의 양끝좌표를 리스트에 넣었고 그 중 왼쪽 좌표를 기준으로 정렬했음
- 그 뒤 조건에 맞게 비교하여 풀이함, 정답보다는 다양한 시각으로 바라보는 게 중요한 문제
- 뻔히 시간초과가 눈에 보이는 문제들은 반드시 다양한 각도로 바라보기
- 스택을 이용하지는 않았지만, 스택을 활용하여 풀 수도 있기 때문에 이곳으로 분류함