import sys
from collections import deque

sys.stdin = open('input.txt')

N, M = map(int, input().split())
my_map = [list(map(int, input())) for _ in range(N)]
visited_zero = [[0 for i in range(M)] for j in range(N)]
visited_one = [[0 for i in range(M)] for j in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

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
                        if not visited_zero[n + dx[i]][m+dy[i]] and not visited_one[n + dx[i]][m+dy[i]]:
                            tmp.append((n + dx[i], m + dy[i], br))
            else:
                for i in range(4):
                    if 0 <= n + dx[i] < N and 0 <= m + dy[i] < M:
                        if not visited_zero[n + dx[i]][m + dy[i]]:
                            if my_map[n + dx[i]][m + dy[i]]:
                                tmp.append((n + dx[i], m + dy[i], 1))
                            else:
                                tmp.append((n + dx[i], m + dy[i], br))
        if tmp:
            q.extend(tmp)
        else: break
        while tmp:
            n, m, br = tmp.popleft()
            if br:
                visited_one[n][m] = 1
            else:
                visited_zero[n][m] = 1
        cnt += 1
    return -1

print(bfs())