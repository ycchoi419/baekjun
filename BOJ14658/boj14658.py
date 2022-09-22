# 메모리 초과
import sys

sys.stdin = open('input.txt')

N, M, L, K = map(int, input().split())
arr = [[0] * (N + L + 3) for _ in range(M + L + 3)]
for _ in range(K):
    x, y = map(int, input().split())
    arr[y][x] += 1
    arr[y][x+L+2] -= 1
    arr[y+L+2][x] -= 1
    arr[y+L+2][x+L+2] += 1
for i in range(M+L+3):
    for j in range(1, N+L+3):
        arr[i][j] += arr[i][j-1]
for j in range(N+L+3):
    for i in range(1, M+L+3):
        arr[i][j] += arr[i-1][j]
ans = 0
for i in arr:
    ans = max(ans, max(i))
ans = K - ans
print(ans)