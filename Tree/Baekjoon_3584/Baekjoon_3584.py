##### Python 3 #####
##### Runtime 104ms, Memory 29968KB #####

import sys
input = sys.stdin.readline

def find_node(node):
    # 루트 노드 포함
    res = [node]
    # 부모가 없을 때까지 경로를 추가하면서 반복 
    while tree[node] != 0:
        res.append(tree[node])
        node = tree[node]
    return res
                        
T = int(input())
for _ in range(T):    
    N = int(input())
    tree = [0]*(N+1)
    # 리스트에 자식 index에 부모를 넣음
    for _ in range(N-1):
        p, c = map(int, input().split())
        tree[c] = p
    
    n1, n2 = map(int, input().split())
    # 하나는 순서가 있는 경로용 list, 다른 하나는 포함 확인용 set
    # set은 list와는 다르게 해쉬값을 이용하여 순서가 없고 in을 이용할 때 훨씬 빠름
    path1 = find_node(n1)
    path2 = set(find_node(n2))
    
    for i in path1:
        if i in path2:
            print(i)
            break