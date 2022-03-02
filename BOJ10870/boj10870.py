N = int(input())


def fibo2(N):
    global memo
    if N >= 2 and N >= len(memo):
        memo.append(fibo2(N-1) + fibo2(N-2))
    return memo[N]


memo = [0, 1]
print(fibo2(N))
