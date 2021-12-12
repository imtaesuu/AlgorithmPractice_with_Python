## - Baekjoon 21944 문제 추천 시스템 Version 2 - [Link](https://www.acmicpc.net/problem/21944)
● 입력  
> 5  
1000 1 1  
1001 2 1  
19998 78 2  
2667 37 3  
2042 55 3  
12  
add 1402 59 1  
recommend 1 1  
recommend2 1  
recommend3 1 50  
recommend3 -1 50  
solved 1000  
solved 2667  
recommend 2 1  
recommend 1 -1  
recommend2 -1  
solved 1001  
recommend 1 -1    

● 출력
> 1402  
19998  
2042  
2667  
19998  
1001  
1001  
1402  

## - Code - [Link](https://github.com/imtaesuu/AlgorithmPractice_with_Python/blob/main/Heap/Baekjoon_21944/Baekjoon_21944.py)

```python
import sys, heapq
from collections import defaultdict
input = sys.stdin.readline
problem_dict = {}
p_dict, g_dict, l_dict = defaultdict(list), defaultdict(list), defaultdict(list)

# 각 딕셔너리에 문제번호, 레벨, 분류를 heap을 이용하여 채워주는 함수
def add_pb(pb_num, l_num, g_num):
    heapq.heappush(p_dict[1], (-l_num, -pb_num, g_num))
    heapq.heappush(p_dict[-1], (l_num, pb_num, g_num))
    heapq.heappush(g_dict[g_num], (-l_num, -pb_num))
    heapq.heappush(g_dict[-g_num], (l_num, pb_num))
    heapq.heappush(l_dict[l_num], (pb_num, g_num))
    heapq.heappush(l_dict[-l_num], (-pb_num, -g_num))
    
    problem_dict[pb_num] = (l_num, g_num)

# 이미 풀었던 문제인지 체킹하는 함수
def check_pb(pb_num, l_num, g_num):
    if problem_dict[pb_num] == 0:
        return False
    
    # 레벨과 분류가 새롭게 추가된 문제랑 똑같은지 체킹 
    prev_l, prev_g = problem_dict[pb_num]
    if prev_l == l_num and prev_g == g_num:
        return True 
    return False
    
N = int(input())
for _ in range(N):
    pb_num, l_num, g_num = map(int, input().split())
    add_pb(pb_num, l_num, g_num)

M = int(input())
for _ in range(M):
    cmd, *args = input().split()
    
    # 각 recommend 마다 체킹함수를 이용해 solved된 문제를 삭제시킴
    # 체킹함수에는 양수를 보내줘야 하며, 코드를 줄이기 위해 x(1 or -1)을 key에 넣을 값에 곱해주고 나온 값에도 곱해줌
    
    if cmd == 'recommend':
        g, x = map(int, args)
        while g_dict[g*x] and not check_pb(g_dict[g*x][0][1]*(-x), g_dict[g*x][0][0]*(-x), g):
            heapq.heappop(g_dict[g*x])

        if g_dict[g*x]:
            print(g_dict[g*x][0][1]*(-x))
        
    elif cmd == 'recommend2':
        x = int(args[0])
        while p_dict[x] and not check_pb(p_dict[x][0][1]*(-x), p_dict[x][0][0]*(-x), p_dict[x][0][2]):
            heapq.heappop(p_dict[x])

        if p_dict[x]:
            print(p_dict[x][0][1]*(-x))

    elif cmd == 'recommend3':
        x, l = map(int, args)
        p = -1
        
        # l_dict의 키값을 1일 때는 오름차순 -1일 때는 내림차순으로 정렬 후 순회함
        # 체킹함수에는 양수를 보내줘야 하기 때문에 판단하여 값에 -1을 곱해줌 
        
        if x == 1:
            for key in sorted(l_dict.keys()):
                if key < 0: continue
                while l_dict[key] and not check_pb(l_dict[key][0][0], key, l_dict[key][0][1]):
                    heapq.heappop(l_dict[key])
                
                if l_dict[key] and key >= l:
                    p = l_dict[key][0][0]
                    break
        else:
            for key in sorted(l_dict.keys(), reverse = True):
                if key < 0: continue
                while l_dict[-key] and not check_pb(-l_dict[-key][0][0], key, -l_dict[-key][0][1]):
                    heapq.heappop(l_dict[-key])
                
                if l_dict[-key] and key < l:
                    p = -l_dict[-key][0][0]
                    break

        print(p)
    elif cmd == 'add':
        p, l, g = map(int, args)
        add_pb(p, l, g)
    else:
        problem_dict[int(args[0])] = 0
	
##### Python 3 #####
##### Runtime 988ms, Memory 115240KB #####
```

## - **How To Solve**
- Version 1 문제보다 좀 더 구현이 복잡해진 문제, 특히 분류와 recommend3를 구현할 때 시간을 많이 소비
- 핵심은 solved된 문제를 모두 삭제하는 것인데, 이때 시간초과를 잘 염두해야함
- 본인은 각 recommend마다 체킹함수를 통해서 우선순위가 가장 빠른 값들을 체킹하여 삭제함
- 한번에 모든 dict를 동기화하는 게 아니라 즉시 사용해아할 dict만 동기화하여 시간소비 최소화
- problem_dict에 add할 때마다 문제번호, 레벨, 분류를 새롭게 적용시켰고, 체킹함수는 새로운 값과 그 전값을 비교하는 것
- 구현이 생각보다 껄끄러웠던 문제, 실전에서 만나도 당황하지 않도록 빡구현 문제를 더 풀기