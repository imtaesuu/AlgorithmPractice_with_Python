import sys
from collections import deque

input = sys.stdin.readline

# sys.setrecirsionlimit(10000)

N, M = map(int, input().rstrip().split())
graph = []

for _ in range(N):
    graph.append(list(input().rstrip()))


def bfs(x, y):

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or \
              ny < 0 or ny >= M:
                continue

            if graph[nx][ny] == '1':
                graph[nx][ny] = int(graph[x][y]) + 1
                q.append((nx, ny))

    return graph[N - 1][M - 1]
print(bfs(0, 0))