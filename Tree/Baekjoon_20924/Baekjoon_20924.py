##### Python 3 #####
##### Runtime 804ms, Memory 124852KB #####

import sys
from collections import defaultdict
input = sys.stdin.readline

# tree 만들기
# defaultdict -> dict를 사용하여 방문 따로 등록하지 않아도 되는 단방향 트리 만들 수 있음 
N, R = map(int, input().split())
tree = defaultdict(dict)
for _ in range(N-1):
    a, b, d = map(int, input().split())
    tree[a][b] = d
    tree[b][a] = d

# 가지치기 시작하는 노드를 찾기
gnode, gdstc = R, 0
while len(tree[gnode]) == 1:
    node, dstc = list(tree[gnode].items())[0]
    # del을 이용하여 반대로 향하는 간선을 삭제
    del tree[node][gnode]
    gdstc += dstc
    gnode = node

# dfs를 이용하여 최대값 구함
if not tree[gnode]:
    print(gdstc, 0)
else:
    stack = [(gnode, 0)]
    maxbranch = 0
    while stack:
        node, dstc = stack.pop()
        
        if not tree[node]:
            if maxbranch < dstc:
                maxbranch = dstc
            continue
        
        for n, d in tree[node].items():
            del tree[n][node]
            stack.append((n, dstc+d))
    
    print(gdstc, maxbranch)              