import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

K = int(input())
W, H = map(int, input().split())

graph = []
graph = [[0 ,0 ,0 ,0],
         [-1 ,0 ,0 ,0],
         [0 ,0 ,-1 ,0],
         [0 ,-1 ,0 ,0],
         [0 ,-1 ,0 ,0],
         [0 ,-1 ,0 ,0]]
# for _ in range(H):
#     graph.append(list(map(int, input().split())))
visited = [[[False] * (K + 1) for _ in range(W)] for _ in range(H)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
hdx, hdy = [-2, -1, -2, -1, 2, 1, 2, 1], [-1, -2, 1, 2, -1, -2, 1, 2]

print(*visited, sep = '\n')


# def bfs():
#     q = deque([(0, 0, 0)])
#     visited[0][0][0] = True
    
#     while q:
        


