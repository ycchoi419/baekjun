N = int(input())

arr = [[0 for i in range(10)] for j in range(N)]
for i in range(1, 10):
    arr[0][i] = 1
for i in range(1, N):
    for j in range(9):
        arr[i][j] += arr[i-1][j+1]
    for j in range(1, 10):
        arr[i][j] += arr[i-1][j-1]
ans = 0
for i in range(10):
    ans += arr[-1][i]
print(ans%1000000000)