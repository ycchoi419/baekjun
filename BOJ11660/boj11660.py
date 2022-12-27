import sys

sys.stdin = open('input.txt')

N, M = map(int, input().split())
arr = [[0 for i in range(N+1)] for j in range(N+1)]
for i in range(N):
    l = list(map(int, input().split()))
    for j in range(N):
        arr[i+1][j+1] = arr[i+1][j] + arr[i][j+1] + l[j] - arr[i][j]
# for i in range(N):
#     for j in range(N):
#         arr[i+1][j+1] = arr[i][j+1] + arr[i+1][j+1]
for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(arr[x2][y2]-arr[x1-1][y2]-arr[x2][y1-1]+arr[x1-1][y1-1])