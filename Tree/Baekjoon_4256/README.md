## - Baekjoon 4256 트리 - [Link](https://www.acmicpc.net/problem/4256)
● 입력  
> 2  
4  
3 2 1 4  
2 3 4 1  
8  
3 6 5 4 8 7 1 2  
5 6 8 4 3 1 2 7   

● 출력
> 2 4 1 3  
5 8 4 6 2 1 7 3 

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Tree/Baekjoon_4256/Baekjoon_4256.py)

```python
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def to_postorder(p_start, p_end, i_start, i_end):    
    if p_end < p_start or i_end < i_start:
        return 
    
    root = preorder[p_start]
    # inorder 값에서의 root값의 idx
    # ValueError를 방지하기 위해 미리 테이블을 만들어둠
    # 위치 동기화를 위해 시작 위치를 빼준게 길이
    pos = position[root]
    length = pos - i_start
    
    # 재귀로 왼쪽 오른쪽을 차례로 보내고 출력해줌
    to_postorder(p_start+1, p_start+length, i_start, pos-1)
    to_postorder(p_start+length+1, p_end, pos+1, i_end)
    print(root, end = ' ')

T = int(input())
for _ in range(T):
    N = int(input())

    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    position = [0] * (N+1)

    # 미리 inorder의 값들의 위치를 테이블에 넣어둠
    for i in range(N):
        position[inorder[i]] = i
    
    to_postorder(0, N-1, 0, N-1)
    print()

##### Python 3 #####
##### Runtime 212ms, Memory 30212KB #####
```

## - **How To Solve**
- 재귀로 풀이하는 문제, 이미 이진 검색 트리 문제에서 경험해본 문제
- 하지만 전위 중위 를 이용해서 후위를 출력하는 것이고, 인자값으로 list 자체를 보내는 방식은 쉽지만 느리고
- 위치값을 넣어서 보내는 건 쉽지 않음, 미리 테이블을 만드는 부분에서 막힘
- 좀 더 이해하고 연습해야겠음