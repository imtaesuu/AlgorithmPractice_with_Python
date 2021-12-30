##### PyPy3 #####
##### Runtime 596ms, Memory 135192KB #####

import sys
from collections import defaultdict, deque
input = sys.stdin.readline

# 부모를 찾는 함수
def find_parents(node):
    for parents, child in tree.items():
        if node in child:
            return parents
    return 0

while True:
    N, K = map(int, input().split())
    if not N+K:
        break
    
    elements = list(map(int, input().split()))
    tree = defaultdict(set)
    
    # 부모를 바꿔주기 위해서 부모 큐와 이전 값을 넣어줄 변수를 만들어준다
    parents = deque([elements[0]])
    prev = parents[0]
    parent = 0
    
    for e in elements[1:]:
        # 문제의 조건에 따라 prev + 1 < e 면 부모를 바꿔준다
        if prev + 1 < e:
            parent = parents.popleft()
        
        parents.append(e)
        tree[parent].add(e)
        prev = e

    p1 = find_parents(K)
    if not p1:
        print(0)
        continue
    p2 = find_parents(p1)
    if not p2:
        print(0)
        continue

    # 할아버지가 같은 자식의 수를 다 더해줌
    res = 0
    for t in tree[p2]:
        if t != p1:
            res += len(tree[t])
    print(res)