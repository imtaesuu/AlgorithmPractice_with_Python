##### Python 3 #####
##### Runtime 68ms, Memory 29200KB #####

import sys
input = sys.stdin.readline

K = int(input())
nodes = list(input().split())

# 각 레벨에 맞는 노드를 넣을 수 있도록 2차원 배열 생성
res = [[] for _ in range(K)]

def make_tree(elements, level):
    # 중앙값을 구한뒤 res에 해당 레벨에 맞게 값을 넣음
    # 만약 중앙값만 남아있는 경우에는 return 
    mid = int(len(elements)/2)
    res[level].append(elements[mid])
    if mid == 0:
        return
    
    # 중위 순회이기에 중앙값으로 부터 왼쪽 노드를 먼저 재귀 시킨 후 오른쪽 노드들을 재귀
    make_tree(elements[:mid], level+1)
    make_tree(elements[mid+1:], level+1)

make_tree(nodes, 0)
for i in res: print(' '.join(i))