##### Python 3 #####
##### Runtime 300ms, Memory 29980KB #####

import sys
input = sys.stdin.readline

N = int(input())
# 최대 크기로 리스트 만듦
table = [0]*100001
# 연결된 노드의 수, 해당 노드가 루트일 때 자식의 수를 구하는 거
for _ in range(N-1):
    a, b = map(int, input().split())
    table[a] += 1
    table[b] += 1

Q = int(input())
for _ in range(Q):
    args = list(map(int, input().split()))
    
    # 입력값들이 무조건 트리라는 가정하에 모든 간선은 단절선
    # 질의에 주어진 노드가 루트일 때 자식의 수가 2개 미만이라면 단절점이 아님
    if args[0] == 1:
        print('no' if table[args[1]] < 2 else 'yes')
    else:
        print('yes')