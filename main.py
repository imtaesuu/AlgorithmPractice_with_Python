import sys, math, itertools
from collections import Counter, defaultdict
import heapq
    
input = sys.stdin.readline

# Case. 1 처음부터 힙에 분류해서 넣기
# Case. 2 분류하지말고 나중에 check함수에 tmp 만들어서 내보낸 후 다시 합치기


problems = defaultdict(list)

def add(P, L, G):
    heapq.heappush(problems['minh'], (L, P, G))
    heapq.heappush(problems['maxh'], (-L, -P, G))
    heapq.heappush(problems[G], (L, P, G))
    heapq.heappush(problems[-G], (-L, -P, G))
    
def strd_L(heap, level):

    
N = int(input())
for _ in range(N):
    P, L, G = map(int, input().split())
    add(P, L, G)

M = int(input())
for _ in range(M):
    cmd = input().split()
    
    if cmd[0] == 'recommend':
        g, x = int(cmd[1]), int(cmd[2])
        if x == 1:
            print(-problems[-g][1])
        else:
            print(problems[g][1])
    
    elif cmd[0] == 'recommend2':
        x = int(cmd[1])
        if x == 1:
            print(-problems['maxh'][1])
        else:
            print(problems['minh'][1])
    
    elif cmd[0] == 'recommend3':
        x, l = int(cmd[1]), int(cmd[2])
        tmp = []
        if x == 1:
            while problems['minh']:
                if problems['minh'][0] >= l:
                    print(problems['minh'][1])
                    break
                else: tmp.append(heapq.heappop(problems['minh']))
            
            if not problems['minh']: print(-1)
            while tmp: heapq.heappush(problems['minh'], tmp.pop())
        
        else:
            while problems['maxh']:
                if problems['maxh'][0] < l:
                    print(-problems['maxh'][1])
                    break
                else: tmp.append(heapq.heappop(problems['maxh']))
            
            if not problems['maxh']: print(-1)
            while tmp: heapq.heappush(problems['maxh'], tmp.pop())
    
    elif cmd[0] == 'add':
        p, l, g = map(int, cmd[1:])
        
        
        
        
        
        
        
        
        
        
        
        
        


