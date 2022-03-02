N = int(input())


def factorial(N):
    global memo
    if N >= 1 and N >= len(memo):
        memo.append(factorial(N-1)*N)
    return memo[N]


memo = [1]
print(factorial(N))
