import sys

sys.stdin = open('input.txt')

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
ans = 64
for i in range(N-7):
    for j in range(M-7):
        black = 0
        white = 0
        for ii in range(8):
            for jj in range(8):
                if (ii+jj)%2:
                    if board[i+ii][j+jj] == 'B':
                        black += 1
                else:
                    if board[i + ii][j + jj] == 'B':
                        white += 1
        ans = min(ans, 32 - black + white, 32 + black - white)
print(ans)