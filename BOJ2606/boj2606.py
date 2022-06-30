import sys
from collections import deque

sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[0 for i in range(N+1)] for j in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    graph[i][j] = 1
    graph[j][i] = 1

def bfs(v):
    q = deque()
    q.append(v)
    while q:
        n = q.popleft()
        visited[n] = 1
        for i in range(1, N+1):
            if graph[n][i] and not visited[i]:
                q.append(i)
    return visited.count(1)-1

print(bfs(1))