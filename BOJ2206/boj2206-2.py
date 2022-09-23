import sys
from collections import deque

sys.stdin = open('input.txt')

N, M = map(int, input().split())
my_map = [list(map(int, input())) for _ in range(N)]
visited = [[0 for i in range(M)] for j in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited[0][0] = 1


def bfs():
    q = deque()
    tmp = deque()
    q.append((0, 0, 0))
    cnt = 0
    while True:
        while q:
            n, m, br = q.popleft()
            if n==N-1 and m==M-1:
                return cnt+1
            if br:
                for i in range(4):
                    if 0 <= n + dx[i] < N and 0 <= m + dy[i] < M:
                        if my_map[n + dx[i]][m + dy[i]]:
                            continue
                        if not visited[n + dx[i]][m+dy[i]]:
                            visited[n + dx[i]][m+dy[i]] = br + 1
                            tmp.append((n + dx[i], m + dy[i], br))
            else:
                for i in range(4):
                    if 0 <= n + dx[i] < N and 0 <= m + dy[i] < M:
                        if visited[n + dx[i]][m + dy[i]] != 1:
                            if my_map[n + dx[i]][m + dy[i]]:
                                visited[n + dx[i]][m + dy[i]] = 2
                                tmp.append((n + dx[i], m + dy[i], 1))
                            else:
                                visited[n + dx[i]][m + dy[i]] = 1
                                tmp.append((n + dx[i], m + dy[i], br))
        if tmp:
            q.extend(tmp)
        else: break
        cnt += 1
        tmp.clear()
    return -1

print(bfs())