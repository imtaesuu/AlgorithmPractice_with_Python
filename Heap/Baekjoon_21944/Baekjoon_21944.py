##### Python 3 #####
##### Runtime 988ms, Memory 115240KB #####

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