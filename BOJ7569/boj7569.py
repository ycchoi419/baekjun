import sys
from collections import deque

sys.stdin = open('input.txt')

M, N, H = map(int, input().split())
tomatos = [[list(map(int, input().split())) for n in range(N)] for h in range(H)]

q = deque()

for m in range(M):
    for n in range(N):
        for h in range(H):
            if tomatos[h][n][m] == 1:
                q.append((m, n, h))
ans = 0
tmp = deque()
while True:
    tmp.clear()
    while q:
        m, n, h = q.pop()
        if (h + 1 < H) and tomatos[h+1][n][m]==0:
            tomatos[h+1][n][m]=1
            tmp.append((m, n, h+1))
        if (h - 1 >= 0) and tomatos[h-1][n][m]==0:
            tomatos[h - 1][n][m]=1
            tmp.append((m, n, h-1))
        if (n + 1 < N) and tomatos[h][n+1][m]==0:
            tomatos[h][n + 1][m]=1
            tmp.append((m, n+1, h))
        if (n - 1 >= 0) and tomatos[h][n-1][m]==0:
            tomatos[h][n - 1][m]=1
            tmp.append((m, n-1, h))
        if (m + 1 < M) and tomatos[h][n][m+1]==0:
            tomatos[h][n][m + 1]=1
            tmp.append((m+1, n, h))
        if (m - 1 >= 0) and tomatos[h][n][m-1]==0:
            tomatos[h][n][m - 1]=1
            tmp.append((m-1, n, h))
    if not tmp:
        break
    else:
        q.extend(tmp)
        ans += 1

for m in range(M):
    for n in range(N):
        for h in range(H):
            if tomatos[h][n][m] == 0:
                ans = -1

print(ans)