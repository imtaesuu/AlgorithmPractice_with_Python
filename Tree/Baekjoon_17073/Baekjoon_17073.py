##### Python 3 #####
##### Runtime 640ms, Memory 33104KB #####

import sys
input = sys.stdin.readline

N, W = map(int, input().split())
table = [0]*(N+1)
# 노드가 두개만 있을 때를 방지하여 root는 초기값을 1 이상으로 설정해야함
table[1] = 1

# 연결된 노드가 있을 때마다 해당값에 +1 씩 해줌
for _ in range(N-1):
    a, b = map(int, input().split())
    table[a] += 1
    table[b] += 1
    
# count를 모르는 경우, for문으로 체크 
# leaf_nodes = 0
# for i in range(1, N+1):
#     if table[i] == 1:
#         leaf_nodes += 1
print(W/table.count(1))