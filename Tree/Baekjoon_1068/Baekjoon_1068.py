##### Python 3 #####
##### Runtime 64ms, Memory 29200KB #####

N = int(input())
parents = list(map(int, input().split()))
del_node = int(input())
graph = [set() for _ in range(N)]

# -1이면 루트로 지정하고, 아니면 그래프 생성
for idx in range(N):
    if parents[idx] == -1:
        root = idx
    else:
        graph[parents[idx]].add(idx)
    
def dfs(node):
    # 자식이 없으면 결과값에 + 1
    if not len(graph[node]):
        return 1
    
    res = 0
    # 자식 전부 dfs 돌림
    for n in graph[node]:
        res += dfs(n)
    
    return res
    
# 제거된 노드가 루트면 0을 출력 아니면, dfs 돌림
if parents[del_node] != -1:
    graph[parents[del_node]].remove(del_node)
    print(dfs(root))
else:
    print(0)