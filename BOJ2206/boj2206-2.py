import sys
from collections import deque

sys.stdin = open('input.txt')

N, M = map(int, input().split())
my_map = [list(map(int, input())) for _ in range(N)]
visited_zero = [[0 for i in range(M)] for j in range(N)]
visited_one = [[0 for i in range(M)] for j in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(n, m):
    q = deque()
    q.append((n, m, 0, 1))
    while q:
        i, j, br, cnt = q.popleft()
        if cnt == 1000000:
            return -1
        if i == N-1 and j == M-1:
            return cnt
        if my_map[i][j]: # 벽일 때
            if br:  # 한 번 부순 상태일 때
                continue
            else:
                # if visited_one[i][j]:
                #     continue
                # else:
                visited_one[i][j] = 1
                # visited_zero[i][j] = 1
                for k in range(4):
                    if i + dx[k] < 0 or i + dx[k] >= N:
                        continue
                    if j + dy[k] < 0 or j + dy[k] >= M:
                        continue
                    # if not visited_one[i + dx[k]][j + dy[k]]:
                    #     visited_one[i + dx[k]][j + dy[k]] = 1
                    #     q.append((i + dx[k], j + dy[k], 1, cnt+1))
        else:
            # if visited_zero[i][j]:
            #     continue
            for k in range(4):
                if i + dx[k] < 0 or i + dx[k] >= N:
                    continue
                if j + dy[k] < 0 or j + dy[k] >= M:
                    continue
                # if br:
                #     if not visited_one[i + dx[k]][j + dy[k]]:
                #         visited_one[i + dx[k]][j + dy[k]] = 1
                # else:
                #     if not visited_zero[i + dx[k]][j + dy[k]]:
                #         visited_zero[i + dx[k]][j + dy[k]] = 1
                q.append((i + dx[k], j + dy[k], br, cnt+1))
    return -1

print(bfs(0,0))