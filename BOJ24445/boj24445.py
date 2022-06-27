import sys
from collections import deque

sys.stdin = open('input.txt')

N, M, R = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)

for l in graph:
    l.sort(reverse=True)

ans = [0 for _ in range(N+1)]
cnt = 1
need_visit = deque([R])
while need_visit:
    n = need_visit.popleft()
    if not visited[n]:
        visited[n] = 1
        ans[n] = cnt
        cnt += 1
        for i in graph[n]:
            if not visited[i]:
                need_visit.append(i)

for i in range(1, N+1):
    print(ans[i])