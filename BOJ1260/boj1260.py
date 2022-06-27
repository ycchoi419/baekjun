import sys
from collections import deque

sys.stdin = open('input.txt')

N, M, V = map(int, input().split())

arr = [[0 for i in range(N+1)] for j in range(N+1)]

for _ in range(M):
    n, m = map(int, input().split())
    arr[n][m] = 1
    arr[m][n] = 1


dfs_visited = [0 for _ in range(N + 1)]
bfs_visited = [0 for _ in range(N + 1)]

dfs_ans = []
bfs_ans = []

# def dfs(v):
#     dfs_visited[v] = 1
#     dfs_ans.append(v)
#     for i in arr[v]:
#         if not dfs_visited[i]:
#             dfs(i)


def dfs(v):
    need_visited = deque()
    need_visited.append(v)
    while need_visited:
        n = need_visited.pop()
        if not dfs_visited[n]:
            dfs_visited[n] = 1
            dfs_ans.append(n)
            for i in range(N, 0, -1):
                if arr[n][i]:
                    need_visited.append(i)

def bfs(v):
    need_visited = deque()
    need_visited.append(v)
    while need_visited:
        n = need_visited.popleft()
        if not bfs_visited[n]:
            bfs_visited[n] = 1
            bfs_ans.append(n)
            for i in range(N+1):
                if arr[n][i]:
                    need_visited.append(i)


dfs(V)
print(*dfs_ans)

bfs(V)
print(*bfs_ans)