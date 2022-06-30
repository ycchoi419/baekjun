import sys
from collections import deque

sys.stdin = open('input.txt')

T = int(sys.stdin.readline())

for tc in range(T):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        i, j = map(int, sys.stdin.readline().split())
        graph[i].append(j)
        graph[j].append(i)

    visited = [0 for _ in range(V+1)]

    def bfs(v):
        q = deque()
        q.append(v)
        cnt = 1
        visited[v] = cnt
        while True:
            temp = deque()
            cnt += 1
            while q:
                n = q.popleft()
                for i in graph[n]:
                    if not visited[i]:
                        visited[i] = cnt
                        temp.append(i)
                    else:
                        if visited[i]%2 != cnt%2:
                            return False
            if not temp:
                return True
            else:
                q = temp.copy()

    ans = bfs(1)
    if ans:
        for i in range(2, V+1):
            if not visited[i]:
                ans = bfs(i)
                if not ans:
                    break

    if ans:
        print("YES")
    else:
        print("NO")
