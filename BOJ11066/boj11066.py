import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))
    add = files[:]
    for i in range(1, K):
        add[i] += add[i-1]
    add.append(0)
    dp = [[0] * K for _ in range(K + 1)]  # dp[i][j]는 j부터 연속한 i개 파일 더하는 경우 중 최소의 값
    for i in range(2, K + 1):
        for j in range(K - i + 1):
            dp[i][j] = 1000000000 * i
            for k in range(1, i):
                dp[i][j] = min(dp[k][j] + dp[i-k][j+k] + add[j+i-1] - add[j-1], dp[i][j])
    print(dp[-1][0])