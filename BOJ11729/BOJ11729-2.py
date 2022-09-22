N = int(input())
# memo[n][i][j]는 n층 탑을 i에서 j로 옮기는 정답 배열
memo = [[[[] for j in range(4)] for i in range(4)] for n in range(N)]
for i in range(1,4):
    for j in range(1,4):
        memo[0][i][j] = [[i, j]]

def sol(n, i, j):
    if memo[n][i][j]:
        return memo[n][i][j]
    else:
        k = 6 - i - j
        memo[n][i][j] = sol(n-1, i, k) + [[i, j]] + sol(n-1, k, j)
        return memo[n][i][j]

sol(N-1, 1, 3)
print(len(memo[N-1][1][3]))
for i in memo[N-1][1][3]:
    print(*i)