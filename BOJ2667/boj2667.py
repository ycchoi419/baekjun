import sys
from collections import deque

sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
my_map = [list(map(int, input())) for _ in range(N)]
visited = [[0 for i in range(N)] for j in range(N)]
need_visited = deque()
ans = []
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = 1
            if my_map[i][j]:
                need_visited.append([i, j])
                cnt = 1
                while need_visited:
                    n = need_visited.pop()
                    for ii, jj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        if (0 <= n[0] + ii < N and 0 <= n[1] + jj < N):
                            if not visited[n[0] + ii][n[1] + jj]:
                                visited[n[0] + ii][n[1] + jj] = 1
                                if my_map[n[0] + ii][n[1] + jj]:
                                    need_visited.append([n[0] + ii, n[1] + jj])
                                    cnt += 1
                ans.append(cnt)

print(len(ans))
for i in sorted(ans):
    print(i)