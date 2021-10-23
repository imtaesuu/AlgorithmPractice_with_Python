import sys
from collections import deque
input = sys.stdin.readline
R, C, N = map(int, input().split())
graph = [['.','.','.','.','.','.','.'],
         ['.','.','.','O','.','.','.'],
         ['.','.','.','.','O','.','.'],
         ['.','.','.','.','.','.','.'],
         ['O','O','.','.','.','.','.'],
         ['O','O','.','.','.','.','.']]

queue = deque()

def fill():
    for i in range(R):
        for j in range(C):
            if graph[i][j] == '.':
                graph[i][j] = 'O'
def find():
    for i in range(R):
        for j in range(C):
            if graph[i][j] == 'O':
                queue.append((i, j))
                
def explosion():
    while queue:
        x, y = queue.popleft()
        graph[x][y] = '.'
        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<R and 0<=ny<C:
                graph[nx][ny] = '.'

# for i in range(R):
#     graph.append(list(input().rstrip()))
#     for j in range(C):
#         graph[i][j] = 0 if graph[i][j] == '.' else 2
 
for i in range(N - 1):
    if i % 2 == 1:
        explosion()
    else:
        find()
        fill()
    print(queue)

for i in graph:
    for j in i:
        print(j, end = "")
    print()