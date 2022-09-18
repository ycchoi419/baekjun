import sys

sys.stdin = open('input.txt')

N = int(input())
wine = [0] * N
for i in range(N):
    wine[i] = int(input())
arr = [[0] * 3 for _ in range(N)]
arr[0][1] = wine[0]
for i in range(1, N):
    arr[i][0] = max(arr[i-1])
    arr[i][1] = arr[i-1][0] + wine[i]
    arr[i][2] = arr[i-1][1] + wine[i]

ans = max(arr[-1])
print(ans)