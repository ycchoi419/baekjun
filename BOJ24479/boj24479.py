import sys
from collections import deque

sys.stdin = open('input.txt')

N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)
ans = [0]*(N+1)
for i in graph:
    i.sort(reverse=True)
visited = [0 for _ in range(N+1)]

cnt = 1
need_visited = deque()
need_visited.append(R)
while need_visited:
    n = need_visited.pop()
    if not visited[n]:
        visited[n] = 1
        ans[n] = cnt
        cnt += 1
        for i in graph[n]:
            if not visited[i]:
                need_visited.append(i)
for i in range(1, N+1):
    print(ans[i])
