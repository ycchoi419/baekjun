import sys
from collections import deque

sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
my_map = [list(map(int, sys.stdin.readline().strip('\n'))) for _ in range(N)]
visited = [[0 for i in range(M)] for j in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(n, m):
    q = deque()
    q.append((n, m, 0))
    while q:
        i, j, br = q.popleft()
        cnt = visited[i][j]
        if my_map[i][j]:
            if br:
                continue
            else:
                br = 1
        if i == N-1 and j == M-1:
            return cnt + 1
        tmp = deque()
        for k in range(4):
            if i + dx[k] < 0 or i + dx[k] >= N:
                continue
            if j + dy[k] < 0 or j + dy[k] >= M:
                continue
            if not visited[i + dx[k]][j + dy[k]]:
                if not my_map[i + dx[k]][j + dy[k]]:
                    tmp.append((i + dx[k], j + dy[k], br))
                    visited[i + dx[k]][j + dy[k]] = cnt + 1
                elif not br:
                    tmp.append((i + dx[k], j + dy[k], br))
                    visited[i + dx[k]][j + dy[k]] = cnt + 1
        if tmp:
            cnt += 1
            q.extend(tmp)
    return -1

print(bfs(0, 0))