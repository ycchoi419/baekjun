from sys import stdin

stdin = open('input.txt')

N, M, K = map(int, stdin.readline().split())
board = [list(stdin.readline().rstrip()) for _ in range(N)]
bk_cnt = [[0 for i in range(M+1)] for j in range(N+1)]
wt_cnt = [[0 for i in range(M+1)] for j in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        if ((i+j)%2 and board[i-1][j-1]=='B') or (not (i+j)%2 and board[i-1][j-1]=='W'):
            bk_cnt[i][j] = bk_cnt[i][j - 1] + bk_cnt[i - 1][j] - bk_cnt[i - 1][j - 1] + 1
            wt_cnt[i][j] = wt_cnt[i][j - 1] + wt_cnt[i - 1][j] - wt_cnt[i - 1][j - 1]
        else:
            bk_cnt[i][j] = bk_cnt[i][j - 1] + bk_cnt[i - 1][j] - bk_cnt[i - 1][j - 1]
            wt_cnt[i][j] = wt_cnt[i][j - 1] + wt_cnt[i - 1][j] - wt_cnt[i - 1][j - 1] + 1
ans = K ** 2
for i in range(N-K+1):
    for j in range(M-K+1):
        ans = min(ans, bk_cnt[i+K][j+K] - bk_cnt[i][j+K] - bk_cnt[i+K][j] + bk_cnt[i][j], wt_cnt[i+K][j+K] - wt_cnt[i][j+K] - wt_cnt[i+K][j] + wt_cnt[i][j])
print(ans)