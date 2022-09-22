import sys

sys.stdin = open('input.txt')

N = int(input())
A = list(map(int, input().split()))
memo = A[:]
memo[0] = A[0]
for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            memo[i] = max(memo[i], memo[j] + A[i])
ans = max(memo)
print(ans)