## - Baekjoon 9466 텀 프로젝트  문제 - [Link](https://www.acmicpc.net/problem/9466)
● 입력  
> 2  
7  
3 1 3 7 3 4 6  
8  
1 2 3 4 5 6 7 8

● 출력
> 3  
0

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Graph_Traversal/Baekjoon_9466/Baekjoon_9466.py)

```python
import sys
input = lambda : sys.stdin.readline().rstrip()
T = int(input())
for _ in range(T):
    n = int(input())
    graph = [0] + list(map(int, input().split()))    
    visited = [False]*(n+1)
    
    res = 0
    for i in range(1, n+1):
        if visited[i]:
            continue
        
        first = i
        link = [first]
        visited[first] = True
        
        while True:
            tmp = graph[first]
            if visited[tmp]:
                break
            first = tmp
            link.append(first)
            visited[first] = True
        
        if link and tmp in link:
            res += len(link[link.index(tmp):])
    print(n- res)

##### PyPy3 #####
##### Runtime 1444ms, Memory 246048KB #####
```

## - **How To Solve**
- 처음에는 순회가 한번씩 끝날 때마다 결과값 리스트에 처음값과 마지막 값을 비교하고 del을 이용해 풀이함
- 문제는 맞았음, 그런데 시간이 너무 오버하게 나왔음, del이 아무리 **O(1)** 라도 크기가 크면 무용지물
- 나중에는 순회하면서 방문한 수를 만나기 전까지 link에 넣어두고 마지막 같은 수인 tmp의 위치를 이용하여 길이를 res에 더함
- 단순한 문제지만 시간을 줄이기 위해서 꽤 애먹은 문제, 나중에 다시 두고두고 봐야함